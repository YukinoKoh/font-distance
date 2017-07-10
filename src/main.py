import os
import jinja2
import webapp2
from google.appengine.ext import db

from models import JpFamily
from models import EnFamily
from handlers import Distance
from handlers import List
from handlers import Sort
from handlers import SetCookie
import settings
settings.init()

app = webapp2.WSGIApplication([('/list/([a-zA-Z0-9_-]+)', List),
                               ('/sort', Sort),
                               ('/', Distance),
                               ('/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_-]+)',SetCookie)
                               ],
                              debug=True)
