
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='got',
    version='0.0.1',
    description='Got: A a git based undo tree. Commit often? Got it.',
    python_requires='==3.*,>=3.6.0',
    project_urls={"homepage": "https://github.com/CircArgs/got", "repository": "https://github.com/CircArgs/got"},
    author='Nick Ouellet',
    author_email='nicholas.p.ouellet@gmail.com',
    license='Apache-2.0',
    keywords='git got commit source control',
    entry_points={"console_scripts": ["got = got:run"]},
    packages=['got', 'got.cli', 'got.cli.commands', 'got.events', 'got.macros', 'got.service', 'got.utils'],
    package_dir={"": "."},
    package_data={},
    install_requires=['cleo==0.*,>=0.8.1', 'colorama==0.*,>=0.4.3'],
    extras_require={"dev": ["black==19.*,>=19.10.0.b0", "dephell==0.*,>=0.8.3", "pylint==2.*,>=2.5.2", "pytest==3.*,>=3.0.0", "pytest-cov==2.*,>=2.4.0"]},
)
