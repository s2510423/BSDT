from setuptools import setup, find_packages

setup(
    name = 'BSDT',
    version = '0.0.0',
    author = 'Brainless',
    author_email = 's2621019@siheung.hs.kr',
    description = 'Bootleg Scientific Data Toolkit',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    url = 'httpe://github.com/s2510423/BSDT',
    packages = find_packages(),
    install_requires = ['pandas','numpy','openpyxl'],
    classifiers = [
        'Programming Language :: Python :: 3',
        'Liscence :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires = '>=3.8',
)