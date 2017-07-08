from models import JpFamily
from models import JpWeight


def insert_jp():
    #insert jp sans to dp
    category='gothic'
    family = 'Rounded Mplus 1c'
    width = 1.1
    balance = 0.94
    insert_family(family, category, width, balance)
    insert_weight(family, 'Thin', 200.0)
    insert_weight(family, 'Regular', 400.0)
    insert_weight(family, 'Bold', 600.0)

    family = 'Mplus 1p'
    width = 1.1
    balance = 0.95
    insert_family(family, category, width, balance)
    insert_weight(family, 'Thin', 200.0)
    insert_weight(family, 'Regular', 400.0)
    insert_weight(family, 'Bold', 600.0)

    family = 'Kozuka Gothic Pro'
    width = 0.9
    balance = 0.8
    insert_family(family, category, width, balance)
    insert_weight(family, 'L', 200.0)
    insert_weight(family, 'R', 400.0)
    insert_weight(family, 'B', 600.0)


def insert_family(family, category, width, balance):
    key_name = family.lower().replace(' ', '_')
    if not JpFamily.get_by_key_name(family):
        family_insert = JpFamily(key_name=key_name, name=family, 
                             category=category, width=width, 
                             balance=balance).put()

def insert_weight(family, weight_name, weight):
    name = family+' '+weight_name
    family = family.lower().replace(' ', '_')
    style = name.lower().replace(' ', '_')
    if not JpWeight.get_by_key_name(name):
        font_insert = JpWeight(key_name=style, family=family, 
                               name=name, style=style,
                               weight=weight, distance=0.0).put()
