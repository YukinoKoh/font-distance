from handler import Handler
import settings
from models import JpFamily
from jp_center import insert_jp
import util


# page to layout all blogs
class JpDistance(Handler):
    def get(self):
        # insert font to en database
        insert_jp()
        select_font = self.jp
        fonts = util.get_distance_list(select_font)
        # list_font = fonts[1]
        # self.response.out.write(list_font[2].distance)
        self.render("jp_distance.html", ref_font=fonts[0], fonts=fonts[1], sitename=settings.SITENAME)


    def post(self):
        keyname = self.request.get("font_selected")
        if EnFont.get_by_key_name(keyname):
            font_selected = EnFont.get_by_key_name(keyname)
        else:
            message = 'Something went wrong...'
            self.render_message(message, sitename=settings.SITENAME)

        fonts = EnFont.all().order('name')
        self.render("main.html", fonts=fonts, font_selected=font_selected,
                    sitename=settings.SITENAME)
