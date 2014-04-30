# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.path.insert(0, 'libs')
sys.setdefaultencoding("utf-8")

from taobao import Taobao
from utils import avg, pie
import jinja2
import logging
import os
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

        template = JINJA_ENVIRONMENT.get_template('index.html')
        rendered_page = template.render()

        self.response.write(rendered_page)

    def post(self):
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'

        search = self.request.get("search")
        logger.info(search)
        self.response.write('<br /><br />')
        self.response.write(search)
        template = JINJA_ENVIRONMENT.get_template('hello.html')

        taobao = Taobao(search)
        #self.response.write(taobao.get_all_h3())
        #self.response.write(taobao.get_all_prices())
        #self.response.write(taobao.get_all_price_per_units())
        #self.response.write(taobao.get_unit())
        #logger.info(taobao.get_all())
        logger.info(pie(taobao.get_all_prices()))

        rendered_page = template.render(
            search=search,
            average_price=avg(taobao.get_all_prices()),
            average_price_per_unit=avg(taobao.get_all_price_per_units())
            if taobao.has_unit() else 0,
            stat=taobao.get_all(),
            unit=taobao.get_unit(),
            all_prices_pie=pie(taobao.get_all_prices(), 10),
            all_price_per_units_pie=pie(taobao.get_all_price_per_units(), 10),
        )
        self.response.write(rendered_page)

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
