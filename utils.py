# -*- coding: utf-8 -*-

import os
import time

from PySide6.QtGui import QColor

from language import Language
from theme import Theme

# helper
class StringUtils:
    @staticmethod
    def contains(string, substring):
        return string.find(substring) != -1

class FileUtils:
    @staticmethod
    def get_name(filename):
        return os.path.splitext(filename)[0]

    @staticmethod
    def get_fullname(name, ext = '.xml'):
        if ext in name:
            return name
        return name + ext

class DateUtils:
    @staticmethod
    def get_year():
        return time.strftime('%Y', time.localtime(time.time()))

    @staticmethod
    def get_date():
        return time.strftime('%Y-%m-%d',time.localtime(time.time()))

class ColorUtils:
    @staticmethod
    def hex2rgb(color):
        value = int(color[1:], 16)
        rgb_color = QColor(value)
        rgb_color = QColor(rgb_color.red(), rgb_color.green(), rgb_color.blue())
        return rgb_color.rgb()

class LanguageUtils:
    @staticmethod
    def validate(language):
        languages = [Language.Chinese.value, Language.English.value]
        return language in languages

class ThemeUtils:
    @staticmethod
    def validate(theme):
        theme = FileUtils.get_fullname(theme)
        return theme in Theme.get_all_themes()