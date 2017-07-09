from handler import Handler
import settings


class SetCookie(Handler):
    def get(self, lang, font):
        lang = str(lang)
        font = str(font)
        self.set_cookie('lang', lang)
        self.set_cookie('font', font)
        url = '/'
        self.redirect(url)
