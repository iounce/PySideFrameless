# -*- coding: utf-8 -*-

import os
from PySide6.QtGui import QColor
import qt_material

# themes of qt_material library
class Theme:
    COMMON_DEFAULT = 'dark_blue.xml'

    def __init__(self, app, theme_name):
        self.app = app
        self.theme = None
        self.theme_name = theme_name if theme_name else Theme.COMMON_DEFAULT

        self.apply(self.theme_name)

    @staticmethod
    def get_all_themes():
        return qt_material.list_themes()

    @staticmethod
    def get_theme(theme_name):
        theme = qt_material.get_theme(theme_name)
        return theme

    def get_theme_name(self):
        return os.path.splitext(self.theme_name)[0]

    def get_theme_fullname(self):
        return  self.theme_name

    @staticmethod
    def get_default():
        return Theme.COMMON_DEFAULT

    def apply(self, theme_name = COMMON_DEFAULT):
        invert_secondary = False if theme_name.find('dark') != -1 else True
        qt_material.apply_stylesheet(self.app, theme_name, invert_secondary=invert_secondary)
        self.theme = self.get_theme(theme_name)
        self.theme_name = theme_name

    def get_primary_color(self):
        return self.theme['primaryColor']

    def get_primary_light_color(self):
        return self.theme['primaryLightColor']

    def get_secondary_dark_color(self):
        return self.theme['secondaryDarkColor']

    def get_secondary_light_color(self):
        return self.theme['secondaryLightColor']

    def get_primary_text_color(self):
        return self.theme['primaryTextColor']

    def get_secondary_text_color(self):
        return self.theme['secondaryTextColor']

    def get_selected_color(self):
        rgb = int(self.get_primary_color()[1:], 16)
        rgb_color = QColor(rgb)
        color = QColor(rgb_color.red(), rgb_color.green(), rgb_color.blue())
        return color.rgb()

    def get_unselected_color(self):
        return self.get_secondary_dark_color()