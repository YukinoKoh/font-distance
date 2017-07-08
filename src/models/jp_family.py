from google.appengine.ext import db
from models import JpWeight


# Database
# font db
class JpFamily(db.Model):
    name = db.StringProperty(required=True)
    category = db.StringProperty(required=True,
               choices=('mincho', 'gothic', 'other'))
    width = db.FloatProperty(required=True)
    balance = db.FloatProperty(required=True)

    def get_all_weight(cls):
        family_name = cls.name.lower().replace(' ','_')
        weight_list = JpWeight.all().order("weight").filter('family = ', family_name)
        return weight_list

    def get_num(cls):
        category = cls.category
        width = cls.width
        balance = cls.balance
        return category, width, balance
