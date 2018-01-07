import json
import os

import pytest
import responses as responses_lib


@pytest.fixture
def fixture_file():

    def _loader(file_path):  # NOQA
        path = os.path.join('tests/fixtures/files', file_path)
        with open(path, 'r') as f:
            return f.read()

    return _loader


@pytest.fixture
def json_fixture_file(fixture_file):

    def _loader(file_path):
        return json.loads(fixture_file(file_path))

    return _loader


@pytest.yield_fixture
def responses():
    responses_lib.start()

    yield responses_lib

    responses_lib.stop()
    responses_lib.reset()


def _plugins(path=None):
    dotted_paths = []
    if not path:
        path = os.path.join(os.path.abspath('.'), 'tests/fixtures')

    for filename in os.listdir(path):
        if os.path.isdir(os.path.join(path, filename)):
            dotted_paths += _plugins(path=os.path.join(path, filename))
        else:
            name, extension = os.path.splitext(filename)
            if extension != '.py' or name == '__init__':
                continue

            rel_path = os.path.relpath(path)
            path_parts = rel_path.split('/')[1:]  # ignore first directory
            plugin_dir = '.'.join(path_parts)
            dotted_paths.append('{}.{}'.format(plugin_dir, name))

    return dotted_paths


# so pytest can find and use the .py files within the 'fixtures'  directory
pytest_plugins = _plugins()
