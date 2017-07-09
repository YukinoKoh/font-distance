from handler import Handler
import settings
from models import JpFamily
from jp_center import insert_jp
import util
from util import select_font


# page to layout all blogs
class Distance(Handler):
    @select_font
    def get(self):
        # insert font to en database
        insert_jp()
        select_font = self.font
        fonts = util.get_distance_list(select_font)
        # self.response.out.write(select_font)
        self.render("distance.html", ref_font=fonts[0], fonts=fonts[1], sitename=settings.SITENAME)


    def post(self):
        pass
