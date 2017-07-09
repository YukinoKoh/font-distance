from handler import Handler
import settings
from models import JpFamily
from jp_center import insert_jp
from util import select_font


# page to layout all blogs
class JpList(Handler):
    @select_font
    def get(self):
        # insert family to en database
        insert_jp()
        jp_lang = 'jp'
        jp_gothic_list = JpFamily.all().filter('category =','gothic')
        jp_mincho_list = JpFamily.all().filter('category =','mincho')
        select_font = self.font
        ref_font = JpFamily.get_by_key_name(select_font)
        self.render('font_list.html', jp_gothic_list=jp_gothic_list,
                    jp_mincho_list=jp_mincho_list,
                    ref_font=ref_font, jp_lang=jp_lang,
                    sitename=settings.SITENAME)


    def post(self):
        url = '/'
        self.redirect(url)
