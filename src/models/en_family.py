from google.appengine.ext import db


# Database
# font db
class EnFamily(db.Model):
    name = db.StringProperty(required=True)
    style = db.StringProperty(required=True)
    category = db.StringProperty(required=True,
               choices=('sans', 'serif', 'other'))
    x_glyph_width = db.FloatProperty(required=True)
    x_height = db.FloatProperty(required=True)
    m_serif = db.FloatProperty(required=True)
    h_stem_horizontal_balance = db.FloatProperty(required=True)
    o_stroke_axis = db.FloatProperty(required=True)
    p_decender = db.FloatProperty(required=True)
    i_line_thickness = db.FloatProperty(required=True)
    # aggregation of width, form_b
    distance_v = db.FloatProperty(required=True)
    # angle, line_thickness, line_b
    distance_h = db.FloatProperty(required=True)
    lang = db.StringProperty(required=True)

    def get_position(cls):
        position_style = 'left: '+str(cls.distance_h+50)+'%;top :'+str(cls.distance_v*150+50)+'%'
        return position_style

    def get_num(cls):
        category = cls.category
        x_glyph_width = cls.x_glyph_width
        x_height = cls.x_height
        m_serif = cls.m_serif
        h_stem_horizontal_balance = cls.h_stem_horizontal_balance
        o_stroke_axis = cls.o_stroke_axis
        p_decender  = cls.p_decender
        i_line_thickness = cls.i_line_thickness
        num1 = x_glyph_width
        num2 = x_height + p_decender/2
        num3 = h_stem_horizontal_balance
        num4 = o_stroke_axis+m_serif + m_serif
        num5 = i_line_thickness        
        return category, num1, num2, num3, num4, num5 
