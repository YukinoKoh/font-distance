import settings
from handler import Handler
from models import JpFamily
import util
from handler import select_font


# page to layout all blogs
class Distance(Handler):
    @select_font
    def get(self):
        # insert font to en database
        select_font = self.font
        select_lang = self.lang
        view = 'distance'
        fonts = util.get_distance_list(select_font, select_lang)
        # self.response.out.write(select_font)
        self.render("distance.html", ref_font=fonts[0], fonts=fonts[1], view=view,
                    en_lang=settings.EN, jp_lang=settings.JP, sitename=settings.SITENAME)

