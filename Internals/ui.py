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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QFrame,
    QGridLayout, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpinBox, QTabWidget, QVBoxLayout, QWidget)

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
        self.Tabs.setGeometry(QRect(0, 0, 501, 581))
        self.Tabs.setTabPosition(QTabWidget.North)
        self.Tabs.setTabShape(QTabWidget.Rounded)
        self.Tabs.setMovable(False)
        self.Tabs.setTabBarAutoHide(False)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget = QWidget(self.tab_3)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 493, 551))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.searchBar = QLineEdit(self.gridLayoutWidget)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.searchBar, 1, 0, 1, 1)

        self.startButton = QPushButton(self.gridLayoutWidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setMinimumSize(QSize(97, 70))
        self.startButton.setMaximumSize(QSize(97, 70))
        self.startButton.setFlat(False)

        self.gridLayout.addWidget(self.startButton, 0, 2, 2, 1)

        self.ramEnter = QSpinBox(self.gridLayoutWidget)
        self.ramEnter.setObjectName(u"ramEnter")
        self.ramEnter.setMinimumSize(QSize(1, 20))
        self.ramEnter.setCursor(QCursor(Qt.ArrowCursor))
        self.ramEnter.setMinimum(1)
        self.ramEnter.setMaximum(99)
        self.ramEnter.setStepType(QAbstractSpinBox.DefaultStepType)
        self.ramEnter.setValue(1)
        self.ramEnter.setDisplayIntegerBase(10)

        self.gridLayout.addWidget(self.ramEnter, 1, 1, 1, 1)

        self.refreshButton = QPushButton(self.gridLayoutWidget)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setMinimumSize(QSize(0, 34))
        self.refreshButton.setCheckable(False)
        self.refreshButton.setChecked(False)
        self.refreshButton.setAutoDefault(False)
        self.refreshButton.setFlat(False)

        self.gridLayout.addWidget(self.refreshButton, 0, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_2.setOpenExternalLinks(False)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.ButtonScroller = QScrollArea(self.gridLayoutWidget)
        self.ButtonScroller.setObjectName(u"ButtonScroller")
        self.ButtonScroller.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonScroller.sizePolicy().hasHeightForWidth())
        self.ButtonScroller.setSizePolicy(sizePolicy)
        self.ButtonScroller.setMinimumSize(QSize(491, 0))
        self.ButtonScroller.setFocusPolicy(Qt.NoFocus)
        self.ButtonScroller.setAutoFillBackground(False)
        self.ButtonScroller.setFrameShadow(QFrame.Sunken)
        self.ButtonScroller.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ButtonScroller.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ButtonScroller.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 500, 425))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(469, 0))
        self.scrollAreaWidgetContents.setFocusPolicy(Qt.NoFocus)
        self.ButtonScroller.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.ButtonScroller, 2, 0, 1, 3)

        self.Tabs.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget = QTabWidget(self.tab)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 495, 545))
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tabWidget.setTabBarAutoHide(True)
        self.normSettings = QWidget()
        self.normSettings.setObjectName(u"normSettings")
        self.verticalLayoutWidget = QWidget(self.normSettings)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 20, 491, 171))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.addDirbutton = QPushButton(self.verticalLayoutWidget)
        self.addDirbutton.setObjectName(u"addDirbutton")
        self.addDirbutton.setMinimumSize(QSize(0, 35))

        self.verticalLayout.addWidget(self.addDirbutton)

        self.scrollArea = QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFocusPolicy(Qt.NoFocus)
        self.scrollArea.setContextMenuPolicy(Qt.NoContextMenu)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 464, 128))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.scrollArea)

        self.normallabel = QLabel(self.normSettings)
        self.normallabel.setObjectName(u"normallabel")
        self.normallabel.setGeometry(QRect(30, 0, 431, 20))
        self.normallabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.normallabel.setMargin(0)
        self.normallabel.setIndent(0)
        self.normallabel.setOpenExternalLinks(False)
        self.safemodecheck = QCheckBox(self.normSettings)
        self.safemodecheck.setObjectName(u"safemodecheck")
        self.safemodecheck.setGeometry(QRect(380, 200, 88, 22))
        self.safemodecheck.setFocusPolicy(Qt.ClickFocus)
        self.safemodecheck.setCheckable(True)
        self.jarguicheck = QCheckBox(self.normSettings)
        self.jarguicheck.setObjectName(u"jarguicheck")
        self.jarguicheck.setGeometry(QRect(390, 230, 71, 22))
        self.jarguicheck.setFocusPolicy(Qt.ClickFocus)
        self.jarguicheck.setIconSize(QSize(16, 16))
        self.jarguicheck.setCheckable(True)
        self.sJRA = QLineEdit(self.normSettings)
        self.sJRA.setObjectName(u"sJRA")
        self.sJRA.setGeometry(QRect(0, 470, 491, 32))
        self.sJRA.setMaxLength(32767)
        self.sJRA.setDragEnabled(True)
        self.sJRA.setClearButtonEnabled(False)
        self.sJavaOver = QLineEdit(self.normSettings)
        self.sJavaOver.setObjectName(u"sJavaOver")
        self.sJavaOver.setGeometry(QRect(0, 430, 191, 32))
        self.sJavaOver.setDragEnabled(True)
        self.jarFileOver = QLineEdit(self.normSettings)
        self.jarFileOver.setObjectName(u"jarFileOver")
        self.jarFileOver.setGeometry(QRect(290, 430, 201, 32))
        self.jarFileOver.setDragEnabled(True)
        self.tabWidget.addTab(self.normSettings, "")
        self.advancedSettings = QWidget()
        self.advancedSettings.setObjectName(u"advancedSettings")
        self.pushButton = QPushButton(self.advancedSettings)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 190, 169, 34))
        self.pushButton.setMinimumSize(QSize(169, 0))
        self.pushButton.setFlat(True)
        self.tabWidget.addTab(self.advancedSettings, "")
        self.Tabs.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.plainTextEdit = QPlainTextEdit(self.tab_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(60, 50, 361, 291))
        self.plainTextEdit.setReadOnly(True)
        self.Tabs.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.Tabs.addTab(self.tab_4, "")
        self.miniSole = QPlainTextEdit(self.centralwidget)
        self.miniSole.setObjectName(u"miniSole")
        self.miniSole.setGeometry(QRect(0, 580, 501, 141))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.miniSole.sizePolicy().hasHeightForWidth())
        self.miniSole.setSizePolicy(sizePolicy2)
        self.miniSole.setMaximumSize(QSize(16777215, 192))
        self.miniSole.setMouseTracking(False)
        self.miniSole.setFocusPolicy(Qt.NoFocus)
        self.miniSole.setContextMenuPolicy(Qt.NoContextMenu)
        self.miniSole.setLineWidth(0)
        self.miniSole.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.miniSole.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.miniSole.setUndoRedoEnabled(False)
        self.miniSole.setReadOnly(True)
        self.LogClearer = QPushButton(self.centralwidget)
        self.LogClearer.setObjectName(u"LogClearer")
        self.LogClearer.setGeometry(QRect(380, 690, 101, 34))
        self.LogClearer.setFocusPolicy(Qt.NoFocus)
        self.LogClearer.setFlat(True)

        self.retranslateUi(Main)

        self.Tabs.setCurrentIndex(0)
        self.startButton.setDefault(False)
        self.refreshButton.setDefault(False)
        self.tabWidget.setCurrentIndex(0)
        self.LogClearer.setDefault(False)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Javier | MC Server Launcher", None))
