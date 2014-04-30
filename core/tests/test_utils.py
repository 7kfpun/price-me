#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.utils import *


def test_is_url():
    assert is_url("http://www.kfpun.com")


def test_is_not_url():
    assert not is_url("htt://www.kfpun.com")
    assert not is_url("www.kfpun.com")
    assert not is_url("http://www.kfpun.c")


def test_avg():
    assert avg([1, 2, 3, 4, 5]) == 3
    assert avg([1.1, 1.2]) == 1.15
    assert avg([1.1]) == 1.1


def test_pie():
    expected = {
        '1.0 - 1.8': [1],
        '1.8 - 2.6': [2],
        '2.6 - 3.4': [3],
        '3.4 - 4.2': [4],
        '4.2 - 5.0': [5],
    }
    assert pie([1, 2, 3, 4, 5]) == expected, \
        '{} is not equal to {}'.format(pie([1, 2, 3, 4, 5]), expected)

# lint_ignore=W0401
