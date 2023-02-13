import pytest


class Test_ABC:
    def test_a(self):
        print('test_a')
        assert 1 == 1

    @pytest.mark.skipif(condition=2 > 1, reason='废弃,跳过')
    def test_b(self):
        print('test_b')
        assert 1 == 2


if __name__ == '__main__':
    pytest.main(['-s', './test_skipif.py'])
