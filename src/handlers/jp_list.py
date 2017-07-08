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
        if self.jp:
            select_font = self.jp
        else:
            select_font = 'kozuka_gothic_pro_r'
        self.render('font_list.html', family_list=family_list,
                    lang=lang, select_font=select_font,
                    sitename=settings.SITENAME)


    def post(self):
        url = '/'
        self.redirect(url)
