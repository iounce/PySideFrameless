# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication,QHBoxLayout,QLabel
from PySide6.QtCore import QTranslator

from icon import LogoIcon
from main_window import MainWindow
from setting import Setting
from theme import Theme
from base_window import BaseWindow

class MyWindow(BaseWindow):
    def __init__(self, parent=None, theme=None):
        super().__init__(parent, theme)

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

    #body
    layout_body = QHBoxLayout()
    label = QLabel("Hello")
    label.setStyleSheet("background-color:red")
    layout_body.addWidget(label)
    
    label = QLabel("World")
    label.setStyleSheet("background-color:blue")
    layout_body.addWidget(label)
    
    #tail
    layout_tail = QHBoxLayout()
    label2 = QLabel("tail")
    label2.setStyleSheet("background-color:yellow")
    layout_tail.addWidget(label2)
    
    theme = Theme(app, theme)
    
    window = MyWindow()
    window.setWindowIcon(LogoIcon.get_icon())
    window.set_body_layout(layout_body)
    window.set_tail_layout(layout_tail)
    window.show()

    sys.exit(app.exec())