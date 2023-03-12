# -*- coding: utf-8 -*-

# widgets style using setStyleSheet
class LabelStyle:
    @staticmethod
    def get_title():
        return 'QLabel{font-size:16px; padding-left:8px}'

    @staticmethod
    def get_close():
        return 'QLabel:hover{background-color:red}'

    @staticmethod
    def get_default():
        return 'QLabel{padding-left:14px; border-radius:6px;border-width:1px;border-color:black;border-style: solid} QLabel:hover{border-width:2px;}'

    @staticmethod
    def get_theme(color):
        return 'QLabel{padding-left:10px; background-color: %s} QLabel:hover{border-width:1px; border-style: solid}' % color

class ButtonStyle:
    @staticmethod
    def get_close():
        return 'QPushButton:hover{background-color:red}'

    @staticmethod
    def get_more():
        return 'QPushButton::menu-indicator{width:0px}'

class MenuStyle:
    @staticmethod
    def get_more():
        return 'QMenu::item{height:20px; width:100px}'

class WidgetStyle:
    @staticmethod
    def get_border(name):
        return 'QWidget#%s{border:1px solid; border-color:#4f5b62}' % name