from models import JpFamily


# pass cookie font val, which is font.style 
def get_distance_list(select_font):
    font_list = JpFamily.all()
    ref_font = JpFamily.get_by_key_name(select_font)
    # returns category, width, form_b, line_b, angle, line
    ref_num = ref_font.get_num()

    log_font = []
    for font in font_list:
        its_num = font.get_num()
        # if the font is the selected one.
        if ref_font.name == font.name:
            font.distance = 0.0
        # compare if their category, and weight are same
        elif ref_num[0] == its_num[0]:
            # compare width
            dis_width = its_num[1] - ref_num[1]
            # compare form balance
            dis_form_b = its_num[2] - ref_num[2]
            # compare line balance 
            dis_line_b = abs(its_num[3] - ref_num[3])
            # compare angle 
            dis_angle = abs(its_num[4] - ref_num[4])
            # compare line thickness
            dis_line = its_num[5] - ref_num[5]
            # scaling
            font.distance_v = dis_width + dis_form_b
            font.distance_h = (dis_line_b + dis_angle)*dis_line
            log_font.append(font)
        else:
            font.distance = 1000.0
        font.put()
    log_font.sort(key = lambda x: x.distance_v)
    return ref_font, log_font



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
