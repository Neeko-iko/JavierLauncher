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
    QSize)
from PySide6.QtWidgets import (QApplication, QFormLayout, QMainWindow, QSizePolicy,
    QTabWidget, QWidget)

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
        self.Launcher = QWidget()
        self.Launcher.setObjectName(u"Launcher")
        self.formLayout = QFormLayout(self.Launcher)
        self.formLayout.setObjectName(u"formLayout")
        self.Tabs.addTab(self.Launcher, "")
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
        self.Tabs.setTabText(self.Tabs.indexOf(self.Launcher), QCoreApplication.translate("Main", u"Launcher", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab), QCoreApplication.translate("Main", u"Settings", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_2), QCoreApplication.translate("Main", u"Creator", None))
    # retranslateUi

