from models import JpFamily
from models import EnFamily
from jp_center import insert_jp
from en_center import insert_en

# pass cookie font val, which is font.style 
def get_distance_list(select_font, select_lang):
    
    ref_font = get_font(select_font, select_lang)
    jp_font_list = JpFamily.all()
    en_font_list = EnFamily.all()
    jp_log = calc_distance(ref_font, jp_font_list)
    en_log = calc_distance(ref_font, en_font_list)
    log_font = jp_log + en_log
    return ref_font, log_font


def get_sorted_list(log_font):
    sorted_font = []
    for font in log_font:
        font.distance = abs(font.distance_v) + abs(font.distance_h)
        sorted_font.append(font)
        font.put()
    sorted_font.sort(key = lambda x: x.distance)
    return sorted_font

def get_font(select_font, select_lang):
    if select_lang == 'jp':
        ref_font = JpFamily.get_by_key_name(select_font)
    if select_lang == 'en':
        ref_font = EnFamily.get_by_key_name(select_font)
    return ref_font


def calc_distance(ref_font, font_list):
    log_font = []
    ref_num = ref_font.get_num()
    for font in font_list:
        # if the font is the selected one.
        if ref_font.name == font.name:
            font.distance_v = 0.0
            font.distance_h = 0.0
            font.distance = 0.0
        # return only in the same category
        else:
            its_num = font.get_num()
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
            font.distance = 0.0
            log_font.append(font)
        font.put()
    return log_font
