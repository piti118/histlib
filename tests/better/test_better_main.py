import subprocess
from os.path import join, dirname

from histlib.better import main as hbm


def test_hist():
    # integration test
    fname = join(dirname(__file__), '../fixtures/test.txt')
    out = hbm.do_it(fname)
    assert out.min_counter == 166233
    assert out.max_counter == 167029
    assert out.min_key == 'a'
    assert out.max_key == 'd'


def test_main():
    # this is end to end test if you really want to simulate user
    fname = join(dirname(__file__), '../fixtures/test.txt')
    out = subprocess.check_output(f'python -m histlib.better.main {fname}', shell=True)
    assert b'Min Key = a' in out
    assert b'Max Key = d' in out
