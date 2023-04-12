

from setuptools import setup

APP = ['main.py']
DATA_FILES = [
    'images/__init__.py',
    'images/compress.py',
    'images/helper.py',
]
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
