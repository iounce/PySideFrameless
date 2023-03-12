# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_message.ui'
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
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MessageWindow(object):
    def setupUi(self, MessageWindow):
        if not MessageWindow.objectName():
            MessageWindow.setObjectName(u"MessageWindow")
        MessageWindow.resize(443, 213)
        self.wid_main = QWidget(MessageWindow)
        self.wid_main.setObjectName(u"wid_main")
        self.wid_main.setGeometry(QRect(0, 0, 441, 211))
        self.gridLayout = QGridLayout(self.wid_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.layout_body = QVBoxLayout()
        self.layout_body.setObjectName(u"layout_body")
        self.layout_text = QHBoxLayout()
        self.layout_text.setObjectName(u"layout_text")
        self.widget_2 = QWidget(self.wid_main)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(16, 0))
        self.widget_2.setMaximumSize(QSize(16, 16777215))

        self.layout_text.addWidget(self.widget_2)

        self.lbl_text = QLabel(self.wid_main)
        self.lbl_text.setObjectName(u"lbl_text")

        self.layout_text.addWidget(self.lbl_text)

        self.widget_3 = QWidget(self.wid_main)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(16, 0))
        self.widget_3.setMaximumSize(QSize(16, 16777215))

        self.layout_text.addWidget(self.widget_3)


        self.layout_body.addLayout(self.layout_text)

        self.layout_btn = QHBoxLayout()
        self.layout_btn.setObjectName(u"layout_btn")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_btn.addItem(self.horizontalSpacer_2)

        self.btn_ok = QPushButton(self.wid_main)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setMinimumSize(QSize(90, 30))
        self.btn_ok.setMaximumSize(QSize(90, 30))

        self.layout_btn.addWidget(self.btn_ok)

        self.widget = QWidget(self.wid_main)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(32, 0))

        self.layout_btn.addWidget(self.widget)

        self.btn_cancel = QPushButton(self.wid_main)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMinimumSize(QSize(90, 30))
        self.btn_cancel.setMaximumSize(QSize(90, 30))

        self.layout_btn.addWidget(self.btn_cancel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_btn.addItem(self.horizontalSpacer_3)


        self.layout_body.addLayout(self.layout_btn)


        self.gridLayout.addLayout(self.layout_body, 1, 0, 1, 2)

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
        self.lbl_title.setMinimumSize(QSize(80, 40))
        self.lbl_title.setMaximumSize(QSize(80, 40))

        self.layout_head.addWidget(self.lbl_title)

        self.horizontalSpacer = QSpacerItem(32, 32, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_head.addItem(self.horizontalSpacer)

        self.btn_close = QPushButton(self.wid_main)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(32, 32))
        self.btn_close.setMaximumSize(QSize(32, 32))

        self.layout_head.addWidget(self.btn_close)


        self.gridLayout.addLayout(self.layout_head, 0, 0, 1, 1)


        self.retranslateUi(MessageWindow)

        QMetaObject.connectSlotsByName(MessageWindow)
    # setupUi

    def retranslateUi(self, MessageWindow):
        MessageWindow.setWindowTitle("")
        self.lbl_text.setText(QCoreApplication.translate("MessageWindow", u"title_text", None))
        self.btn_ok.setText(QCoreApplication.translate("MessageWindow", u"title_ok", None))
        self.btn_cancel.setText(QCoreApplication.translate("MessageWindow", u"title_cancel", None))
        self.lbl_logo.setText("")
        self.lbl_title.setText(QCoreApplication.translate("MessageWindow", u"title_this_window", None))
        self.btn_close.setText("")
    # retranslateUi

