from models import JpFamily


def insert_jp():
    #insert jp sans to dp
    # measurements are
    # width: width / height
    # form_balabce: hiragana 'a' / kanji 'ei' area
    # yoko_tate_balance = yokosen height / tatesen width of kanji'ei'
    # angle = yokosen of hiragana 'a'
    # line_thickness = chrome 500% screen capture font-size: 20px

    # Mincho 
    category='mincho'
    # typekit
    name = 'Kozuka Mincho Pr6N'
    width = 97.0/95.0
    form_balance = 83.0*89.0/(97.0*95.0)
    yoko_tate_balance = 2.0/6.0
    angle = 9.8
    line_thickness = 5.0
    insertJp(name, category, width, form_balance, yoko_tate_balance, angle, line_thickness)
    
    name = 'Kozuka Mincho Pro'
    width = 99.0/96.0
    form_balance = 82.0*89.0/(99.0*96.0)
    yoko_tate_balance = 2.0/6.0
    angle = 8.7
    line_thickness = 6.0
    insertJp(name, category, width, form_balance, yoko_tate_balance, angle, line_thickness)
    
    name = 'Heisei Mincho StdN'
    width = 94.0/90.0
    form_balance = 77.0*86.0/(94.0*90.0)
    yoko_tate_balance = 3.0/7.0
    angle = 7.5
    line_thickness = 5.0
    insertJp(name, category, width, form_balance, yoko_tate_balance, angle, line_thickness)
    
    name = 'Ryo Text PlusN'
    width = 98.0/94.0
    form_balance = 75.0*86.0/(98.0*94.0)
    yoko_tate_balance = 2.0/7.0
    angle = 12.2
    line_thickness = 4.5
    insertJp(name, category, width, form_balance, yoko_tate_balance, angle, line_thickness)
    
    name = 'Ryo Display PlusN'
    width = 97.0/95.0
    form_balance = 76.0*86.0/(97.0*95.0)
    yoko_tate_balance = 2.0/9.0
    angle = 12.5
    line_thickness = 6.0
    insertJp(name, category, width, form_balance, yoko_tate_balance, angle, line_thickness)
    
    name = 'Source Han Serif Japanese'
    width = 96.0/93.0
    form_balance = 77.0*84.0/(96.0*93.0)
    yoko_tate_balance = 3.0/7.0
    angle = 9.3
    line_thickness = 5.0
    insertJp(name, category, width, form_balance, yoko_tate_balance, angle, line_thickness)
    
    name = 'A-OTF Ryumin PR6N'
    width = 95.0/93.0
    form_balance = 78.0*90.0/(95.0*93.0)
    yoko_tate_balance = 2.0/5.0
    angle = 9.7
    line_thickness = 6.0
    insertJp(name, category, width, form_balance, yoko_tate_balance, angle, line_thickness)
    
    name = 'A-OTF Futo Min A101 PR6N'
    width = 94.0/94.0
    form_balance = 71.0*87.0/(94.0*94.0)
    yoko_tate_balance = 2.0/7.0
    angle = 10.5
    line_thickness = 6.0
    insertJp(name, category, width, form_balance, yoko_tate_balance, angle, line_thickness)
    
    # google font 
    name = 'Sawarabi Mincho'
    width = 92.0/94.0
    form_balance = 78.0*85.0/(92.0*94.0)
    yoko_tate_balance = 2.0/8.0
    angle = 9.8
    line_thickness = 7.0
    insertJp(name, category, width, form_balance, yoko_tate_balance, angle, line_thickness)

    category='gothic'

    # typekit
    name = 'A-OTF Bothic BBB Pr6N'
    # width/height of Kanji
    width = 47.0/47.0
    # hiragane devided by kanji
    form_balance = 37.0*37.0/(47.0*47.0)
    # thinest diveded by thickest
    yoko_tate_balance = 3.0/4.0
    # horizontal line of hiragane
    angle = 8.0
    # thickness of vertical line of  hiragane
    line_thickness = 8.0
    insertJp(name, category, width, form_balance, yoko_tate_balance, angle, line_thickness)

    name = 'Heisei Kaku Gothic Std'
    width = 81.0/80.0
    form_balance = 70.0*75.0/(81.0*80.0)
    yoko_tate_balance = 8.0/7.8
    angle = 5.8
    line_thickness = 7.0
    insertJp(name, category, width, form_balance, yoko_tate_balance, angle, line_thickness)

    name = 'Ryo Gothic PlusN'
    width = 90.0/91.0
    form_balance = 75.0*85.0/(90.0*91.0)
    yoko_tate_balance = 7.0/7.0
    angle = 5.7
    line_thickness = 7.8
    insertJp(name, category, width, form_balance, yoko_tate_balance, angle, line_thickness)

    name = 'Source Han Sans Japanese'
    width = 88.0/89.0
    form_balance = 81.0*77.0/(88.0*89.0)
    yoko_tate_balance = 7.0/8.0
    angle = 2.8
    line_thickness = 8.0
    insertJp(name, category, width, form_balance, yoko_tate_balance, angle, line_thickness)

    name = 'Kozuka Gothic Pr6N'
    width = 81.0/80.0
    form_balance = 71.0*77.0/(81.0*80.0)
    yoko_tate_balance = 6.0/6.0
    angle = 2.9
    line_thickness = 7.0
    insertJp(name, category, width, form_balance, yoko_tate_balance, angle, line_thickness)

    name = 'Kozuka Gothic Pro'
    width = 81.0/81.0
    form_balance = 71.0*76.0/(81.0*81.0)
    yoko_tate_balance = 6.0/6.0
    angle = 2.9
    line_thickness = 8.0
    insertJp(name, category, width, form_balance, yoko_tate_balance, angle, line_thickness)

    # google font
    name = 'Noto Sans Japanese'
    width = 93.0/92.0
    form_balance = 79.0*85.0/(93.0*92.0)
    yoko_tate_balance = 8.0/8.0
    angle = 3.2
    line_thickness = 7.0
    insertJp(name, category, width, form_balance, yoko_tate_balance, angle, line_thickness)

    name = 'Sawarabi Gothic'
    width = 95.0/91.0
    form_balance = 81.0*87.0/(95.0*91.0)
    yoko_tate_balance = 7.0/8.0
    angle = 3.4
    line_thickness = 7.0
    insertJp(name, category, width, form_balance, yoko_tate_balance, angle, line_thickness)

    name = 'Rounded Mplus 1c'
    width = 91.0/90.0
    form_balance = 83.0*88.0/(91.0*90.0)
    yoko_tate_balance = 7.0/7.0
    angle = 0.0
    line_thickness = 7.0
    insertJp(name, category, width, form_balance, yoko_tate_balance, angle, line_thickness)

    name = 'Mplus 1p'
    width = 95.0/91.0
    form_balance = 82.0*88.0/(95.0*91.0)
    yoko_tate_balance = 7.0/8.5
    angle = 0.0
    line_thickness = 7.0
    insertJp(name, category, width, form_balance, yoko_tate_balance, angle, line_thickness)

def insertJp(name, category, width, form_balance, yoko_tate_balance, angle, line_thickness):
    key_name = name.lower().replace(' ', '_')
    if not JpFamily.get_by_key_name(name):
        style = key_name
        family_insert = JpFamily(key_name=key_name, name=name, 
                             category=category, width=width, 
                             form_balance=form_balance, style=style,
                             yoko_tate_balance=yoko_tate_balance, angle=angle, 
                             line_thickness=line_thickness, distance_v=0.0,
                             distance_h=0.0, distance=0.0, lang='jp').put()

