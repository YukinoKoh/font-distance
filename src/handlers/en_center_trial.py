from models import EnFont


def insert_enFont():
    # insert font db
    name = 'Roboto'
    if not EnFont.get_by_key_name(name):
        font_insert = EnFont(key_name=name, name=name, helvetica=0.9,
                             roboto=1.0, zilla_slab=0.3,
                             libre_baskerville=0.4).put()
    name = 'Helvetica'
    if not EnFont.get_by_key_name(name):
        font_insert = EnFont(key_name=name, name=name, helvetica=1.0,
                             roboto=0.9, zilla_slab=0.3,
                             libre_baskerville=0.3).put()
    name = 'Libre Baskerville'
    if not EnFont.get_by_key_name(name):
        font_insert = EnFont(key_name=name, name=name, helvetica=0.3,
                             roboto=0.4, zilla_slab=0.4,
                             libre_baskerville=1.0).put()


