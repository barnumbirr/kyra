#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from datetime import datetime

class Logger(object):

    def __init__(self, filename = None):
        self.__filename = filename
        self.__ERROR = '{0}'.format('\033[91m[ERROR]\033[0m :: ')
        self.__WARNING = '{0}'.format('\033[93m[WARNING]\033[0m :: ')
        self.__INFO = '{0}'.format('\033[94m[INFO]\033[0m :: ')
        self.__NORMAL = '{0}'.format('\033[0m[NORMAL]\033[0m :: ')
        self.__GOOD = '{0}'.format('\033[92m[GOOD]\033[0m :: ')
        self.__FUNCTION = '{0}{1}'.format('\033[95m[FUNCTION]\033[0m', ' :: ')

    def __write(self, filename, content):
        with open(os.path.abspath(filename), 'a') as f:
            f.write('{0}{1}'.format(content, '\n'))

    def __formatter(self, error, msg):
        return('{0}{1}{2}'.format(self.__timestamp(), error, msg))

    def __timestamp(self):
        t_current = datetime.now()
        t_ordered = datetime.strftime(t_current, '%d-%m-%Y %H:%M:%S')
        return('{0}{1}'.format(t_ordered, ' :: '))

    def __function_call(self, fn, retval, *args):
        if self.__filename != None:
            self.__write(self.__filename, '{0}{1}{2}{3}{4}{5}'.format(self.__timestamp(), self.__FUNCTION, fn.__name__, retval, ' returned ', str(*args)))
        else:
            print('{0}{1}{2}{3}{4}{5}'.format(self.__timestamp(), self.__FUNCTION, fn.__name__, retval, ' returned ', str(*args)))

    def error(self, msg):
        if self.__filename != None:
            self.__write(self.__filename, self.__formatter(self.__ERROR, msg))
        else:
            print(self.__formatter(self.__ERROR, msg))

    def warning(self, msg):
        if self.__filename != None:
            self.__write(self.__filename, self.__formatter(self.__WARNING, msg))
        else:
            print(self.__formatter(self.__WARNING, msg))

    def info(self, msg):
        if self.__filename != None:
            self.__write(self.__filename, self.__formatter(self.__INFO, msg))
        else:
            print(self.__formatter(self.__INFO, msg))

    def normal(self, msg):
        if self.__filename != None:
            self.__write(self.__filename, self.__formatter(self.__NORMAL, msg))
        else:
            print(self.__formatter(self.__NORMAL, msg))

    def good(self, msg):
        if self.__filename != None:
            self.__write(self.__filename, self.__formatter(self.__GOOD, msg))
        else:
            print(self.__formatter(self.__GOOD, msg))

    def decorator(self, fn):
        def wrapper(*args):
            return_value = fn(*args)
            self.__function_call(fn, return_value, args)
            return return_value
        return wrapper
