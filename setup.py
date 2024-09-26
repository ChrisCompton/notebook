# pip install -e .
from setuptools import setup, find_packages

setup(
    name='mkdocs-marp-plugin',
    version='0.8.1',
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'marp = marp.marp:Marp',
        ]
    }
)