from handler import Handler
import settings


class SetCookie(Handler):
    def get(self, lang, font, view):
        lang = str(lang)
        font = str(font)
        self.set_cookie('lang', lang)
        self.set_cookie('font', font)
        if view == 'sort':
            url = '/'+view
        else:
            url = '/'
        self.redirect(url)
