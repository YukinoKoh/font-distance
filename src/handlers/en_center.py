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
    # google 
    name = 'Noto Sans'
    width = 65.0/72.0
    x_height = 54.0/72.0
    m_serif = 0.0
    h_stem_horizontal_balance = 9.0/10.0
    o_stroke_axis = 0.0
    p_decender = 24.0/72.0
    i_line_thickness = 10.1
    design = 'Google'
    insertEn(name, category, width, x_height, m_serif, h_stem_horizontal_balance, o_stroke_axis, p_decender, i_line_thickness, design)

    # typekit
    name = 'Eurostile'
    width = 61.0/68.0
    x_height = 48.0/68.0
    m_serif = 0.0
    h_stem_horizontal_balance = 7.0/8.0
    o_stroke_axis = 0.0
    p_decender = 20.0/68.0
    i_line_thickness = 8.0
    design = 'URW++'
    insertEn(name, category, width, x_height, m_serif, h_stem_horizontal_balance, o_stroke_axis, p_decender, i_line_thickness, design)

    name = 'Verdana'
    width = 67.0/74.0
    x_height = 55.0/74.0
    m_serif = 0.0
    h_stem_horizontal_balance = 8.0/10.0
    o_stroke_axis = 0.0
    p_decender = 20.0/74.0
    i_line_thickness = 10.0
    design = 'Matthew Carter, Microsoft'
    insertEn(name, category, width, x_height, m_serif, h_stem_horizontal_balance, o_stroke_axis, p_decender, i_line_thickness, design)

    category = 'serif'
    # google
    name = 'Noto Serif'
    width = 71.0/72.0
    x_height = 54.0/72.0
    m_serif = 9.0
    h_stem_horizontal_balance = 8.5/10.5
    o_stroke_axis = 0.0
    p_decender = 24.0/72.0
    i_line_thickness = 10.0
    design = 'Google'
    insertEn(name, category, width, x_height, m_serif, h_stem_horizontal_balance, o_stroke_axis, p_decender, i_line_thickness, design)

    # typekit
    name = 'Adobe Calson'
    width = 65.0/71.0
    x_height = 43.0/71.0
    m_serif = 12.0
    h_stem_horizontal_balance = 3.0/12.0
    o_stroke_axis = 3.9
    p_decender = 27.0/71.0
    i_line_thickness = 10.1
    design = 'Carol Twombly, Adobe'
    insertEn(name, category, width, x_height, m_serif, h_stem_horizontal_balance, o_stroke_axis, p_decender, i_line_thickness, design)

    name = 'Adobe Garamond'
    width = 68.0/67.0
    x_height = 40.0/67.0
    m_serif = 9.0
    h_stem_horizontal_balance = 4.0/9.0
    o_stroke_axis = 3.0
    p_decender = 26.0/67.0
    i_line_thickness = 9.0
    design = 'Robert Slimbach, Adobe'
    insertEn(name, category, width, x_height, m_serif, h_stem_horizontal_balance, o_stroke_axis, p_decender, i_line_thickness, design)

    name = 'Baskerville URW'
    width = 70.0/67.0
    x_height = 41.0/67.0
    m_serif = 11.5
    h_stem_horizontal_balance = 3.0/14.0
    o_stroke_axis = 1.2
    p_decender = 24.0/67.0
    i_line_thickness = 10.0
    design = 'URW++'
    insertEn(name, category, width, x_height, m_serif, h_stem_horizontal_balance, o_stroke_axis, p_decender, i_line_thickness, design)

    # common
    name = 'Courier New'
    width = 59.0/59.0
    x_height = 43.0/59.0
    m_serif = 7.0
    h_stem_horizontal_balance = 4.0/5.0
    o_stroke_axis = 0.0
    p_decender = 19.0/59.0
    i_line_thickness = 4.0
    design = 'Monotype'
    insertEn(name, category, width, x_height, m_serif, h_stem_horizontal_balance, o_stroke_axis, p_decender, i_line_thickness, design)

    name = 'Georgia'
    width = 72.0/70.0
    x_height = 49.0/70.0
    m_serif = 11.0
    h_stem_horizontal_balance = 4.0/11.0
    o_stroke_axis = 0.4
    p_decender = 21.0/70.0
    i_line_thickness = 11.0
    design = 'Matthew Carter, Tom Rickner, Microsoft'
    insertEn(name, category, width, x_height, m_serif, h_stem_horizontal_balance, o_stroke_axis, p_decender, i_line_thickness, design)

    name = 'Times New Roman'
    width = 72.0/68.0
    x_height = 45.0/68.0
    m_serif = 10.0
    h_stem_horizontal_balance = 4.0/10.0
    o_stroke_axis = 1.3
    p_decender = 21.0/68.0
    i_line_thickness = 10.0
    design = 'Monotype'
    insertEn(name, category, width, x_height, m_serif, h_stem_horizontal_balance, o_stroke_axis, p_decender, i_line_thickness, design)

def insertEn(name, category, width, x_height, m_serif, h_stem_horizontal_balance, o_stroke_axis, p_decender, i_line_thickness, design):
    key_name = name.lower().replace(' ', '_')
    if not EnFamily.get_by_key_name(name):
        style = key_name
        family_insert = EnFamily(key_name=key_name, name=name, style=style,
                                 category=category, width=width,
                                 x_height=x_height, m_serif=m_serif,
                                 h_stem_horizontal_balance=h_stem_horizontal_balance,
                                 o_stroke_axis=o_stroke_axis, p_decender=p_decender,
                                 i_line_thickness=i_line_thickness, design=design, distance_v=0.0,
                                 distance_h=0.0, distance=0.0, lang='en').put() 

