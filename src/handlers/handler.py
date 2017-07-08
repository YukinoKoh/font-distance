# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
import jinja2
import webapp2

import settings
from models import JpFamily
import util

# handling templates with jinja2
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


# base handler
class Handler(webapp2.RequestHandler):
    ''' handle site'''
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    # render message page
    def render_message(self, message):
        self.render("message.html", sitename=settings.sitename,
                    message=message)

    def set_cookie(self, lang, font_style):
        # self.response.headers['Content-Type'] = 'text/plain'
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        cookie_key = str(lang)
        cookie_val = str(font_style)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (cookie_key, cookie_val))

    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        jp_select = self.request.cookies.get('jp')
        if not jp_select:
            self.set_cookie('jp', 'kozuka_gothic_pro_r')
        en_select = self.request.cookies.get('en')
        self.jp = jp_select
        self.en = en_select

