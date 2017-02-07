#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_meta_ultra_api
----------------------------------

Tests for `meta_ultra_api` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from meta_ultra_api import meta_ultra_api
from meta_ultra_api import cli



class TestMeta_ultra_api(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'meta_ultra_api.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output