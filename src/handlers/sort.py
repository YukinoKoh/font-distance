import settings
from handler import Handler
from models import JpFamily
from models import EnFamily
import util
from handler import select_font


# page to layout all blogs
class Sort(Handler):
    @select_font
    def get(self, lang):
        # insert font to en database
        select_lang = lang
        if lang == 'jp':
            select_font = self.jp
        if lang == 'en':
            select_font = self.en
        view='sort-'+lang
        distance_list = util.get_log_list(select_font, select_lang)
        sort_list = util.get_sorted_list(distance_list[1])
        select_font = util.get_selected_font(self.jp, self.en)
        self.render("sort.html", ref_font=distance_list[0],
                    fonts=sort_list, view=view, jp_lang=settings.JP, en_lang=settings.EN,
                    jp_font=select_font[0], en_font=select_font[1],
                    sitename=settings.SITENAME)

    def post(self):
        pass
