from handler import Handler
import settings


class SetCookie(Handler):
    def get(self, lang, font, view):
        lang = str(lang)
        font = str(font)
        self.set_cookie(lang, font)
        self.set_cookie('latest', lang)
        if view != 'distance':
            view = view.replace('-', '/')
            url = '/'+view
        else:
            url = '/'
        self.redirect(url)
