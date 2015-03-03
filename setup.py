#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'kyra',
    version = '0.0.1',
    url = 'https://github.com/c0ding/kyra',
    download_url = 'https://github.com/c0ding/kyra/archive/master.zip',
    author = 'c0ding',
    author_email = 'me@martinsimon.me',
    license = 'Apache v2.0 License',
    packages = ['kyra'],
    description = 'Small logging libray I made for my own use.',
    long_description = file('README.md','r').read(),
    keywords = ['logging'],
)