#if QT_CONFIG(tooltip)
        self.searchBar.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>Search/Filter through your servers so that you can find the perfect server even faster!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.searchBar.setInputMask("")
        self.searchBar.setText("")
        self.searchBar.setPlaceholderText(QCoreApplication.translate("Main", u"Query", None))
#if QT_CONFIG(tooltip)
        self.startButton.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>What it says on the tin.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.startButton.setText(QCoreApplication.translate("Main", u"Select a Server", None))
#if QT_CONFIG(tooltip)
        self.ramEnter.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>RAM to use for the server, in gigabytes.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ramEnter.setSuffix(QCoreApplication.translate("Main", u" Gb", None))
#if QT_CONFIG(tooltip)
        self.refreshButton.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>Refreshes the serverlist<br/>maybe Javier forgot something?</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.refreshButton.setText(QCoreApplication.translate("Main", u"Refresh Server List / Search", None))
        self.label_2.setText(QCoreApplication.translate("Main", u"Set RAM", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_3), QCoreApplication.translate("Main", u"Launcher", None))
#if QT_CONFIG(tooltip)
        self.Tabs.setTabToolTip(self.Tabs.indexOf(self.tab_3), QCoreApplication.translate("Main", u"Where you launch your minecraft servers!", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.addDirbutton.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>Adds a new directory for Javier to look through when searching for your servers to display in the Launch tab!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.addDirbutton.setText(QCoreApplication.translate("Main", u"Add New Directory", None))
        self.normallabel.setText(QCoreApplication.translate("Main", u"Normal Settings", None))
#if QT_CONFIG(tooltip)
        self.safemodecheck.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>DEFAULT: OFF</p><p>Safemode will only run the vanilla jar without any datapacks if there are any.</p><p>mainly used for troubleshooting issues</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.safemodecheck.setText(QCoreApplication.translate("Main", u"Safemode", None))
#if QT_CONFIG(tooltip)
        self.jarguicheck.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>DEFAULT: OFF</p><p>Toggles the server .jar GUI</p><p>if you don't know what this means, leave it off</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.jarguicheck.setText(QCoreApplication.translate("Main", u"Jar GUI", None))
#if QT_CONFIG(tooltip)
        self.sJRA.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>DEFAULT: NONE<br/>Java Runtime Arguments, these can help your server run more efficiently </p><p>if you don't know what this means, don't worry about it!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sJRA.setPlaceholderText(QCoreApplication.translate("Main", u"Java Runtime Arguments", None))
#if QT_CONFIG(tooltip)
        self.sJavaOver.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>DEFAULT: EMPTY (java)<br/>Java Runtime Binary is the filepath at which your java goes, this one is server specific- the Forge modloader on any MC version likes to use Java 8.</p><p>besides that you should be good with java 18 for all versions</p><p>if you don't know what any of this means, don't worry about it!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sJavaOver.setPlaceholderText(QCoreApplication.translate("Main", u"java binary runtime override", None))
#if QT_CONFIG(tooltip)
        self.jarFileOver.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>DEFAULT: EMPTY (JAVIER WILL FIND IT)</p><p>.jar file override should really only be used incase Javier manages to get the wrong server jar file for your server.</p><p>if you don't know what this means, don't worry about it!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.jarFileOver.setText("")
        self.jarFileOver.setPlaceholderText(QCoreApplication.translate("Main", u".jar file override", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.normSettings), QCoreApplication.translate("Main", u"Normal Settings", None))
        self.pushButton.setText(QCoreApplication.translate("Main", u"quirky button lol", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.advancedSettings), QCoreApplication.translate("Main", u"Advanced Settings", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab), QCoreApplication.translate("Main", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.Tabs.setTabToolTip(self.Tabs.indexOf(self.tab), QCoreApplication.translate("Main", u"The Settings Page", None))
#endif // QT_CONFIG(tooltip)
        self.plainTextEdit.setPlainText(QCoreApplication.translate("Main", u"Hi Javier is unfinished \n"
"\n"
"this is the \"Creator\" Page!\n"
"it will be up and running or culled soon\n"
"\n"
"its purpose will be to assist you in making servers for you and your friends to enjoy! all from the comfort from Javiers admittedly mediocre design\n"
"", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_2), QCoreApplication.translate("Main", u"Creator", None))
#if QT_CONFIG(tooltip)
        self.Tabs.setTabToolTip(self.Tabs.indexOf(self.tab_2), QCoreApplication.translate("Main", u"The Server Creator, where you make your servers", None))
#endif // QT_CONFIG(tooltip)
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_4), QCoreApplication.translate("Main", u"Help", None))
#if QT_CONFIG(tooltip)
        self.Tabs.setTabToolTip(self.Tabs.indexOf(self.tab_4), QCoreApplication.translate("Main", u"What do you expect this to mean?", None))
#endif // QT_CONFIG(tooltip)
        self.LogClearer.setText(QCoreApplication.translate("Main", u"Clear MiniSole", None))
    # retranslateUi

