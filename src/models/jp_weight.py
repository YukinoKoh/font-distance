from google.appengine.ext import db


# Database
# font db
def font_key(name='default'):
    return db.Key.from_path('fonts', name)


class JpWeight(db.Model):
    family = db.StringProperty(required=True)
    name = db.StringProperty(required=True)
    style = db.StringProperty(required=True)
    weight = db.FloatProperty(required=True)
    distance = db.FloatProperty(required=True)

    def get_position(cls):
        position_style = 'left: '+ str(cls.distance*1000)+'px'
        return position_style
