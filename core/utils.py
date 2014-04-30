#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def is_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain... # noqa
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return bool(regex.match(url))


def avg(list_):
    return float(sum(list_)) / len(list_) if len(list_) > 0 else float('nan')


def pie(list_, groups=5):
    if not list_:
        return {}
    max_ = max(list_)
    min_ = min(list_)
    step = float(max_ - min_) / groups
    return {
        '{} - {}'.format(min_ + i * step, min_ + (i + 1) * step): [
            data for data in sorted(list_)
            if i * step <= data - min_ <= (i + 1) * step]
        for i in range(groups)
    }
