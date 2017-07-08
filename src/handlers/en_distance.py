from handler import Handler
import settings
from models import EnFont
from en_center import insert_en


# page to layout all blogs
class EnDistance(Handler):
    def get(self):
        # insert font to en database
        insert_en()
        fonts = EnFont.all().order('name')
        self.render("main.html", fonts=fonts, sitename=settings.SITENAME)


    def post(self):
        keyname = self.request.get("font_selected")
        if EnFont.get_by_key_name(keyname):
            font_selected = EnFont.get_by_key_name(keyname)
        else:
            message = 'Something went wrong...'
            self.render_message(message, sitename=settings.SITENAME)

        fonts = EnFont.all().order('name')
        self.render("main.html", fonts=fonts, font_selected=font_selected,
                    sitename=settings.SITENAME)
