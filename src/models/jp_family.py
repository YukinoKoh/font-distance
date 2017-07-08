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
    line_balance = db.FloatProperty(required=True)
    angle = db.FloatProperty(required=True)
    line_thickness = db.FloatProperty(required=True)
    # aggregation of width, form_b
    distance_v = db.FloatProperty(required=True)
    # angle, line_thickness, line_b
    distance_h = db.FloatProperty(required=True)

    def get_position(cls):
        position_style = 'left: '+str(cls.distance_h+50)+'%;top :'+str(cls.distance_v*150+50)+'%'
        return position_style

    def get_num(cls):
        category = cls.category
        width = cls.width
        form_b = cls.form_balance
        line_b = cls.line_balance
        angle = cls.angle
        line = cls.line_thickness
        return category, width, form_b, line_b, angle, line
