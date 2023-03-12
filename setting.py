# -*- coding: utf-8 -*-

import enum
import json
import os

from language import Language, Locale
from theme import Theme
from utils import FileUtils, LanguageUtils, ThemeUtils

# settings(settings.json)
class Setting:
    def __init__(self):
        self.language = Language.Chinese.value
        self.theme = Theme.COMMON_DEFAULT

    def get_locale(self):
        if self.language == Language.English.value:
            return Locale.English
        else:
            return Locale.Chinese

    def get_language(self):
        return self.language

    def get_theme(self):
        return FileUtils.get_fullname(self.theme)

    def load(self):
        path = os.path.join(os.getcwd(), 'setting.json')
        if not os.path.exists(path):
            print('Setting: file does not exist(%s)' % path)
            return

        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            if len(content) == 0:
                return

            # noinspection PyBroadException
            try:
                setting = json.loads(content)
            except:
                setting = None

            if not setting:
                return

            if isinstance(setting, dict):
                language = setting.get('language')
                if LanguageUtils.validate(language):
                    self.language = language

                theme = setting.get('theme')
                if ThemeUtils.validate(theme):
                    self.theme = theme

    @staticmethod
    def save(language, theme):
        if not language or not theme:
            return

        path = os.path.join(os.getcwd(), 'setting.json')
        with open(path, 'w', encoding='utf-8') as f:
            setting = {'language': language, 'theme': theme}
            f.write(json.dumps(setting))