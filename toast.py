# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PySide6.QtCore import Qt, QSize

# show message and disappear automatically
class ToastWidget(QWidget):
    def __init__(self, parent, theme, text, interval=1500):
        super().__init__(parent)

        self.theme = theme
        self.base = 0
        self.timeout = 0
        self.current = 0
        self.timer_id = 0

        self.init_widget(text)
        self.init_timer(interval)

    def init_widget(self, text):
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setFixedHeight(48)

        layout = QHBoxLayout()

        label = QLabel(self)
        label.setText(text)
        label.setStyleSheet(
            'QLabel{margin-left:8px;margin-top:4px;margin-right:8px;padding-bottom:4px;background-color:%s;color:#f5f5f5}' %
            self.theme.get_primary_color())
        layout.addWidget(label)
        self.setStyleSheet('QWidget{background-color:%s;}' % self.theme.get_primary_color())

        self.setLayout(layout)

    def init_timer(self, interval):
        self.base = 500
        self.timeout = interval if interval and interval > self.base else self.base
        self.current = 0

        self.timer_id = self.startTimer(self.base)

    # window disappear then timeout
    def timerEvent(self, *args, **kwargs):
        self.current += self.base
        print('timer:', self.current, self.timeout)
        if self.current >= self.timeout:
            self.hide()
            self.killTimer(self.timer_id)
            self.close()