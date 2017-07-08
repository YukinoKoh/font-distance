from models import JpWeight
from models import JpFamily


# pass cookie font val, which is font.style 
def get_distance_list(select_font):
    font_list = JpWeight.all()
    ref_font = JpWeight.get_by_key_name(select_font)
    ref_num = get_num(ref_font.family, ref_font.weight)

    log_font = []
    for font in font_list:
        its_num = get_num(font.family, font.weight)
        # if the font is the selected one.
        if ref_font.name == font.name:
            font.distance = 0.0
        # compare if their category, and weight are same
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
    return ref_font, log_font

# get key num based on weight db info
def get_num(family, weight):
    # get key num from its family db
    family_set = JpFamily.get_by_key_name(str(family))
    # category, width balance
    cwb = family_set.get_num()
    return cwb[0], cwb[1], cwb[2], weight



def font_select(func):
    """
    A decorator to set cookie 
    """
    def set_font(self, *args, **kwargs):
        # Redirect to login if user not logged in, else execute func.
        if not self.jp:
            self.jp = 'kozuka_gothic_pro_r'
        else:
            func(self, *args, **kwargs)
    return set_font
