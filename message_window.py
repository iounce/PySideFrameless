# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QDialog

from ui_message import Ui_MessageWindow

from icon import MenuIcon, LogoIcon
from style import LabelStyle, WidgetStyle, ButtonStyle

# show messagebox
class MessageWindow(QDialog):
    def __init__(self, parent=None, theme=None, title=None, text=None):
        super().__init__(parent)

        self.theme = theme
        self.title = title
        self.text = text

        self.is_moving = None
        self.start_point = None
        self.window_point = None

        self.ui = Ui_MessageWindow()
        self.ui.setupUi(self)

        self.init_window()
        self.init_menu()
        self.init_content()

    def init_window(self):
        self.ui.lbl_logo.setMinimumSize(QSize(24, 24))
        self.ui.lbl_logo.setMaximumSize(QSize(24, 24))
        self.ui.lbl_logo.setPixmap(LogoIcon.get_pixmap())
        self.ui.lbl_logo.setScaledContents(True)
        self.ui.lbl_logo.setText('')
        self.ui.lbl_title.setStyleSheet(LabelStyle.get_title())
        self.ui.wid_main.setContentsMargins(16, 8, 4, 16)
        self.ui.wid_main.setStyleSheet(WidgetStyle.get_border('wid_main'))
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_ShowModal, True)

    def init_menu(self):
        self.ui.btn_close.setFlat(True)
        self.ui.btn_close.setIcon(MenuIcon.get_close())
        self.ui.btn_close.setIconSize(QSize(24, 24))
        self.ui.btn_close.setText('')
        self.ui.btn_close.setStyleSheet(ButtonStyle.get_close())
        self.ui.btn_close.clicked.connect(self.on_exit)
        self.ui.btn_ok.clicked.connect(self.on_ok)
        self.ui.btn_cancel.clicked.connect(self.on_cancel)

    def init_content(self):
        self.ui.lbl_text.setText(self.text)

    def on_exit(self):
        self.close()

    def on_ok(self):
        self.done(QDialog.DialogCode.Accepted)

    def on_cancel(self):
        self.done(QDialog.DialogCode.Rejected)

    # process mouse event when dragging the window
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.is_moving = True
            self.start_point = e.globalPosition().toPoint()
            self.window_point = self.frameGeometry().topLeft()

    def mouseMoveEvent(self, e):
        if self.is_moving:
            pos = e.globalPosition().toPoint() - self.start_point
            self.move(self.window_point + pos)

    def mouseReleaseEvent(self, e):
        self.is_moving = False