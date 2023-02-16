import pytest

@pytest.fixture(scope='session', autouse=True)
def login():
    print('用例先登录')