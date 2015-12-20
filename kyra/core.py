#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from datetime import datetime

class Logger(object):

    def __init__(self, filename=None):
        self._filename = filename
        self._ERROR = '{0}'.format('\033[91m[ERROR]\033[0m :: ')
        self._WARNING = '{0}'.format('\033[93m[WARNING]\033[0m :: ')
        self._INFO = '{0}'.format('\033[94m[INFO]\033[0m :: ')
        self._NORMAL = '{0}'.format('\033[0m[NORMAL]\033[0m :: ')
        self._GOOD = '{0}'.format('\033[92m[GOOD]\033[0m :: ')
        self._FUNCTION = '{0}{1}'.format('\033[95m[FUNCTION]\033[0m', ' :: ')

    def _write(self, filename, content):
        with open(os.path.abspath(filename), 'a') as f:
            f.write('{0}{1}'.format(content, '\n'))

    def _formatter(self, error, msg):
        return('{0}{1}{2}'.format(self._timestamp(), error, msg))

    def _timestamp(self):
        t_current = datetime.now()
        t_ordered = datetime.strftime(t_current, '%d-%m-%Y %H:%M:%S')
        return('{0}{1}'.format(t_ordered, ' :: '))

    def _function_call(self, fn, retval, *args):
        if self._filename != None:
            self._write(self._filename, '{0}{1}{2}{3}{4}{5}'.format(self._timestamp(), self._FUNCTION, fn.__name__, retval, ' returned ', str(*args)))
        else:
            print('{0}{1}{2}{3}{4}{5}'.format(self._timestamp(), self._FUNCTION, fn.__name__, retval, ' returned ', str(*args)))

    def error(self, msg):
        if self._filename != None:
            self._write(self._filename, self._formatter(self._ERROR, msg))
        else:
            return(self._formatter(self._ERROR, msg))

    def warning(self, msg):
        if self._filename != None:
            self._write(self._filename, self._formatter(self._WARNING, msg))
        else:
            return(self._formatter(self._WARNING, msg))

    def info(self, msg):
        if self._filename != None:
            self._write(self._filename, self._formatter(self._INFO, msg))
        else:
            return(self._formatter(self._INFO, msg))

    def normal(self, msg):
        if self._filename != None:
            self._write(self._filename, self._formatter(self._NORMAL, msg))
        else:
            return(self._formatter(self._NORMAL, msg))

    def good(self, msg):
        if self._filename != None:
            self._write(self._filename, self._formatter(self._GOOD, msg))
        else:
            return(self._formatter(self._GOOD, msg))

    def decorator(self, fn):
        def wrapper(*args):
            return_value = fn(*args)
            self._function_call(fn, return_value, args)
            return return_value
        return wrapper
