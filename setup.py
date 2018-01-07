from setuptools import setup


setup(
  name = 'rai',
  packages = ['rai'],
  version = '0.0.1',
  license = 'MIT',
  description = 'A high-level client for interacting with Raiblocks nodes',
  author = 'Kevin Kennell',
  author_email = 'kevin@kennell.de',
  install_requires=[
        'requests',
        'netaddr'
  ],
  url = 'https://github.com/kennell/rai',
  keywords = ['raiblocks', 'cryptocurrency'],
  classifiers = [],
)