# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.path.insert(0, 'libs')
sys.setdefaultencoding("utf-8")

from bs4 import BeautifulSoup
import jinja2
import logging
import os
import requests
import webapp2


logger = logging.getLogger(__name__)


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        os.path.join(os.path.dirname(__file__), "templates"),
    ),
    extensions=[
        'jinja2.ext.i18n',
        'jinja2.ext.autoescape',
    ]
)


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.write('Hello, World!')

        template = JINJA_ENVIRONMENT.get_template('hello.html')
        rendered_page = template.render()

        self.response.write(rendered_page)

    def post(self):
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.write('Hello, World!')

        search = self.request.get("search")
        logger.info(search)
        self.response.write('<br /><br />')
        self.response.write(search)
        template = JINJA_ENVIRONMENT.get_template('hello.html')
        rendered_page = template.render(search=search)

        self.response.write(rendered_page)

        if search:
            response = requests.get(
                u'http://s.taobao.com/search?q={}'.format(search))
            if response.status_code == 200:
                soup = BeautifulSoup(
                    response.content.decode('gbk').encode('utf8'))
                print soup.prettify
                #self.response.write('<br /><br />')
                self.response.write(
                    [div for div in soup.find_all("div", class_="price")])


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
