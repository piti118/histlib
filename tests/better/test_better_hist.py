import pytest

from histlib.better import hist as hbh
from histlib.better.hist import KeyValue


def test_find_hist_simple():
    d = ['a', 'a', 'b']
    got = hbh.find_hist(d)
    exp = {'a': 2, 'b': 1}
    assert got == exp  # yes you can compare dict like this


def test_find_hist_should_strip():
    d = ['a\n', 'a', 'b']
    got = hbh.find_hist(d)
    exp = {'a': 2, 'b': 1}
    assert got == exp  # yes you can compare dict like this


def test_find_hist_should_give_empty_dict_for_empty_iterable():
    d = []
    got = hbh.find_hist(d)
    assert got == {}


def test_find_max_key_value_simple():
    got = hbh.max_key_value({'a': 2, 'b': 1})
    exp = KeyValue(key='a', value=2)
    assert got == exp


def test_find_max_key_value_should_return_last_one_on_tie():
    # write this kind of test only this is the guarantee behavior of the function.
    got = hbh.max_key_value({'a': 2, 'b': 2})
    exp = KeyValue(key='a', value=2)
    assert got == exp


def test_find_max_key_value_should_raise_when_given_empty_dict():
    with pytest.raises(ValueError) as excinfo:
        got = hbh.max_key_value({})
        assert 'Empty' in excinfo.value


def test_hist_then_find_max():
    # Integration test but with typing it's not really needed
    # way back before we have typing this is useful
    # make sure output of one fits into input of another
    d = ['a', 'a', 'b']
    hist = hbh.find_hist(d)
    hbh.max_key_value(hist)  # just make sure it doesn't crash
