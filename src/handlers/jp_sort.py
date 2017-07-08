from handler import Handler
import settings
from models import JpFamily
from jp_center import insert_jp
import util


# page to layout all blogs
class JpSort(Handler):
    def get(self):
        # insert font to en database
        insert_jp()
        lang = 'jp'

        font_list = JpFamily.all()

        select_font = self.jp
        sort_list = util.get_distance_list(select_font)
        self.render("jp_sort.html", ref_font=sort_list[0],
                    fonts=sort_list[1], sitename=settings.SITENAME)

    def post(self):
        pass
