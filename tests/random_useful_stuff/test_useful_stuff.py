from pytest import approx


# def test_with_logging():
#     # need log_cli=true
#     logging.info('info')
#     time.sleep(5)
#     logging.warning('warning')
#     assert False

def test_approx():
    assert 1 == approx(0.9999999999999999999999999999999999999999999999)
    assert 1 == approx(0.9, abs=0.2)

def test_magic_number_here(magic_number):
    # see conftest.py
    assert magic_number == 123
