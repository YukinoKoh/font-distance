from google.appengine.ext import db


# Database
# font db
class EnFamily(db.Model):
    # width = x A width / cap height
    # x height = x height / cap height
    # m serif = serif length of m 500% chrome screen - font-size 20px
    # h_stem_horizontal_balance = H horizontal height / H stem width
    # o_stroke_axis = angle 0 - vertical  
    # p_descender = length of p descender / cap height
    # i_line_thickness: thickness of i 500% chrome screen - font-size 20px
    name = db.StringProperty(required=True)
    style = db.StringProperty(required=True)
    category = db.StringProperty(required=True,
               choices=('sans', 'serif', 'other'))
    width = db.FloatProperty(required=True)
    w_width = db.FloatProperty(required=True)
    x_height = db.FloatProperty(required=True)
    m_serif = db.FloatProperty(required=True)
    h_stem_horizontal_balance = db.FloatProperty(required=True)
    o_stroke_axis = db.FloatProperty(required=True)
    p_descender = db.FloatProperty(required=True)
    i_line_thickness = db.FloatProperty(required=True)
    design = db.StringProperty(required=True)
    # aggregation of width, x-height, descender
    distance_v = db.FloatProperty(required=True)
    # aggregation of m_serif, stem-horizontal, stroke axis, line thickness
    distance_h = db.FloatProperty(required=True)
    # sum of abs of  distance_v and distance_h
    distance = db.FloatProperty(required=True)
    lang = db.StringProperty(required=True)

    def get_position(cls):
        position_style = 'left: '+str(cls.distance_h*8+50)+'%;top :'+str(cls.distance_v*8+50)+'%'
        return position_style

    def get_svg(cls):
        svg = 'font_en'+cls.style+'.svg'
        return svg

    def get_num(cls):
        category = cls.category
        width = (cls.width + cls.w_width)/2
        x_height = cls.x_height
        m_serif = cls.m_serif
        h_stem_horizontal_balance = cls.h_stem_horizontal_balance
        o_stroke_axis = cls.o_stroke_axis
        p_descender  = cls.p_descender
        i_line_thickness = cls.i_line_thickness
        num1 = width
        num2 = x_height + p_descender
        num3 = h_stem_horizontal_balance
        num4 = o_stroke_axis+m_serif + m_serif*5
        num5 = i_line_thickness
        return category, num1, num2, num3, num4, num5 
