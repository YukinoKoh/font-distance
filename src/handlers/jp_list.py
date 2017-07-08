from handler import Handler
import settings
from models import JpFamily
from models import JpWeight
from jp_center import insert_jp


# page to layout all blogs
class JpList(Handler):
    def get(self):
        # insert family to en database
        insert_jp()
        family_list = JpFamily.all()

        lang = 'jp'
        select_font = self.jp
        ref_font = JpWeight.get_by_key_name(select_font)
        self.render('font_list.html', family_list=family_list,
                    lang=lang, ref_font=ref_font,
                    sitename=settings.SITENAME)


    def post(self):
        url = '/'
        self.redirect(url)
