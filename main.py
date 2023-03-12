# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTranslator

from icon import LogoIcon
from main_window import MainWindow
from setting import Setting
from theme import Theme

# main entry point
if __name__ == "__main__":
    #load language and theme from settings
    setting = Setting()
    setting.load()

    locale = setting.get_locale()
    theme = setting.get_theme()

    print('main:', locale, theme)

    #set default language
    translator = QTranslator()
    translator.load(locale)

    app = QApplication(sys.argv)

    app.installTranslator(translator)

    #start main window
    window = MainWindow(Theme(app, theme), translator, setting)
    window.setWindowIcon(LogoIcon.get_icon())
    window.show()

    sys.exit(app.exec())