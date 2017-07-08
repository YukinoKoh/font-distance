from models import JpFamily


def insert_jp():
    #insert jp sans to dp
    category='gothic'

    # typekit
    family = 'A-OTF Bothic BBB Pr6N'
    # width/height of Kanji
    width = 47.0/47.0
    # hiragane devided by kanji
    form_balance = 37.0*37.0/(47.0*47.0)
    # thinest diveded by thickest
    line_balance = 3.0/4.0
    # horizontal line of hiragane
    angle = 8.0
    # thickness of vertical line of  hiragane
    line_thickness = 0.0
    insert_family(family, category, width, form_balance, line_balance, angle, line_thickness)

    family = 'Heisei Kaku Gothic Std'
    width = 81.0/80.0
    form_balance = 70.0*75.0/(81.0*80.0)
    line_balance = 8.0/7.8
    angle = 5.8
    line_thickness = 0.0
    insert_family(family, category, width, form_balance, line_balance, angle, line_thickness)

    family = 'Ryo Gothic PlusN'
    width = 90.0/91.0
    form_balance = 75.0/85.0
    line_balance = 7.0/7.0
    angle = 5.7
    line_thickness = 0.0
    insert_family(family, category, width, form_balance, line_balance, angle, line_thickness)

    family = 'Source Han Sans Japanese'
    width = 88.0/89.0
    form_balance = 81.0*77.0/(88.0*89.0)
    line_balance = 7.0/8.0
    angle = 2.8
    line_thickness = 0.0
    insert_family(family, category, width, form_balance, line_balance, angle, line_thickness)

    family = 'Kozuka Gothic Pr6N'
    width = 81.0/80.0
    form_balance = 71.0*77.0/(81.0*80.0)
    line_balance = 6.0/6.0
    angle = 2.9
    line_thickness = 0.0
    insert_family(family, category, width, form_balance, line_balance, angle, line_thickness)

    family = 'Kozuka Gothic Pro'
    width = 81.0*81.0
    form_balance = 71.0*76.0/(81.0*81.0)
    line_balance = 6.0/6.0
    angle = 2.9
    line_thickness = 0.0
    insert_family(family, category, width, form_balance, line_balance, angle, line_thickness)

    # google font
    family = 'Noto Sans Japanese'
    width = 1.0
    form_balance = 0.95
    line_balance = 1.05
    angle = 1.0
    line_thickness = 1.0
    insert_family(family, category, width, form_balance, line_balance, angle, line_thickness)

    family = 'Sawarabi Gothic'
    width = 0.9
    form_balance = 0.75
    line_balance = 1.0
    angle = 1.0
    line_thickness = 0.0
    insert_family(family, category, width, form_balance, line_balance, angle, line_thickness)

    family = 'Rounded Mplus 1c'
    width = 1.1
    form_balance = 0.94
    line_balance = 1.0
    angle = 1.0
    line_thickness = 0.0
    insert_family(family, category, width, form_balance, line_balance, angle, line_thickness)

    family = 'Mplus 1p'
    width = 1.1
    form_balance = 0.95
    line_balance = 1.0
    angle = 1.0
    line_thickness = 0.0
    insert_family(family, category, width, form_balance, line_balance, angle, line_thickness)


def insert_family(family, category, width, form_balance, line_balance, angle, line_thickness):
    key_name = family.lower().replace(' ', '_')
    if not JpFamily.get_by_key_name(family):
        style = key_name
        family_insert = JpFamily(key_name=key_name, name=family, 
                             category=category, width=width, 
                             form_balance=form_balance, style=style,
                             line_balance=line_balance, angle=angle, 
                             line_thickness=line_thickness, distance_v=0.0,
                             distance_h=0.0).put()

