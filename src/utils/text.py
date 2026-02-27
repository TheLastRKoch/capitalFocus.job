import unicodedata


class TextUtils:

    def normalize_text(self, text):
        proceed_text = unicodedata.normalize('NFD', text)
        return ''.join(c for c in proceed_text
                       if unicodedata.category(c) != 'Mn')
