import settings
import util
from handler import Handler
from handler import select_font

# page to layout all blogs
class Typeset(Handler):
    @select_font
    def get(self):
        view = 'typeset'
        select_font = util.get_selected_font(self.jp, self.en)
        self.render("typeset.html", 
                    jp_font=select_font[0], en_font=select_font[1],
                    view=view, sitename=settings.SITENAME)


