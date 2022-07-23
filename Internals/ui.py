# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.setEnabled(True)
        Main.resize(500, 720)
        Main.setMinimumSize(QSize(500, 720))
        Main.setMaximumSize(QSize(500, 720))
        Main.setAutoFillBackground(False)
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(500, 720))
        self.centralwidget.setMaximumSize(QSize(500, 720))
        self.Tabs = QTabWidget(self.centralwidget)
        self.Tabs.setObjectName(u"Tabs")
        self.Tabs.setGeometry(QRect(0, 0, 501, 721))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget = QWidget(self.tab_3)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 491, 681))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 4)

        self.spinBox = QSpinBox(self.gridLayoutWidget)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout.addWidget(self.spinBox, 0, 3, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.listView = QListView(self.gridLayoutWidget)
        self.listView.setObjectName(u"listView")

        self.gridLayout.addWidget(self.listView, 1, 0, 1, 4)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 4)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.Tabs.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.Tabs.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.Tabs.addTab(self.tab_2, "")
        #Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        self.Tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Javier | MC Server Launcher", None))
        self.label.setText(QCoreApplication.translate("Main", u"Launch Arguments", None))
        self.pushButton.setText(QCoreApplication.translate("Main", u"Start Server ?", None))
        self.label_2.setText(QCoreApplication.translate("Main", u"  Enter Ram", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_3), QCoreApplication.translate("Main", u"Page", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab), QCoreApplication.translate("Main", u"Settings", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_2), QCoreApplication.translate("Main", u"Creator", None))
    # retranslateUi

