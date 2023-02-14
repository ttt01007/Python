import pytest


def test_case01():
    '''
        注释1
    '''
    print('用例1')
    assert 1 == 1


def test_case02():
    '''
        注释2
    '''
    print('用例2')
    assert 1 == 2


if __name__ == '__main__':
    pytest.main(['-s', '-v', '--capture=sys', '--html=./report/report.html'])
