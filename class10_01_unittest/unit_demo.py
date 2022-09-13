import unittest


class UnitDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_01(self):
        print('01')
        self.tsw()

    def test_02(self):
        print('02')

    def tsw(self):
        print('TSW')


if __name__ == '__main__':
    unittest.main
