from models import JpFamily


def insert_jp():
    #insert jp sans to dp
    category='gothic'
    family = 'Rounded Mplus 1c'
    width = 1.1
    balance = 0.94
    line = 1.0
    insert_family(family, category, width, balance, line)

    family = 'Mplus 1p'
    width = 1.1
    balance = 0.95
    line = 1.0
    insert_family(family, category, width, balance, line)

    family = 'Sawarabi Gothic'
    width = 0.9
    balance = 0.75
    line = 1.0
    insert_family(family, category, width, balance, line)


    family = 'Kozuka Gothic Pro'
    width = 0.9
    balance = 0.8
    line = 1.0
    insert_family(family, category, width, balance, line)


def insert_family(family, category, width, balance, line):
    key_name = family.lower().replace(' ', '_')
    if not JpFamily.get_by_key_name(family):
        style = key_name
        family_insert = JpFamily(key_name=key_name, name=family, 
                             category=category, width=width, 
                             balance=balance, style=style,
                             line=line, distance=0.0).put()

