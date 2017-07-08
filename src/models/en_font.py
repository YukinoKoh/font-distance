from google.appengine.ext import db


# Database
# font db
def font_key(name='default'):
    return db.Key.from_path('fonts', name)


class EnFont(db.Model):
    name = db.StringProperty(required=True)
    helvetica = db.FloatProperty(required=True)
    roboto = db.FloatProperty(required=True)
    libre_baskerville = db.FloatProperty(required=True)

    def get_style(cls):
        style_name = cls.name.lower().replace(" ", "_") 
        return style_name

    def get_position(cls, font_selected):
        target = font_selected.name.lower().replace(" ", "_")
        dis = 0
        if target == 'helvetica':
            dis = cls.helvetica
        elif target == 'roboto':
            dis = cls.roboto
        elif target == 'libre_baskerville':
            dis = cls.libre_baskerville
        position_style = 'right: calc(95% * ' + str(dis) + ')'
        return position_style
