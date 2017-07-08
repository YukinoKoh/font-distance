import os
import jinja2
import webapp2
from google.appengine.ext import db

from models import EnFont
from models import JpFamily
from handlers import EnDistance
from handlers import JpDistance
from handlers import JpList
from handlers import JpSort
from handlers import SetCookie
import settings
settings.init()

app = webapp2.WSGIApplication([('/', EnDistance),
                               ('/jplist', JpList),
                               ('/jpsort', JpSort),
                               ('/jp', JpDistance),
                               ('/~([a-zA-Z0-9_-]+)/([a-zA-Z0-9_-]+)',SetCookie)
                               ],
                              debug=True)
