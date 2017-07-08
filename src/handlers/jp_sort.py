from handler import Handler
import settings
from models import JpFamily
from models import JpWeight
from jp_center import insert_jp


# page to layout all blogs
class JpSort(Handler):
    def get(self):
        # insert font to en database
        insert_jp()
        lang = 'jp'
        if self.jp:
            select_font = self.jp
        else:
            select_font = 'kozuka_gothic_pro_b'

        font_list = JpWeight.all()
        ref_font = JpWeight.get_by_key_name(select_font) 
        ref_num = self.get_num(ref_font.family, ref_font.weight)

        log_font = []
        for font in font_list:
            its_num = self.get_num(font.family, font.weight)
            # if the font is the selected one.
            if ref_font.name == font.name:
                font.distance = 0.0
                log_font.append(font)
            # compare category
            elif ref_font.family != font.family and ref_font.weight == font.weight and ref_num[0] == its_num[0]: 
                # compare width
                dis_width = abs(its_num[1] - ref_num[1])
                # compare balance
                dis_balance = abs(its_num[2] - ref_num[2])
                # scaling
                font.distance = dis_width + dis_balance 
                log_font.append(font)
            else:
                font.distance = 1000.0
            font.put()
        log_font.sort(key = lambda x: x.distance)
        # self.response.out.write(page)
        self.render("jp_sort.html", ref_font=ref_font,
                    fonts = log_font, sitename=settings.SITENAME)

    # get key num based on weight db info
    def get_num(self, family, weight):
        # get key num from its family db
        family_set = JpFamily.get_by_key_name(str(family))
        # category, width balance
        cwb = family_set.get_num()
        return cwb[0], cwb[1], cwb[2], weight

    def post(self):
        pass
