from handler import Handler
import settings


class SetCookie(Handler):
    def get(self, lang, font_style):
        lang = str(lang)
        font = str(font_style)
        self.set_cookie(lang, font)
        url = '/jpsort'
        self.redirect(url)
