import pytest


@pytest.mark.parametrize('a', ['aaa', 'bbb'])
def test_01(a):
    print('\n' + a)


if __name__ == '__main__':
    pytest.main(['-s', 'test_single_parameter.py'])
