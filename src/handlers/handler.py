# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
import jinja2
import webapp2

import settings
from models import JpFamily
from jp_center import insert_jp
from en_center import insert_en
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

    def set_cookie(self, key, val):
        # self.response.headers['Content-Type'] = 'text/plain'
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        cookie_key = str(key)
        cookie_val = str(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (cookie_key, cookie_val)
             )

    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        self.jp = self.request.cookies.get('jp')
        self.en = self.request.cookies.get('en')
        self.latest = self.request.cookies.get('latest')

def select_font(func):
    """
    A decorator to set cookie 
    """
    def set_font(self, *args, **kwargs):
        insert_jp()
        insert_en()
        if not self.jp:
            self.set_cookie('jp', 'kozuka_gothic_pro')
        if not self.en:
            self.set_cookie('en', 'adobe_garamond')
        if not self.latest:
            self.redirect('/jp/kozuka_gothic_pro/distance')
        else:
            func(self, *args, **kwargs)
    return set_font

