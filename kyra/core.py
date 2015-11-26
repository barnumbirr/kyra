#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

__title__ = 'kyra'
__version__ = '0.2'
__author__ = 'Martin Simon <me@martinsimon.me>'
__repo__ = 'https://github.com/mrsmn/kyra'
__license__ = 'Apache v2.0 License'

class Logger(object):

    def __init__(self, filename=None):
        self.filename = filename
        self.ERROR = '{0}'.format('\033[91m[ERROR]\033[0m :: ')
        self.WARNING = '{0}'.format('\033[93m[WARNING]\033[0m :: ')
        self.INFO = '{0}'.format('\033[94m[INFO]\033[0m :: ')
        self.NORMAL = '{0}'.format('\033[0m[NORMAL]\033[0m :: ')
        self.GOOD = '{0}'.format('\033[92m[GOOD]\033[0m :: ')
        self.FUNCTION = '{0}{1}'.format('\033[95m[FUNCTION]\033[0m', ' :: ')
        
    def __write(self, filename, content):
        with open(filename, 'a') as f:
            f.write('{0}{1}'.format(content, '\n'))
    
    def __formatter(self, error, text):
        return('{0}{1}{2}'.format(self.__timestamp(), error, text))

    def __timestamp(self):
        time_now = datetime.now()
        time_ordered = datetime.strftime(time_now, '%d-%m-%Y %H:%M:%S')
        return('{0}{1}'.format(time_ordered, ' :: '))

    def function_call(self, fn, retval, *args):
        print('{0}{1}{2}{3}{4}{5}'.format(self.__timestamp(), self.FUNCTION, fn.__name__, retval, ' returned ', str(*args)))

    def error(self, text):
        if self.filename != None:
            self.__write(self.filename, self.__formatter(self.ERROR, text))
        else:
            return(self.__formatter(self.ERROR, text))

    def warning(self, text):
        if self.filename != None:
            self.__write(self.filename, self.__formatter(self.WARNING, text))
        else:
            return(self.__formatter(self.WARNING, text))

    def info(self, text):
        if self.filename != None:
            self.__write(self.filename, self.__formatter(self.INFO, text))
        else:
            return(self.__formatter(self.INFO, text))

    def normal(self, text):
        if self.filename != None:
            self.__write(self.filename, self.__formatter(self.NORMAL, text))
        else:
            return(self.__formatter(self.NORMAL, text))

    def good(self, text):
        if self.filename != None:
            self.__write(self.filename, self.__formatter(self.GOOD, text))
        else:
            return(self.__formatter(self.GOOD, text))

def loggable(fn):
    def wrapper(*args):
        return_value = fn(*args)
        Logger().function_call(fn, return_value, args)
        return return_value
    return wrapper
