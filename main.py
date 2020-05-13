

from lib import make_pairs
from glib import makegfx
from source import getd


def prepare_data():
    k, v = list(getd().schema.items())[0]
    pairs = {0: []}
    make_pairs(k, v, pairs, 0)
    return pairs



if __name__ == '__main__':
    pairs = prepare_data()
    makegfx(getd().title, pairs, getd().voc, getd().link)
