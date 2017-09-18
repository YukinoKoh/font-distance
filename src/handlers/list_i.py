from handler import Handler
import settings
from models import JpFamily
from models import EnFamily
from jp_center import insert_jp
from en_center import insert_en
from handler import select_font
import util


# page to layout all blogs
class List(Handler):
    @select_font
    def get(self, view):
        
        # find ref_font: if it is English 
        if view.find('en') != -1: 
            select_lang = 'en'
            select_font = self.en
        elif view.find('jp') != -1:
            select_lang = 'jp'
            select_font = self.jp
        else:
            select_lang = self.latest
            if select_lang == 'en':
                select_font = self.en
            if select_lang == 'jp':
                select_font = self.jp
        en_sans_list = EnFamily.all().filter('category =','sans')
        en_serif_list = EnFamily.all().filter('category =','serif')
        jp_sans_list = JpFamily.all().filter('category =','gothic')
        jp_serif_list = JpFamily.all().filter('category =','mincho')
        ref_font = util.get_font(select_font, select_lang)
        select_font = util.get_selected_font(self.jp, self.en)

        self.render('list.html', en_sans_list=en_sans_list,
                    en_serif_list=en_serif_list, jp_sans_list=jp_sans_list,
                    jp_serif_list=jp_serif_list,
                    ref_font=ref_font, view=view, jp_lang=settings.JP, en_lang=settings.EN,
                    jp_font=select_font[0], en_font=select_font[1],
                    sitename=settings.SITENAME)

