import pytest
from Homework18.code_for_testing import Human

@pytest.fixture
def human():
    print('setup for test')
    yield Human('Abelard', 62, 'black')
    print('teardown')
