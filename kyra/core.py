#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

__title__ = 'kyra'
__version__ = '0.1.1'
__author__ = 'Martin Simon <me@martinsimon.me>'
__repo__ = 'https://github.com/mrsmn/kyra'
__license__ = 'Apache v2.0 License'

class Logger(object):

    ERROR = '{0}'.format('\033[91m[ERROR]\033[0m :: ')
    WARNING = '{0}'.format('\033[93m[WARNING]\033[0m :: ')
    INFO = '{0}'.format('\033[94m[INFO]\033[0m :: ')
    NORMAL = '{0}'.format('\033[0m[NORMAL]\033[0m :: ')
    GOOD = '{0}'.format('\033[92m[GOOD]\033[0m :: ')
    FUNCTION = '{0}{1}'.format('\033[95m[FUNCTION]\033[0m', ' :: ')
    
    @staticmethod
    def __timestamp():
        time_now = datetime.now()
        time_ordered = datetime.strftime(time_now, '%d-%m-%Y %H:%M:%S')
        return('{0}{1}'.format(time_ordered, ' :: '))

    @classmethod
    def function_call(self, fn, retval, *args):
        print('{0}{1}{2}{3}{4}{5}'.format(self.__timestamp(), self.FUNCTION, fn.__name__, retval, ' returned ', str(*args)))

    @classmethod
    def error(self, text):
        return('{0}{1}{2}'.format(self.__timestamp(), self.ERROR, text))

    @classmethod
    def warning(self, text):
        return('{0}{1}{2}'.format(self.__timestamp(), self.WARNING, text))

    @classmethod
    def info(self, text):
        return('{0}{1}{2}'.format(self.__timestamp(), self.INFO, text))

    @classmethod
    def normal(self, text):
        return('{0}{1}{2}'.format(self.__timestamp(), self.NORMAL, text))

    @classmethod
    def good(self, text):
        return('{0}{1}{2}'.format(self.__timestamp(), self.GOOD, text))

def loggable(fn):
    def wrapper(*args):
        return_value = fn(*args)
        Logger.function_call(fn, args, return_value)
        return return_value
    return wrapper
