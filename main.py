

from lib import make_pairs
from glib import makegfx
from source import module_dict

T = module_dict.get('seutil_run_setfiles')

def prepare_data():
    k, v = list(T().schema.items())[0]
    pairs = {0: []}
    make_pairs(k, v, pairs, 0)
    return pairs



if __name__ == '__main__':
    pairs = prepare_data()
    makegfx(T().title, pairs, T().voc, T().link)
