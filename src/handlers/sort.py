import settings
from handler import Handler
from models import JpFamily
from models import EnFamily
import util
from util import select_font


# page to layout all blogs
class Sort(Handler):
    @select_font
    def get(self):
        # insert font to en database
        select_font = self.font
        select_lang = self.lang
        sort_list = util.get_distance_list(select_font, select_lang)
        self.render("sort.html", ref_font=sort_list[0],
                    fonts=sort_list[1], sitename=settings.SITENAME)

    def post(self):
        pass
