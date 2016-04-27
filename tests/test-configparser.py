#!/usr/bin/env python
import unittest
import os
try:
    from ConfigParser import RawConfigParser, ConfigParser, SafeConfigParser  # noqa
except ImportError:
    from configparser import RawConfigParser, ConfigParser, SafeConfigParser  # nowa

# configparser.InterpolationSyntaxError: '%' must be followed by '%' or '(', found:
ini_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sample.ini')


class test_configparser(unittest.TestCase):

    def test_configparser(self):
        x = RawConfigParser()
        x.read(ini_filename)
        path = x.get('general', 'path')
        assert path == 'feature%2Fcool'

    def test_rawconfigparser(self):
        x = RawConfigParser()
        x.read(ini_filename)
        path = x.get('general', 'path')
        assert path == 'feature%2Fcool'

    def test_safeconfigparser(self):
        x = RawConfigParser()
        x.read(ini_filename)
        path = x.get('general', 'path')
        assert path == 'feature%2Fcool'
