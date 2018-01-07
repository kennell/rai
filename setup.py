from setuptools import setup


setup(
  name = 'rai',
  packages = ['rai'],
  version = '0.0.8',
  license = 'MIT',
  description = 'A high-level, pythonic client for interacting with Raiblocks nodes',
  author = 'Kevin Kennell',
  author_email = 'kevin@kennell.de',
  install_requires=[
    'requests'
  ],
  url = 'https://github.com/kennell/rai',
  keywords = ['raiblocks', 'cryptocurrency'],
  classifiers = [],
)
