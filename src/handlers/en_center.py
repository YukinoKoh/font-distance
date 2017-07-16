from models import EnFamily


def insert_en():
    # insert font db
    # width = x A width / A height
    # x height = x height / cap height
    # m serif = serif length of m 500% chrome screen - font-size 20px
    # h_stem_horizontal_balance = H horizontal height / H stem width
    # o_stroke_axis = angle 0 - vertical  
    # p_decender = p decender / caps height 
    # i_line_thickness: thickness of i 500% chrome screen - font-size 20px

    category = 'sans'

    name = 'Noto Sans'
    width = 65.0/72.0
    x_height = 53.0/72.0
    m_serif = 0.0
    h_stem_horizontal_balance = 9.0/10.0
    o_stroke_axis = 0.0
    p_decender = 21.0/72.0
    i_line_thickness = 10.1
    insertEn(name, category, width, x_height, m_serif, h_stem_horizontal_balance, o_stroke_axis, p_decender, i_line_thickness)

    category = 'serif'

    name = 'Adobe Garamond'
    width = 65.0/72.0
    x_height = 53.0/72.0
    m_serif = 0.0
    h_stem_horizontal_balance = 9.0/10.0
    o_stroke_axis = 0.0
    p_decender = 21.0/72.0
    i_line_thickness = 10.1
    insertEn(name, category, width, x_height, m_serif, h_stem_horizontal_balance, o_stroke_axis, p_decender, i_line_thickness)

def insertEn(name, category, width, x_height, m_serif, h_stem_horizontal_balance, o_stroke_axis, p_decender, i_line_thickness):
    key_name = name.lower().replace(' ', '_')
    if not EnFamily.get_by_key_name(name):
        style = key_name
        family_insert = EnFamily(key_name=key_name, name=name, style=style,
                                 category=category, width=width,
                                 x_height=x_height, m_serif=m_serif,
                                 h_stem_horizontal_balance=h_stem_horizontal_balance,
                                 o_stroke_axis=o_stroke_axis, p_decender=p_decender,
                                 i_line_thickness=i_line_thickness, distance_v=0.0,
                                 distance_h=0.0, distance=0.0, lang='en').put() 

