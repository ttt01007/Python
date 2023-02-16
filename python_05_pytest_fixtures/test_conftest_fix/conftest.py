import pytest


@pytest.fixture(scope='session', autouse=True)
def fix_a():
    print('setup 用例前置操作')
    yield
    print('teardown 用例后置操作')
