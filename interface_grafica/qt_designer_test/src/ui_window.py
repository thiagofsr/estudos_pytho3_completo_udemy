# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(656, 414)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_name = QLabel(self.centralwidget)
        self.lbl_name.setObjectName(u"lbl_name")
        font = QFont()
        font.setPointSize(20)
        self.lbl_name.setFont(font)

        self.gridLayout_2.addWidget(self.lbl_name, 1, 0, 1, 1)

        self.txb_name = QLineEdit(self.centralwidget)
        self.txb_name.setObjectName(u"txb_name")
        self.txb_name.setFont(font)

        self.gridLayout_2.addWidget(self.txb_name, 1, 1, 1, 1)

        self.btn_send = QPushButton(self.centralwidget)
        self.btn_send.setObjectName(u"btn_send")
        self.btn_send.setFont(font)

        self.gridLayout_2.addWidget(self.btn_send, 1, 2, 1, 1)

        self.lbl_results = QLabel(self.centralwidget)
        self.lbl_results.setObjectName(u"lbl_results")
        font1 = QFont()
        font1.setPointSize(60)
        self.lbl_results.setFont(font1)
        self.lbl_results.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_results, 0, 0, 1, 3)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 656, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_name.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.txb_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite algo", None))
        self.btn_send.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.lbl_results.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

