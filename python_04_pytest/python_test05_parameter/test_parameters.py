import pytest


@pytest.mark.parametrize('a,b', [('tsw', 'damajiang'), ('zjy', 'dapuke')])
def test_01(a, b):
    print('\n' + a + ":" + b)


if __name__ == '__main__':
    pytest.main(['-s', 'test_parameter.py'])
