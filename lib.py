

def make_pairs(pk, que, pairs, lvl):
    #print(pk, '---', que, '---', pairs, end='\n\n')
    if isinstance(que, str):
        pairs[lvl].append((pk, que))
        return
    down = []
    while len(que) > 0:
        t = que.pop(0)
        pairs[lvl].append((pk, t)) if isinstance(t, str) else None
        if isinstance(t, dict):
            k, v = list(t.items())[0]
            pairs[lvl].append((pk, k))
            down.append(t)
    if len(down) > 0:
        pairs[lvl + 1] = [] if pairs.get(lvl+1) is None else pairs[lvl + 1]
    while len(down) > 0:
        t = down.pop(0)
        k, v = list(t.items())[0]
        make_pairs(k, v, pairs, lvl+1)
    return pairs
