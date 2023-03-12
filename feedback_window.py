# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtWidgets import QDialog, QLabel
from PySide6.QtGui import QGuiApplication

from icon import MenuIcon, LogoIcon
from style import LabelStyle, WidgetStyle, ButtonStyle
from ui_feedback import Ui_FeedbackWindow

import os

# show feedback information of the application
class FeedbackWindow(QDialog):
    theme_signal = Signal(str)

    def __init__(self, parent=None, theme=None):
        super().__init__(parent)

        self.theme = theme
        self.clipboard = QGuiApplication.clipboard()

        self.is_moving = None
        self.start_point = None
        self.window_point = None

        self.ui = Ui_FeedbackWindow()
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

    def init_menu(self):
        self.ui.btn_close.setFlat(True)
        self.ui.btn_close.setIcon(MenuIcon.get_close())
        self.ui.btn_close.setIconSize(QSize(24, 24))
        self.ui.btn_close.setText('')
        self.ui.btn_close.setStyleSheet(ButtonStyle.get_close())
        self.ui.btn_close.clicked.connect(self.on_exit)

    def init_content(self):
        self.ui.layout_body.setAlignment(Qt.AlignCenter)
        self.ui.layout_body.addStretch()

        for i in range(4):
            label = QLabel()
            label.setFixedHeight(6)
            self.ui.layout_body.addWidget(label, 1)

        label = QLabel()
        label.setText(FeedbackWindow.tr('info_qq'))
        label.setToolTip(FeedbackWindow.tr('tip_copy_data'))
        label.setStyleSheet('font-size: 16px')
        label.mousePressEvent = self.on_copy_data
        self.ui.layout_body.addWidget(label, 1)

        label = QLabel()
        label.setText(FeedbackWindow.tr('info_email'))
        label.setToolTip(FeedbackWindow.tr('tip_copy_data'))
        label.setStyleSheet('font-size: 16px')
        label.mousePressEvent = self.on_copy_data
        self.ui.layout_body.addWidget(label, 1)

        for i in range(4):
            label = QLabel()
            label.setFixedHeight(6)
            self.ui.layout_body.addWidget(label, 1)

    @staticmethod
    def get_license_folder():
        return os.path.join(os.getcwd(), "license")

    def on_exit(self):
        self.close()

    # set clipboard text
    def on_copy_data(self, e):
        if e.button() == Qt.LeftButton:
            widget = self.childAt(e.scenePosition().toPoint())
            text = widget.text()
            data = text.split(':')[1]
            self.clipboard.setText(data.strip())

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