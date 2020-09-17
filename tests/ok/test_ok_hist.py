from os.path import dirname, join

import histlib.ok.main as hom


def test_hist():
    fname = join(dirname(__file__), '../fixtures/test.txt') # always use relative path
    out = hom.do_it(fname)
    assert out.min_counter == 166233
    assert out.max_counter == 167029
    assert out.min_key == 'a'
    assert out.max_key == 'd'
