#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'kyra',
    version = '0.4',
    url = 'https://github.com/mrsmn/kyra',
    download_url = 'https://github.com/mrsmn/kyra/archive/master.zip',
    author = 'Martin Simon <me@martinsimon.me>',
    author_email = 'me@martinsimon.me',
    license = 'Apache v2.0 License',
    packages = ['kyra'],
    description = 'Small logging libray I made for my own use.',
    long_description = open('README.md','r').read(),
    keywords = ['logging'],
)
