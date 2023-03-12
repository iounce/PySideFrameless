# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_theme.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_ThemeWindow(object):
    def setupUi(self, ThemeWindow):
        if not ThemeWindow.objectName():
            ThemeWindow.setObjectName(u"ThemeWindow")
        ThemeWindow.resize(724, 395)
        self.wid_main = QWidget(ThemeWindow)
        self.wid_main.setObjectName(u"wid_main")
        self.wid_main.setGeometry(QRect(0, 0, 721, 391))
        self.gridLayout = QGridLayout(self.wid_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.layout_head = QHBoxLayout()
        self.layout_head.setSpacing(2)
        self.layout_head.setObjectName(u"layout_head")
        self.layout_head.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.lbl_logo = QLabel(self.wid_main)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setEnabled(True)
        self.lbl_logo.setMinimumSize(QSize(32, 32))
        self.lbl_logo.setMaximumSize(QSize(32, 32))

        self.layout_head.addWidget(self.lbl_logo)

        self.lbl_title = QLabel(self.wid_main)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setMinimumSize(QSize(200, 40))
        self.lbl_title.setMaximumSize(QSize(200, 40))

        self.layout_head.addWidget(self.lbl_title)

        self.horizontalSpacer = QSpacerItem(80, 32, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_head.addItem(self.horizontalSpacer)

        self.btn_close = QPushButton(self.wid_main)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(32, 32))
        self.btn_close.setMaximumSize(QSize(32, 32))

        self.layout_head.addWidget(self.btn_close)


        self.gridLayout.addLayout(self.layout_head, 0, 0, 1, 2)

        self.layout_body = QGridLayout()
        self.layout_body.setObjectName(u"layout_body")

        self.gridLayout.addLayout(self.layout_body, 1, 0, 1, 2)


        self.retranslateUi(ThemeWindow)

        QMetaObject.connectSlotsByName(ThemeWindow)
    # setupUi

    def retranslateUi(self, ThemeWindow):
        ThemeWindow.setWindowTitle("")
        self.lbl_logo.setText("")
        self.lbl_title.setText(QCoreApplication.translate("ThemeWindow", u"title_this_window", None))
        self.btn_close.setText("")
    # retranslateUi

