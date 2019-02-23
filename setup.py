from setuptools import setup, find_packages

setup(
    name = 'nanopy',
    version = '0.0.1',
    url = 'https://github.com/AndreasAlbert/nanopy.git',
    author = 'Andreas Albert',
    author_email = 'andreas.albert@cern.ch',
    description = 'HEP Analysis on flat TTrees, like CMS NanoAOD',
    packages = find_packages(),    
    install_requires = [''],
)