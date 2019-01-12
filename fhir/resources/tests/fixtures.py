import hashlib
import io
import os
import pytest
import pathlib
import tempfile
import shutil
import sys
import zipfile

PARSER_PATH = pathlib.Path(os.path.abspath(__file__)).parents[3] / 'fhir-parser'
SCRIPT_PATH = pathlib.Path(os.path.abspath(__file__)).parents[3] / 'script'
CACHE_PATH = pathlib.Path(os.path.abspath(__file__)).parents[3] / '.cache'


def download_and_store(url, path):
    """ """
    import requests
    try:
        sys.stdout.write('Attempting to download from {0}\n'.format(url))
        ret = requests.get(url)
    except requests.HTTPError as exc:
        raise LookupError(
            'Failed to download. Full error: {0!s}'.format(exc)
        )
    else:
        if not ret.ok:
            raise Exception("Failed to download {0}".format(url))
        with io.open(path, 'wb') as handle:
            for chunk in ret.iter_content():
                handle.write(chunk)
            sys.stdout.write(
                'Download has been completed, now saved to {0}\n'.format(path)
            )


def expand(self, local):
    """ Expand the ZIP file at the given path to the cache directory.
    """
    path = os.path.join(self.cache, local)
    assert os.path.exists(path)
    import zipfile  # import here as we can bypass its use with a manual unzip

    with zipfile.ZipFile(path) as z:
        z.extractall(self.cache)


@pytest.fixture(scope='session')
def base_settings():

    if not CACHE_PATH.exists():
        CACHE_PATH.mkdir()

    settings = {}

    with io.open(str(SCRIPT_PATH / 'settings.py'), 'r') as fp:
        exec(fp.read(), settings)

    example_data_file_uri = settings['specification_url'] + '/examples-json.zip'

    example_data_file_id = \
            hashlib.md5(example_data_file_uri.encode()).hexdigest()

    example_data_file_location = CACHE_PATH / (example_data_file_id + '.zip')

    if not example_data_file_location.exists():
        download_and_store(
            example_data_file_uri,
            str(example_data_file_location))

    temp_data_dir = tempfile.mkdtemp()
    # extract all files from archive and put into temp dir
    with zipfile.ZipFile(str(example_data_file_location)) as z:
        z.extractall(temp_data_dir)

    if 'FHIR_UNITTEST_DATADIR' not in os.environ:
        os.environ.setdefault('FHIR_UNITTEST_DATADIR', temp_data_dir)

    yield settings

    shutil.rmtree(temp_data_dir)
