
from itertools import cycle

WIDE = 10
HEIGHT = 5
HORIZONTAL_COLOR_SET = ('rgb(0,133,229)', 'rgb(40,121,180)', 'rgb(70,113,144)')
SHAPE_SET = ('linear', 'vhv')  #spline


def hcol():
    return cycle(HORIZONTAL_COLOR_SET)

def shape():
    return cycle(SHAPE_SET)

def textpos(n: int, row_width, txt_lvl, shape):
    if n == 0:
        return 'left', 'middle'
    elif n == (row_width):
       return'right', 'middle'
    else:
        if shape == 'vhv:':
            return 'center', 'bottom'
        txt_lvl = 'top' if txt_lvl == 'bottom' else 'bottom'
        return 'center', txt_lvl

def calc_height(y0, n):
    return y0 - HEIGHT - (0.1 * HEIGHT) if (n % 2) else y0 - HEIGHT + (0.1 * HEIGHT)

