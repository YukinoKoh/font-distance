import settings
from handler import Handler


# page to layout all blogs
class About(Handler):
    def get(self):
        view = 'about'
        self.render("about.html", view=view, sitename=settings.SITENAME)

