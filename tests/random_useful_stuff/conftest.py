import pytest


@pytest.fixture(scope='session')  # run exactly once per test session
def magic_number() -> int:
    return 123
