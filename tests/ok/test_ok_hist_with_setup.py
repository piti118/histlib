import os
import tempfile

import pytest

from histlib.ok.main import do_it, MinMaxKeyCounter


@pytest.fixture(scope='module')
def input_file() -> str:
    data = ['a', 'a', 'a', 'b', 'c', 'c']
    print('Setup')
    with tempfile.NamedTemporaryFile('w', delete=False) as f:
        for d in data:
            f.write(d + '\n')
        f.close()  # windows namedtempfile can't be reopen unless it's closed.
        yield f.name
        os.unlink(f.name)
        print('File is closed')  # print will not appear unless you do capture=no


def test_with_setup(input_file: str):
    got = do_it(input_file)
    expected = MinMaxKeyCounter(min_key='b', max_key='a', min_counter=1, max_counter=3)
    assert got == expected


def test_with_setup_again(input_file: str):
    got = do_it(input_file)
    expected = MinMaxKeyCounter(min_key='b', max_key='a', min_counter=1, max_counter=3)
    assert got == expected
