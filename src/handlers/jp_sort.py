import settings
from handler import Handler
from models import JpFamily
from jp_center import insert_jp
import util
from util import font_select


# page to layout all blogs
class JpSort(Handler):
    @font_select
    def get(self):
        # insert font to en database
        insert_jp()
        select_font = self.font
        sort_list = util.get_distance_list(select_font)
        self.render("jp_sort.html", ref_font=sort_list[0],
                    fonts=sort_list[1], sitename=settings.SITENAME)

    def post(self):
        pass
