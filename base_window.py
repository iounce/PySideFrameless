# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt, QSize, QRect, Signal
from PySide6.QtWidgets import QDialog, QLabel, QWidget, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QLayout, QSpacerItem, QSizePolicy
from PySide6.QtGui import QCursor
from cursor import CursorDirection

from icon import MenuIcon, LogoIcon
from style import LabelStyle, WidgetStyle, ButtonStyle
#from ui_base import Ui_BaseWindow

import os

# show base information of the application
class BaseWindow(QDialog):
    base_signal = Signal(str)

    def __init__(self, parent=None, theme=None):
        super().__init__(parent)

        self.theme = theme

        self.is_moving = None
        self.start_point = None
        self.window_point = None
        self.cursor_direction = CursorDirection.Default
        self.left_btn_pressed = False
        self.drag_point = 0
        
        self.init_layout()
        self.init_app_bar()
        self.init_window()
        
        self.resize(600, 400)
        self.set_title('BaseWindow')
    
    # init window
    def init_window(self):
        self.setContentsMargins(8, 8, 8, 8)
        self.setStyleSheet(WidgetStyle.get_border('wid_main'))
        self.setMouseTracking(True)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        
    # init the window layout
    def init_layout(self):
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        
        self.layout_head = QHBoxLayout()
        self.layout_body = QVBoxLayout()
        self.layout_tail = QVBoxLayout()
        
        self.gridLayout.addLayout(self.layout_head, 0, 0, 1, 2)
        self.gridLayout.addLayout(self.layout_body, 1, 0, 1, 2)
        self.gridLayout.addLayout(self.layout_tail, 2, 0, 1, 2)

        #head
        self.layout_head.setSpacing(2)
        self.lbl_logo = QLabel(self)
        self.lbl_logo.setEnabled(True)
        self.lbl_logo.setMinimumSize(QSize(32, 32))
        self.lbl_logo.setMaximumSize(QSize(32, 32))
        self.layout_head.addWidget(self.lbl_logo)

        self.lbl_title = QLabel(self)
        self.lbl_title.setMinimumSize(QSize(200, 40))
        self.lbl_title.setMaximumSize(QSize(200, 40))
        self.layout_head.addWidget(self.lbl_title)

        self.spacer = QSpacerItem(32, 32, QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        self.layout_head.addItem(self.spacer)
        
        self.btn_min = QPushButton(self)
        self.btn_min.setMinimumSize(QSize(32, 32))
        self.btn_min.setMaximumSize(QSize(32, 32))
        self.layout_head.addWidget(self.btn_min)
        
        self.btn_max = QPushButton(self)
        self.btn_max.setMinimumSize(QSize(32, 32))
        self.btn_max.setMaximumSize(QSize(32, 32))
        self.layout_head.addWidget(self.btn_max)
        
        self.btn_restore = QPushButton(self)
        self.btn_restore.setMinimumSize(QSize(32, 32))
        self.btn_restore.setMaximumSize(QSize(32, 32))
        self.layout_head.addWidget(self.btn_restore)

        self.btn_close = QPushButton(self)
        self.btn_close.setMinimumSize(QSize(32, 32))
        self.btn_close.setMaximumSize(QSize(32, 32))
        self.layout_head.addWidget(self.btn_close)
              
        #body
        self.wid_body = QWidget()
        self.layout_body.addWidget(self.wid_body)
        
        #tail
        self.wid_tail = QWidget()
        self.wid_tail.setFixedHeight(20)
        self.layout_tail.addWidget(self.wid_tail)

    # init app bar
    def init_app_bar(self):
        self.lbl_logo.setMinimumSize(QSize(24, 24))
        self.lbl_logo.setMaximumSize(QSize(24, 24))
        self.lbl_logo.setPixmap(LogoIcon.get_pixmap())
        self.lbl_logo.setScaledContents(True)
        self.lbl_logo.setText('')
        self.lbl_title.setStyleSheet(LabelStyle.get_title())

        self.btn_max.setVisible(True)
        self.btn_restore.setVisible(False)
        
        self.btn_min.setFlat(True)
        self.btn_min.setIcon(MenuIcon.get_min())
        self.btn_min.setIconSize(QSize(24, 24))
        self.btn_min.clicked.connect(self.on_min)
        
        self.btn_max.setFlat(True)
        self.btn_max.setIcon(MenuIcon.get_max())
        self.btn_max.setIconSize(QSize(24, 24))
        self.btn_max.clicked.connect(self.on_max)
        
        self.btn_restore.setFlat(True)
        self.btn_restore.setIcon(MenuIcon.get_restore())
        self.btn_restore.setIconSize(QSize(24, 24))
        self.btn_restore.clicked.connect(self.on_restore)
        
        self.btn_close.setFlat(True)
        self.btn_close.setIcon(MenuIcon.get_close())
        self.btn_close.setIconSize(QSize(24, 24))
        self.btn_close.setText('')
        self.btn_close.setStyleSheet(ButtonStyle.get_close())
        self.btn_close.clicked.connect(self.on_exit)
        
    # set window title
    def set_title(self, title):
        self.lbl_title.setText(title)
        
    # add body layout
    def set_body_layout(self, layout):
        self.wid_body.setLayout(layout)
        
    # add tail layout
    def set_tail_layout(self, layout):
        self.wid_tail.setLayout(layout)
        
    # minimize the window
    def on_min(self):
        self.showMinimized()

    # maximize the window
    def on_max(self):
        self.btn_max.setVisible(False)
        self.btn_restore.setVisible(True)
        self.showMaximized()

    # restore the window
    def on_restore(self):
        self.btn_max.setVisible(True)
        self.btn_restore.setVisible(False)
        self.showNormal()

    # exit the window
    def on_exit(self):
        self.close()

    # get the cursor direction when dragging the mouse
    def get_cursor_direction(self, global_point):
        padding = 3
        
        rect = self.rect()
        top_left = self.mapToGlobal(rect.topLeft())
        bottom_right = self.mapToGlobal(rect.bottomRight())

        x = global_point.x()
        y = global_point.y()

        if top_left.x() + padding >= x >= top_left.x() and top_left.y() + padding >= y >= top_left.y():
            self.cursor_direction = CursorDirection.LeftTop
            self.setCursor(QCursor(Qt.SizeFDiagCursor))
        elif bottom_right.x() - padding <= x <= bottom_right.x() and bottom_right.y() - padding <= y <= bottom_right.y():
            self.cursor_direction = CursorDirection.RightBottom
            self.setCursor(QCursor(Qt.SizeFDiagCursor))
        elif top_left.x() + padding >= x >= top_left.x() and bottom_right.y() - padding <= y <= bottom_right.y():
            self.cursor_direction = CursorDirection.LeftBottom
            self.setCursor(QCursor(Qt.SizeBDiagCursor))
        elif bottom_right.x() >= x >= bottom_right.x() - padding and top_left.y() <= y <= top_left.y() + padding:
            self.cursor_direction = CursorDirection.RightTop
            self.setCursor(QCursor(Qt.SizeBDiagCursor))
        elif top_left.x() + padding >= x >= top_left.x():
            self.cursor_direction = CursorDirection.Left
            self.setCursor(QCursor(Qt.SizeHorCursor))
        elif bottom_right.x() >= x >= bottom_right.x() - padding:
            self.cursor_direction = CursorDirection.Right
            self.setCursor(QCursor(Qt.SizeHorCursor))
        elif top_left.y() <= y <= top_left.y() + padding:
            self.cursor_direction = CursorDirection.Up
            self.setCursor(QCursor(Qt.SizeVerCursor))
        elif bottom_right.y() >= y >= bottom_right.y() - padding:
            self.cursor_direction = CursorDirection.Down
            self.setCursor(QCursor(Qt.SizeVerCursor))
        else:
            self.cursor_direction = CursorDirection.Default
            self.setCursor(QCursor(Qt.ArrowCursor))

    # process mouse event when dragging the window
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_btn_pressed = True

            if self.cursor_direction != CursorDirection.Default:
                self.mouseGrabber()
            else:
                self.drag_point = e.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, e):
        global_point = e.globalPos()
        rect = self.rect()
        top_left = self.mapToGlobal(rect.topLeft())
        bottom_right = self.mapToGlobal(rect.bottomRight())

        if not self.left_btn_pressed:
            self.get_cursor_direction(global_point)
        else:
            if self.cursor_direction != CursorDirection.Default:
                move_rect = QRect(top_left, bottom_right)

                if self.cursor_direction == CursorDirection.Left:
                    if bottom_right.x() - global_point.x() <= self.minimumWidth():
                        move_rect.setX(top_left.x())
                    else:
                        move_rect.setX(global_point.x())
                elif self.cursor_direction == CursorDirection.Right:
                    move_rect.setWidth(global_point.x() - top_left.x())
                elif self.cursor_direction == CursorDirection.Up:
                    if bottom_right.y() - global_point.y() <= self.minimumHeight():
                        move_rect.setY(top_left.y())
                    else:
                        move_rect.setY(global_point.y())
                elif self.cursor_direction == CursorDirection.Down:
                    move_rect.setHeight(global_point.y() - top_left.y())
                elif self.cursor_direction == CursorDirection.LeftTop:
                    if bottom_right.x() - global_point.x() <= self.minimumWidth():
                        move_rect.setX(top_left.x())
                    else:
                        move_rect.setX(global_point.x())

                    if bottom_right.y() - global_point.y() <= self.minimumHeight():
                        move_rect.setY(top_left.y())
                    else:
                        move_rect.setY(global_point.y())
                elif self.cursor_direction == CursorDirection.RightTop:
                    move_rect.setWidth(global_point.x() - top_left.x())
                    move_rect.setY(global_point.y())
                elif self.cursor_direction == CursorDirection.LeftBottom:
                    move_rect.setX(global_point.x())
                    move_rect.setHeight(global_point.y() - top_left.y())
                elif self.cursor_direction == CursorDirection.RightBottom:
                    move_rect.setWidth(global_point.x() - top_left.x())
                    move_rect.setHeight(global_point.y() - top_left.y())
                else:
                    pass

                self.setGeometry(move_rect)
            else:
                self.move(e.globalPos() - self.drag_point)
                e.accept()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_btn_pressed = False

            if self.cursor_direction != CursorDirection.Default:
                self.releaseMouse()
                self.setCursor(QCursor(Qt.ArrowCursor))