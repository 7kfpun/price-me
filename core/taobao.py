# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import logging
import requests


logger = logging.getLogger(__name__)


class Taobao:

    def __init__(self, search):
        self.search = search

        self.response = requests.get(
            u'http://s.taobao.com/search?q={}'.format(search))

        if self.response.status_code == 200:
            self.soup = BeautifulSoup(self.response.text, from_encoding='utf8')

    def get_length(self):
        return len(self.get_all_h3())

    def get_all_h3(self):
        return [
            element.get_text().strip() for element
            in self.soup.find_all("h3", {"class": "summary"})
        ]

    def get_all_prices(self):
        return [
            float(element.get_text().replace(u'\uffe5', '')) for element
            in self.soup.find_all("div", {"class": "col price"})
        ]

    def get_all_price_per_units(self):
        return [
            float(element.find('b').get_text()) for element
            in self.soup.find_all(
                "span", {"class": "icon-pit icon-service-duliang"})
        ]

    def get_unit(self):
        element = self.soup.find(
            "span", {"class": "icon-pit icon-service-duliang"})
        return element.find('em').get_text() if element else None

    def has_unit(self):
        return bool(self.get_unit())

    def get_all(self):
        price_per_units = self.get_all_price_per_units() \
            if self.get_all_price_per_units() \
            else [None] * self.get_length()

        return zip(
            self.get_all_h3(),
            self.get_all_prices(),
            price_per_units,
            #self.get_unit(),
        )
