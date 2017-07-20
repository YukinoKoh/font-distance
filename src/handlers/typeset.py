import settings
import util
from handler import Handler
from handler import select_font

# page to layout all blogs
class Typeset(Handler):
    @select_font
    def get(self):
        en_font = util.get_font(self.en, 'en')
        jp_font = util.get_font(self.jp, 'jp')
        view = 'typeset'
        self.render("typeset.html", en_font=en_font, jp_font=jp_font,
                    view=view, sitename=settings.SITENAME)


