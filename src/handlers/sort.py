import settings
from handler import Handler
from models import JpFamily
from models import EnFamily
import util
from handler import select_font


# page to layout all blogs
class Sort(Handler):
    @select_font
    def get(self):
        # insert font to en database
        select_font = self.font
        select_lang = self.lang
        view='sort'
        distance_list = util.get_distance_list(select_font, select_lang)
        sort_list = util.get_sorted_list(distance_list[1])
        self.render("sort.html", ref_font=distance_list[0],
                    fonts=sort_list, view=view, jp_lang=settings.JP, en_lang=settings.EN,
                    sitename=settings.SITENAME)

    def post(self):
        pass
