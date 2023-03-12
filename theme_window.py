# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtWidgets import QDialog, QLabel

from icon import MenuIcon, LogoIcon
from style import LabelStyle, WidgetStyle, ButtonStyle
from utils import FileUtils
from theme import Theme
from ui_theme import Ui_ThemeWindow

# theme window(qt-material library themes)
class ThemeWindow(QDialog):
    theme_signal = Signal(str)

    def __init__(self, parent=None, theme=None):
        super().__init__(parent)

        self.theme = theme

        self.is_moving = None
        self.start_point = None
        self.window_point = None

        self.ui = Ui_ThemeWindow()
        self.ui.setupUi(self)

        self.init_window()
        self.init_menu()
        self.init_themes()

    def init_window(self):
        self.ui.lbl_logo.setMinimumSize(QSize(24, 24))
        self.ui.lbl_logo.setMaximumSize(QSize(24, 24))
        self.ui.lbl_logo.setPixmap(LogoIcon.get_pixmap())
        self.ui.lbl_logo.setScaledContents(True)
        self.ui.lbl_logo.setText('')
        self.ui.lbl_title.setStyleSheet(LabelStyle.get_title())
        self.ui.wid_main.setContentsMargins(16, 0, 8, 16)
        self.ui.wid_main.setStyleSheet(WidgetStyle.get_border('wid_main'))
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)

    def init_menu(self):
        self.ui.btn_close.setFlat(True)
        self.ui.btn_close.setIcon(MenuIcon.get_close())
        self.ui.btn_close.setIconSize(QSize(24, 24))
        self.ui.btn_close.setText('')
        self.ui.btn_close.setStyleSheet(ButtonStyle.get_close())
        self.ui.btn_close.clicked.connect(self.on_exit)

    def init_themes(self):
        label = QLabel()
        label.setFixedHeight(40)
        label.setText(ThemeWindow.tr('info_default_theme'))
        label.setStyleSheet(LabelStyle.get_default())
        label.mousePressEvent = self.on_default_theme
        self.ui.layout_body.addWidget(label, 0, 0, 1, -1)

        row = 1
        column = 0
        column_count = 4

        themes = Theme.get_all_themes()
        for name in themes:
            theme = Theme.get_theme(name)

            name = FileUtils.get_name(name)
            label = QLabel()
            label.setMinimumSize(QSize(160, 32))
            label.setMaximumSize(QSize(160, 32))
            label.setText(name)
            label.setStyleSheet(LabelStyle.get_theme(theme['primaryColor']))
            label.mousePressEvent = self.on_change_theme

            self.ui.layout_body.addWidget(label, row, column)

            column += 1

            if column % column_count == 0:
                row += 1
                column = 0

    def on_exit(self):
        self.close()

    def on_default_theme(self, _):
        name = self.theme.get_default()
        self.theme.apply(name)

        self.theme_signal.emit(name)

    def on_change_theme(self, e):
        widget = self.childAt(e.scenePosition().toPoint())
        name = FileUtils.get_fullname(widget.text())
        self.theme.apply(name)

        self.theme_signal.emit(name)

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