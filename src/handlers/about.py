import settings
from handler import Handler


# page to layout all blogs
class About(Handler):
    def get(self):
        self.render("about.html", sitename=settings.SITENAME)

