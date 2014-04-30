#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import requests_cache

from core.taobao import Taobao


class TestTaobao(unittest.TestCase):

    def setUp(self):
        with requests_cache.enabled('fixtures/cache_taobao_ipod'):
            self.taobao = Taobao('ipod')
        assert 'taobao' in self.taobao.response.content, self.taobao.response

    def tearDown(self):
        pass

    def test_taobao_type(self):
        assert type(self.taobao.get_all_h3()) == list
        assert type(self.taobao.get_all_prices()) == list

    def test_taobao(self):
        assert type(self.taobao.get_all_h3()) == list

# lint_ignore=W0401
