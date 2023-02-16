import pytest


# ids使用中文会有乱码,使用conftest.py转码
@pytest.mark.parametrize('a,b', [('tsw', 'damajiang'),
                                 ('zjy', 'dapuke')],
                         ids=['用例1', '用例2'])
def test_01(a, b):
    print('\n' + a + ":" + b)


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_ids.py'])
