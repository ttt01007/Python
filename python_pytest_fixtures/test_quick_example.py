import pytest


@pytest.fixture()
def first_fix():
    return ['a']


def test_string(first_fix):
    first_fix.append('b')

    assert first_fix == ['a', 'b']


if __name__ == '__main__':
    pytest.main(['-s', 'test_quick_example.py'])
