from google.appengine.ext import db


# Database
# font db
class JpFamily(db.Model):
    name = db.StringProperty(required=True)
    style = db.StringProperty(required=True)
    category = db.StringProperty(required=True,
               choices=('mincho', 'gothic', 'other'))
    width = db.FloatProperty(required=True)
    form_balance = db.FloatProperty(required=True)
    yoko_tate_balance = db.FloatProperty(required=True)
    angle = db.FloatProperty(required=True)
    line_thickness = db.FloatProperty(required=True)
    design = db.StringProperty(required=True)
    # aggregation of width, form_b
    distance_v = db.FloatProperty(required=True)
    # angle, line_thickness, line_b
    distance_h = db.FloatProperty(required=True)
    # sum of abs of  distance_v and distance_h
    distance = db.FloatProperty(required=True)
    lang = db.StringProperty(required=True)

    def get_position(cls):
        position_style = 'left: '+str(cls.distance_h*10+10)+'%;top :'+str(cls.distance_v*5+50)+'%'
        return position_style

    def get_num(cls):
        category = cls.category
        num1 = cls.width
        num2 = cls.form_balance *2
        num3 = cls.yoko_tate_balance
        num4 = cls.angle *0.01
        num5 = cls.line_thickness *0.15
        return category, num1, num2, num3, num4, num5
