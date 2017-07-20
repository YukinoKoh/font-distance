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
        select_lang = self.latest
        if select_lang == 'jp':
            select_font = self.jp
        elif select_lang == 'en':
            select_font = self.en
        else:
            select_font = self.jp
        intro = self.get_intro()
        view = 'distance'
        fonts = util.get_distance_list(select_font, select_lang)
        # self.response.out.write(select_font)
        self.render("distance.html", ref_font=fonts[0], fonts=fonts[1], intro=intro, view=view,
                    en_lang=settings.EN, jp_lang=settings.JP, sitename=settings.SITENAME)

