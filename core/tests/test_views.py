#!/usr/bin/env python
# -*- coding: utf-8 -*-
from webtest import TestApp

from core.views import application

application = TestApp(application)


def test_index():
    response = application.get('/')
    assert 'taobao' in str(response), response


# lint_ignore=W0401
