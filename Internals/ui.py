# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'JavierUI.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpinBox, QTabWidget,
    QWidget)

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
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 493, 681))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.startButton = QPushButton(self.gridLayoutWidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setMinimumSize(QSize(0, 70))

        self.gridLayout.addWidget(self.startButton, 0, 2, 2, 1)

        self.ramEnter = QSpinBox(self.gridLayoutWidget)
        self.ramEnter.setObjectName(u"ramEnter")
        self.ramEnter.setMinimumSize(QSize(1, 20))
        self.ramEnter.setCursor(QCursor(Qt.ArrowCursor))

        self.gridLayout.addWidget(self.ramEnter, 1, 1, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMaximumSize(QSize(16777215, 150))
        self.plainTextEdit.setMouseTracking(False)
        self.plainTextEdit.setFocusPolicy(Qt.NoFocus)
        self.plainTextEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.plainTextEdit.setLineWidth(0)
        self.plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout.addWidget(self.plainTextEdit, 4, 0, 1, 3)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.ButtonScroller = QScrollArea(self.gridLayoutWidget)
        self.ButtonScroller.setObjectName(u"ButtonScroller")
        self.ButtonScroller.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ButtonScroller.sizePolicy().hasHeightForWidth())
        self.ButtonScroller.setSizePolicy(sizePolicy1)
        self.ButtonScroller.setMinimumSize(QSize(491, 0))
        self.ButtonScroller.setFocusPolicy(Qt.NoFocus)
        self.ButtonScroller.setAutoFillBackground(False)
        self.ButtonScroller.setFrameShadow(QFrame.Sunken)
        self.ButtonScroller.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ButtonScroller.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ButtonScroller.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 461, 442))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy2)
        self.scrollAreaWidgetContents.setFocusPolicy(Qt.NoFocus)
        self.ButtonScroller.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.ButtonScroller, 2, 0, 1, 3)

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
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Main", u"Search", None))
        self.startButton.setText(QCoreApplication.translate("Main", u"Start Server ?", None))
        self.label_2.setText(QCoreApplication.translate("Main", u"set RAM", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_3), QCoreApplication.translate("Main", u"Page", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab), QCoreApplication.translate("Main", u"Settings", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_2), QCoreApplication.translate("Main", u"Creator", None))
    # retranslateUi

