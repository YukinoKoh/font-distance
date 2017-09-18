import settings
import util
from handler import Handler


# page to layout all blogs
class About(Handler):
    def get(self):
        view = 'about'
        select_font = util.get_selected_font(self.jp, self.en)
        self.render("about.html", view=view, sitename=settings.SITENAME, jp_font=select_font[0],
                    en_font=select_font[1])

