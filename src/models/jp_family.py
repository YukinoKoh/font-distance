from google.appengine.ext import db


# Database
# font db
class JpFamily(db.Model):
    name = db.StringProperty(required=True)
    category = db.StringProperty(required=True,
               choices=('mincho', 'gothic', 'other'))
    width = db.FloatProperty(required=True)
    balance = db.FloatProperty(required=True)
    line = db.FloatProperty(required=True)
    style = db.StringProperty(required=True)
    distance = db.FloatProperty(required=True)

    def get_position(cls):
        position_style = 'left: '+ str(cls.distance*1000)+'px'
        return position_style

    def get_num(cls):
        category = cls.category
        width = cls.width
        balance = cls.balance
        line = cls.line
        return category, width, balance, line
