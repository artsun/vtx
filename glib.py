
import plotly.graph_objects as go
import webbrowser
from styles import WIDE, HEIGHT, hcol, textpos, shape, calc_height
from ipywidgets import Output, VBox
from plotly.offline import plot


def makegfx(title: str, data: dict, descr: dict, hlink: dict) -> None:
    voc = descr
    fig = go.FigureWidget()
    #fig = go.Figure()
    shape_ = shape()
    y0 = len(data) * HEIGHT  # basic height
    axis = (max(len(x) for x in data.values()) * WIDE)/2  # main vertical axis

    print('axis=', axis)
    txt_lvl = 'top'

    pxy = {0: {data[0][0][0]: (axis, y0)}}


    for level in range(len(data)):
        print('level=', level)
        hcol_ = hcol()
        level_shape = next(shape_)
        # coordinates of parent nodes in level
        pxy[level + 1] = {}   # handle first node
        print(pxy)
        lwide = len(data[level])  # number of nodes in a row * longitude = total length
        x1 = axis - (lwide * WIDE) / 2
        pname = '' if level != 0 else voc.get(data[0][0][0])

        for n, link in enumerate(data[level]):
            x1 = x1 + WIDE
            y1 = calc_height(y0, n) if level_shape == 'linear' else y0 - HEIGHT
            tpxy = pxy[level + 1].get(link[1])
            if tpxy is not None:
                pxy[level + 1].update({link[1]: [tpxy, (x1, y1)]}) if isinstance(tpxy, tuple) else None
                pxy[level + 1][link[1]].append((x1, y1)) if isinstance(tpxy, list) else None
            else:
                pxy[level + 1].update({link[1]: (x1, y1)})  # node for next level
            txy = pxy[level][link[0]]
            if not isinstance(txy, tuple):
                txy = txy.pop(0)
            print('link:', link, 'x0=', txy[0], 'y0=', txy[1], 'x=', x1, 'y=', y1)
            txt_side, txt_lvl = textpos(n, len(data[level]) - 1, txt_lvl, level_shape)

            txt_pos = '{} {}'.format(txt_lvl, txt_side)

            fcolor = 'blue' if voc.get(link[1])[2] else 'black'



            if level == 0 and n == 0:
                hyperlink = hlink.get(link[0])
                fig.add_trace(go.Scatter(
                    x=[txy[0]],
                    y=[txy[1]],
                    name=pname[1],
                    texttemplate=[
                        '{}<br><a href=\"{}\">{}</a>'.format(pname[0], hyperlink.url, hyperlink.name)],
                    #text=[pname[0]],
                    mode='text+markers',
                    hoverinfo='name',
                    hoverlabel=dict(namelength=70),
                    textposition=['top center'],
                    textfont=dict(size=16, color=fcolor),
                    marker=dict(symbol='circle-dot', opacity=1, size=15, color=next(hcol_)),
                    showlegend=False,
                    #cliponaxis=False,
                ))
            hyperlink = hlink.get(link[1])
            hyperlink = '<br><a href=\"{}\">{}</a>'.format(hyperlink.url, hyperlink.name) if hyperlink else ''
            fig.add_trace(go.Scatter(
                x=[txy[0], x1],
                y=[txy[1], y1],
                mode='lines',
                line=dict(color=next(hcol_), width=2, shape=level_shape, simplify=True, dash='dot'),
                hoverinfo='none',
                showlegend=False,
                meta=dict(layer='below')
            ))
            point = go.Scatter(
                x=[x1],
                y=[y1],
                texttemplate=['{}{}'.format(voc.get(link[1])[0], hyperlink)],
                mode='text+markers',
                hovertemplate="{}<extra></extra>".format(voc.get(link[1])[1]),
                hoverlabel=dict(namelength=70),
                textposition=[txt_pos],
                textfont=dict(size=16, color=fcolor),
                marker=dict(symbol='circle-dot', opacity=1, size=15, color=next(hcol_)),
                showlegend=False,
                meta=dict(layer='above'),
                hoveron='points',
                #cliponaxis=
            )
            #point.on_click(update_point)
            fig.add_trace(point)

        y0 = y0 - HEIGHT

    fig.update_layout(title=title, margin=dict(t=40, b=10, r=10, l=10))
    #plot_div = plot(fig, output_type='div', include_plotlyjs=True)


    fig.show()


