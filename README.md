<h1><img src="https://raw.githubusercontent.com/c0ding/kyra/master/doc/kyra.png" height=55 alt="kyra" title="kyra"> kyra</h1>

[![PyPi Version](https://img.shields.io/pypi/v/kyra.svg)](https://pypi.python.org/pypi/kyra/)

**kyra** is a small logging library written in Python I made for my own use. This library has been tested with Python 2.7.x and Python 3.6.x.

## Installation:

From source use

      $ python setup.py install

or install from PyPi

      $ pip install kyra

## Usage:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kyra import Logger

log = Logger()
# An absolute path can be passed to Logger() to log to a file.

@log.decorator
def sum(a, b):
   return a+b
sum(2, 4)

log.error('This tests the ERROR logging call.')

```

## License:

```
Copyright 2014-2017 Martin Simon

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

```

## Buy me a coffee?

If you feel like buying me a coffee (or a beer?), donations are welcome:

```
WDC : WbcWJzVD8yXt3yLnnkCZtwQo4YgSUdELkj
HBN : F2Zs4igv8r4oJJzh4sh4bGmeqoUxLQHPki
DOGE: DRBkryyau5CMxpBzVmrBAjK6dVdMZSBsuS
```
