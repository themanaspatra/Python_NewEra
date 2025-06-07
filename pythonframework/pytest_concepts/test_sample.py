import pytest

@pytest.mark.dependency()
def test_case_1():
    assert 'hello' == 'hai'

@pytest.mark.dependency(depends=['test_case_1'])
def test_case_2():
    assert 1 == 3
