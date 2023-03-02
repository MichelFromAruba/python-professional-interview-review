import sys
from pytest import fixture

# needed for command line execution, until we add 'src' to the PYTHONPATH env variable
sys.path.append('src/')

# fix once we do the PYTHONPATH cleanup
from objects_and_types import scopes


@fixture()
def message():
    m = 'foo'
    print(f'about to yield, m: {m}')
    yield m
    m = None  # non sensiscal but proves a point
    print(f'clean up message, m: {m}')


def test_scopes(message):
    returned_message = scopes.show_message(message)

    assert returned_message is not None
    assert returned_message == message

    print('done test')
