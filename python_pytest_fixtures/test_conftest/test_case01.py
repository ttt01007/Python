import pytest


def test_case01(fix1):
    print('----------用例一----------')


if __name__ == '__main__':
    pytest.main(['-s', 'test_case01.py'])
