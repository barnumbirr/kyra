#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

class Logger():

    def timestamp():
        time_now = datetime.now()
        time_ordered = datetime.strftime(time_now, '%d-%m-%Y %H:%M:%S')
        return('{0}{1}'.format(time_ordered, ' :: '))

    ERROR = '{0}{1}'.format(timestamp(), '\033[91m[ERROR]\033[0m :: ')
    WARNING = '{0}{1}'.format(timestamp(), '\033[93m[WARNING]\033[0m :: ')
    INFO = '{0}{1}'.format(timestamp(), '\033[94m[INFO]\033[0m :: ')
    NORMAL = '{0}{1}'.format(timestamp(), '\033[0m[NORMAL]\033[0m :: ')
    GOOD = '{0}{1}'.format(timestamp(), '\033[92m[GOOD]\033[0m :: ', '%s')
    FUNCTION = '{0}{1}{2}'.format(timestamp(), '\033[95m[FUNCTION]\033[0m', ' :: ')

    @classmethod
    def function_call(self, fn, retval, *args):
        print('{0}{1}{2}{3}{4}'.format(self.FUNCTION, fn.__name__, retval, ' returned ', str(*args)))

    @classmethod
    def error(self, text):
        return('{0}{1}'.format(self.ERROR, text))

    @classmethod
    def warning(self, text):
        return('{0}{1}'.format(self.WARNING, text))

    @classmethod
    def info(self, text):
        return('{0}{1}'.format(self.INFO, text))

    @classmethod
    def normal(self, text):
        return('{0}{1}'.format(self.NORMAL, text))

    @classmethod
    def good(self, text):
        return('{0}{1}'.format(self.GOOD, text))

def loggable(fn):
    def wrapper(*args):
        return_value = fn(*args)
        Logger.function_call(fn, args, return_value)
        return return_value
    return wrapper
