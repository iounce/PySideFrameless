# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(958, 600)
        self.wid_main = QWidget(MainWindow)
        self.wid_main.setObjectName(u"wid_main")
        self.wid_main.setMouseTracking(True)
        self.gridLayout = QGridLayout(self.wid_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.layout_body = QHBoxLayout()
        self.layout_body.setObjectName(u"layout_body")
        self.widget_2 = QWidget(self.wid_main)
        self.widget_2.setObjectName(u"widget_2")

        self.layout_body.addWidget(self.widget_2)


        self.gridLayout.addLayout(self.layout_body, 1, 0, 1, 2)

        self.layout_foot = QHBoxLayout()
        self.layout_foot.setObjectName(u"layout_foot")
        self.widget = QWidget(self.wid_main)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 33))
        self.widget.setMaximumSize(QSize(16777215, 32))

        self.layout_foot.addWidget(self.widget)


        self.gridLayout.addLayout(self.layout_foot, 2, 0, 1, 2)

        self.layout_head = QHBoxLayout()
        self.layout_head.setSpacing(2)
        self.layout_head.setObjectName(u"layout_head")
        self.layout_head.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.lbl_logo = QLabel(self.wid_main)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setEnabled(True)
        self.lbl_logo.setMinimumSize(QSize(32, 32))
        self.lbl_logo.setMaximumSize(QSize(32, 32))
        self.lbl_logo.setMouseTracking(True)

        self.layout_head.addWidget(self.lbl_logo)

        self.lbl_title = QLabel(self.wid_main)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setMinimumSize(QSize(200, 40))
        self.lbl_title.setMaximumSize(QSize(200, 40))
        self.lbl_title.setMouseTracking(True)

        self.layout_head.addWidget(self.lbl_title)

        self.horizontalSpacer = QSpacerItem(80, 32, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_head.addItem(self.horizontalSpacer)

        self.btn_more = QPushButton(self.wid_main)
        self.btn_more.setObjectName(u"btn_more")
        self.btn_more.setMinimumSize(QSize(32, 32))
        self.btn_more.setMaximumSize(QSize(32, 32))

        self.layout_head.addWidget(self.btn_more)

        self.btn_min = QPushButton(self.wid_main)
        self.btn_min.setObjectName(u"btn_min")
        self.btn_min.setMinimumSize(QSize(32, 32))
        self.btn_min.setMaximumSize(QSize(32, 32))

        self.layout_head.addWidget(self.btn_min)

        self.btn_max = QPushButton(self.wid_main)
        self.btn_max.setObjectName(u"btn_max")
        self.btn_max.setMinimumSize(QSize(32, 32))
        self.btn_max.setMaximumSize(QSize(32, 32))

        self.layout_head.addWidget(self.btn_max)

        self.btn_restore = QPushButton(self.wid_main)
        self.btn_restore.setObjectName(u"btn_restore")
        self.btn_restore.setMinimumSize(QSize(32, 32))
        self.btn_restore.setMaximumSize(QSize(32, 32))

        self.layout_head.addWidget(self.btn_restore)

        self.btn_close = QPushButton(self.wid_main)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(32, 32))
        self.btn_close.setMaximumSize(QSize(32, 32))

        self.layout_head.addWidget(self.btn_close)


        self.gridLayout.addLayout(self.layout_head, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.wid_main)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_logo.setText("")
        self.lbl_title.setText(QCoreApplication.translate("MainWindow", u"title_this_app", None))
        self.btn_more.setText("")
        self.btn_min.setText("")
        self.btn_max.setText("")
        self.btn_restore.setText("")
        self.btn_close.setText("")
    # retranslateUi

