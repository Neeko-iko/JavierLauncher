# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'JavierUI.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QProgressBar, QPushButton, QScrollArea, QSizePolicy,
    QSpinBox, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.setEnabled(True)
        Main.resize(498, 716)
        Main.setMinimumSize(QSize(498, 615))
        Main.setMaximumSize(QSize(16777215, 16777215))
        Main.setAutoFillBackground(False)
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(500, 720))
        self.centralwidget.setMaximumSize(QSize(500, 720))
        self.Tabs = QTabWidget(self.centralwidget)
        self.Tabs.setObjectName(u"Tabs")
        self.Tabs.setEnabled(True)
        self.Tabs.setGeometry(QRect(0, 0, 501, 581))
        self.Tabs.setTabPosition(QTabWidget.North)
        self.Tabs.setTabShape(QTabWidget.Rounded)
        self.Tabs.setDocumentMode(True)
        self.Tabs.setMovable(False)
        self.Tabs.setTabBarAutoHide(False)
        self.launcherTab = QWidget()
        self.launcherTab.setObjectName(u"launcherTab")
        self.gridLayoutWidget = QWidget(self.launcherTab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 501, 551))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.searchBar = QLineEdit(self.gridLayoutWidget)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setMaximumSize(QSize(325, 30))
        self.searchBar.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.searchBar, 1, 0, 1, 1)

        self.setRamLabel = QLabel(self.gridLayoutWidget)
        self.setRamLabel.setObjectName(u"setRamLabel")
        self.setRamLabel.setScaledContents(False)
        self.setRamLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.setRamLabel.setOpenExternalLinks(False)

        self.gridLayout.addWidget(self.setRamLabel, 0, 1, 1, 1)

        self.ramEnter = QSpinBox(self.gridLayoutWidget)
        self.ramEnter.setObjectName(u"ramEnter")
        self.ramEnter.setMinimumSize(QSize(1, 30))
        self.ramEnter.setMaximumSize(QSize(60, 30))
        self.ramEnter.setCursor(QCursor(Qt.ArrowCursor))
        self.ramEnter.setWrapping(False)
        self.ramEnter.setFrame(True)
        self.ramEnter.setProperty("showGroupSeparator", False)
        self.ramEnter.setMinimum(1)
        self.ramEnter.setMaximum(99)
        self.ramEnter.setStepType(QAbstractSpinBox.DefaultStepType)
        self.ramEnter.setValue(1)
        self.ramEnter.setDisplayIntegerBase(10)

        self.gridLayout.addWidget(self.ramEnter, 1, 1, 1, 1)

        self.serverRefreshButton = QPushButton(self.gridLayoutWidget)
        self.serverRefreshButton.setObjectName(u"serverRefreshButton")
        self.serverRefreshButton.setMinimumSize(QSize(0, 34))
        self.serverRefreshButton.setMaximumSize(QSize(325, 30))
        self.serverRefreshButton.setCheckable(False)
        self.serverRefreshButton.setChecked(False)
        self.serverRefreshButton.setAutoDefault(False)
        self.serverRefreshButton.setFlat(False)

        self.gridLayout.addWidget(self.serverRefreshButton, 0, 0, 1, 1)

        self.buttonScroller = QScrollArea(self.gridLayoutWidget)
        self.buttonScroller.setObjectName(u"buttonScroller")
        self.buttonScroller.setMinimumSize(QSize(495, 0))
        self.buttonScroller.setMaximumSize(QSize(16777215, 16777215))
        self.buttonScroller.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.buttonScroller.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.buttonScroller.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 472, 469))
        self.buttonScroller.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.buttonScroller, 2, 0, 1, 3)

        self.startButton = QPushButton(self.gridLayoutWidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setMinimumSize(QSize(102, 70))
        self.startButton.setMaximumSize(QSize(93, 114))
        self.startButton.setFlat(False)

        self.gridLayout.addWidget(self.startButton, 0, 2, 2, 1)

        self.Tabs.addTab(self.launcherTab, "")
        self.settingsTab = QWidget()
        self.settingsTab.setObjectName(u"settingsTab")
        self.tabWidget = QTabWidget(self.settingsTab)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 495, 545))
        self.tabWidget.setFocusPolicy(Qt.NoFocus)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.normSettings = QWidget()
        self.normSettings.setObjectName(u"normSettings")
        self.verticalLayoutWidget = QWidget(self.normSettings)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 519, 191))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.addDirButton = QPushButton(self.verticalLayoutWidget)
        self.addDirButton.setObjectName(u"addDirButton")
        self.addDirButton.setMinimumSize(QSize(0, 40))
        self.addDirButton.setMaximumSize(QSize(495, 16777215))

        self.verticalLayout.addWidget(self.addDirButton)

        self.DirScoller = QScrollArea(self.verticalLayoutWidget)
        self.DirScoller.setObjectName(u"DirScoller")
        self.DirScoller.setMinimumSize(QSize(269, 0))
        self.DirScoller.setMaximumSize(QSize(495, 16777215))
        self.DirScoller.setFocusPolicy(Qt.NoFocus)
        self.DirScoller.setContextMenuPolicy(Qt.NoContextMenu)
        self.DirScoller.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.DirScoller.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DirScoller.setWidgetResizable(True)
        self.dirScrollerWidget = QWidget()
        self.dirScrollerWidget.setObjectName(u"dirScrollerWidget")
        self.dirScrollerWidget.setGeometry(QRect(0, 0, 470, 143))
        self.DirScoller.setWidget(self.dirScrollerWidget)

        self.verticalLayout.addWidget(self.DirScoller)

        self.themeScroller = QScrollArea(self.normSettings)
        self.themeScroller.setObjectName(u"themeScroller")
        self.themeScroller.setGeometry(QRect(0, 220, 171, 291))
        self.themeScroller.setFocusPolicy(Qt.NoFocus)
        self.themeScroller.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.themeScroller.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.themeScroller.setWidgetResizable(True)
        self.themeArea = QWidget()
        self.themeArea.setObjectName(u"themeArea")
        self.themeArea.setGeometry(QRect(0, 0, 146, 287))
        self.themeScroller.setWidget(self.themeArea)
        self.themeRefresh = QPushButton(self.normSettings)
        self.themeRefresh.setObjectName(u"themeRefresh")
        self.themeRefresh.setGeometry(QRect(0, 190, 171, 34))
        self.javaDownBar = QProgressBar(self.normSettings)
        self.javaDownBar.setObjectName(u"javaDownBar")
        self.javaDownBar.setEnabled(False)
        self.javaDownBar.setGeometry(QRect(170, 210, 131, 20))
        self.javaDownBar.setCursor(QCursor(Qt.BusyCursor))
        self.javaDownBar.setContextMenuPolicy(Qt.NoContextMenu)
        self.javaDownBar.setAutoFillBackground(False)
        self.javaDownBar.setMinimum(0)
        self.javaDownBar.setMaximum(1)
        self.javaDownBar.setValue(-1)
        self.javaDownBar.setTextVisible(False)
        self.javaDownBar.setOrientation(Qt.Horizontal)
        self.javaDownBar.setInvertedAppearance(False)
        self.javaIntBox = QSpinBox(self.normSettings)
        self.javaIntBox.setObjectName(u"javaIntBox")
        self.javaIntBox.setGeometry(QRect(270, 189, 31, 31))
        self.javaIntBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.javaIntBox.setMinimum(8)
        self.downJavaButton = QPushButton(self.normSettings)
        self.downJavaButton.setObjectName(u"downJavaButton")
        self.downJavaButton.setGeometry(QRect(170, 189, 131, 31))
        self.downJavaButton.setAutoFillBackground(False)
        self.downJavaButton.setAutoDefault(False)
        self.downJavaButton.setFlat(False)
        self.tabWidget.addTab(self.normSettings, "")
        self.verticalLayoutWidget.raise_()
        self.themeScroller.raise_()
        self.themeRefresh.raise_()
        self.javaDownBar.raise_()
        self.downJavaButton.raise_()
        self.javaIntBox.raise_()
        self.advancedSettings = QWidget()
        self.advancedSettings.setObjectName(u"advancedSettings")
        self.pushButton = QPushButton(self.advancedSettings)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 230, 221, 34))
        self.pushButton.setMinimumSize(QSize(169, 0))
        self.pushButton.setFlat(True)
        self.jarFileEntry = QLineEdit(self.advancedSettings)
        self.jarFileEntry.setObjectName(u"jarFileEntry")
        self.jarFileEntry.setGeometry(QRect(280, 430, 201, 32))
        self.jarFileEntry.setDragEnabled(True)
        self.defaultCheck = QCheckBox(self.advancedSettings)
        self.defaultCheck.setObjectName(u"defaultCheck")
        self.defaultCheck.setGeometry(QRect(200, 430, 81, 31))
        self.defaultCheck.setLayoutDirection(Qt.LeftToRight)
        self.defaultCheck.setChecked(True)
        self.sJavaOver = QLineEdit(self.advancedSettings)
        self.sJavaOver.setObjectName(u"sJavaOver")
        self.sJavaOver.setGeometry(QRect(0, 430, 191, 32))
        self.sJavaOver.setDragEnabled(True)
        self.jraEntry = QLineEdit(self.advancedSettings)
        self.jraEntry.setObjectName(u"jraEntry")
        self.jraEntry.setGeometry(QRect(0, 470, 481, 32))
        self.jraEntry.setMaxLength(32767)
        self.jraEntry.setDragEnabled(True)
        self.jraEntry.setClearButtonEnabled(False)
        self.serverSelectLabel = QLabel(self.advancedSettings)
        self.serverSelectLabel.setObjectName(u"serverSelectLabel")
        self.serverSelectLabel.setGeometry(QRect(0, 410, 481, 18))
        self.serverSelectLabel.setLayoutDirection(Qt.LeftToRight)
        self.serverSelectLabel.setTextFormat(Qt.PlainText)
        self.serverSelectLabel.setAlignment(Qt.AlignCenter)
        self.saveSettings = QPushButton(self.advancedSettings)
        self.saveSettings.setObjectName(u"saveSettings")
        self.saveSettings.setGeometry(QRect(0, 330, 181, 38))
        self.jarGuiCheck = QCheckBox(self.advancedSettings)
        self.jarGuiCheck.setObjectName(u"jarGuiCheck")
        self.jarGuiCheck.setGeometry(QRect(0, 370, 71, 22))
        self.jarGuiCheck.setFocusPolicy(Qt.ClickFocus)
        self.jarGuiCheck.setIconSize(QSize(16, 16))
        self.jarGuiCheck.setCheckable(True)
        self.jarGuiCheck.setTristate(False)
        self.safemodeCheck = QCheckBox(self.advancedSettings)
        self.safemodeCheck.setObjectName(u"safemodeCheck")
        self.safemodeCheck.setGeometry(QRect(90, 370, 88, 22))
        self.safemodeCheck.setFocusPolicy(Qt.ClickFocus)
        self.safemodeCheck.setCheckable(True)
        self.tabWidget.addTab(self.advancedSettings, "")
        self.Tabs.addTab(self.settingsTab, "")
        self.creatorTab = QWidget()
        self.creatorTab.setObjectName(u"creatorTab")
        self.plainTextEdit = QPlainTextEdit(self.creatorTab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(70, 100, 361, 291))
        self.plainTextEdit.setReadOnly(True)
        self.Tabs.addTab(self.creatorTab, "")
        self.helpTab = QWidget()
        self.helpTab.setObjectName(u"helpTab")
        self.textEdit = QTextEdit(self.helpTab)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 10, 471, 521))
        self.Tabs.addTab(self.helpTab, "")
        self.miniSole = QPlainTextEdit(self.centralwidget)
        self.miniSole.setObjectName(u"miniSole")
        self.miniSole.setGeometry(QRect(0, 580, 501, 141))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.miniSole.sizePolicy().hasHeightForWidth())
        self.miniSole.setSizePolicy(sizePolicy)
        self.miniSole.setMaximumSize(QSize(16777215, 192))
        self.miniSole.setMouseTracking(False)
        self.miniSole.setFocusPolicy(Qt.NoFocus)
        self.miniSole.setContextMenuPolicy(Qt.NoContextMenu)
        self.miniSole.setLineWidth(0)
        self.miniSole.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.miniSole.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.miniSole.setUndoRedoEnabled(False)
        self.miniSole.setReadOnly(True)
        self.logClearButton = QPushButton(self.centralwidget)
        self.logClearButton.setObjectName(u"logClearButton")
        self.logClearButton.setGeometry(QRect(380, 690, 101, 34))
        self.logClearButton.setFocusPolicy(Qt.NoFocus)
        self.logClearButton.setCheckable(False)
        self.logClearButton.setChecked(False)
        self.logClearButton.setFlat(True)
        self.updateCheckerButton = QPushButton(self.centralwidget)
        self.updateCheckerButton.setObjectName(u"updateCheckerButton")
        self.updateCheckerButton.setGeometry(QRect(370, 0, 131, 31))
        self.updateCheckerButton.setFocusPolicy(Qt.NoFocus)
        self.updateCheckerButton.setFlat(True)
        #Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        self.Tabs.setCurrentIndex(0)
        self.serverRefreshButton.setDefault(False)
        self.startButton.setDefault(False)
        self.tabWidget.setCurrentIndex(0)
        self.logClearButton.setDefault(False)


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
        self.setRamLabel.setText(QCoreApplication.translate("Main", u"Set RAM", None))
#if QT_CONFIG(tooltip)
        self.ramEnter.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>RAM to use for the server, in gigabytes.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ramEnter.setSuffix(QCoreApplication.translate("Main", u" GB", None))
#if QT_CONFIG(tooltip)
        self.serverRefreshButton.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>Refreshes the serverlist<br/>maybe Javier forgot something?</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.serverRefreshButton.setText(QCoreApplication.translate("Main", u"Refresh Server List / Search", None))
#if QT_CONFIG(tooltip)
        self.startButton.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>What it says on the tin.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.startButton.setText(QCoreApplication.translate("Main", u"Select a\n"
"Server!", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.launcherTab), QCoreApplication.translate("Main", u"Launcher", None))
#if QT_CONFIG(tooltip)
        self.Tabs.setTabToolTip(self.Tabs.indexOf(self.launcherTab), QCoreApplication.translate("Main", u"Where you launch your minecraft servers!", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.addDirButton.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>Adds a new directory for Javier to look through when searching for your servers to display in the Launch tab!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.addDirButton.setText(QCoreApplication.translate("Main", u"Add New Directory", None))
#if QT_CONFIG(tooltip)
        self.themeRefresh.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>Can't find your current theme?<br/>Themes are stored in Internals/themes</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.themeRefresh.setText(QCoreApplication.translate("Main", u"Refresh Theme Selector", None))
#if QT_CONFIG(tooltip)
        self.javaIntBox.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>this is the major java version number</p><p>generally 8 and 16 are used, but maybe you need something esle!<br/>8 is mainly for forge/older versions of MC<br/>and 16+ is for anything above 1.15</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.downJavaButton.setToolTip(QCoreApplication.translate("Main", u"download the java major version selected!", None))
#endif // QT_CONFIG(tooltip)
        self.downJavaButton.setText(QCoreApplication.translate("Main", u"Download Java        ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.normSettings), QCoreApplication.translate("Main", u"Javier Related", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("Main", u"the spooky secret button ooooooo", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("Main", u"quirky button lol but this time extra", None))
#if QT_CONFIG(tooltip)
        self.jarFileEntry.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>DEFAULT: EMPTY (JAVIER WILL FIND IT)</p><p>.jar file override should really only be used incase Javier manages to get the wrong server jar file for your server.</p><p>if you don't know what this means, don't worry about it!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.jarFileEntry.setText("")
        self.jarFileEntry.setPlaceholderText(QCoreApplication.translate("Main", u".jar file override", None))
#if QT_CONFIG(tooltip)
        self.defaultCheck.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>TEMPORARY</p><p>used for if you want your settings to be saved as the default, or if they're for the specific server</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.defaultCheck.setText(QCoreApplication.translate("Main", u"Default", None))
#if QT_CONFIG(tooltip)
        self.sJavaOver.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>DEFAULT: EMPTY (java)<br/>Java Runtime Binary is the filepath at which your java goes, this one is server specific- the Forge modloader on any MC version likes to use Java 8.</p><p>besides that you should be good with java 18 for all versions</p><p>if you don't know what any of this means, don't worry about it!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sJavaOver.setPlaceholderText(QCoreApplication.translate("Main", u"java binary runtime override", None))
#if QT_CONFIG(tooltip)
        self.jraEntry.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>DEFAULT: NONE<br/>Java Runtime Arguments, these can help your server run more efficiently </p><p>if you don't know what this means, don't worry about it!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.jraEntry.setPlaceholderText(QCoreApplication.translate("Main", u"Java Runtime Arguments", None))
#if QT_CONFIG(tooltip)
        self.serverSelectLabel.setToolTip(QCoreApplication.translate("Main", u"The server Selected", None))
#endif // QT_CONFIG(tooltip)
        self.serverSelectLabel.setText(QCoreApplication.translate("Main", u"No Server Selected!", None))
        self.saveSettings.setText(QCoreApplication.translate("Main", u"Save Settings", None))
#if QT_CONFIG(tooltip)
        self.jarGuiCheck.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>DEFAULT: OFF</p><p>Toggles the server .jar GUI</p><p>if you don't know what this means, leave it off</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.jarGuiCheck.setText(QCoreApplication.translate("Main", u"Jar GUI", None))
#if QT_CONFIG(tooltip)
        self.safemodeCheck.setToolTip(QCoreApplication.translate("Main", u"<html><head/><body><p>DEFAULT: OFF</p><p>Safemode will only run the vanilla jar without any datapacks if there are any.</p><p>mainly used for troubleshooting issues</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.safemodeCheck.setText(QCoreApplication.translate("Main", u"Safemode", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.advancedSettings), QCoreApplication.translate("Main", u"Server Related", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.settingsTab), QCoreApplication.translate("Main", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.Tabs.setTabToolTip(self.Tabs.indexOf(self.settingsTab), QCoreApplication.translate("Main", u"The Settings Page", None))
#endif // QT_CONFIG(tooltip)
        self.plainTextEdit.setPlainText(QCoreApplication.translate("Main", u"Hi Javier is unfinished \n"
"\n"
"this is the \"Creator\" Page!\n"
"it will be up and running or culled soon\n"
"\n"
"its purpose will be to assist you in making servers for you and your friends to enjoy! all from the comfort from Javiers admittedly mediocre design\n"
"", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.creatorTab), QCoreApplication.translate("Main", u"Creator", None))
#if QT_CONFIG(tooltip)
        self.Tabs.setTabToolTip(self.Tabs.indexOf(self.creatorTab), QCoreApplication.translate("Main", u"The Server Creator, where you make your servers", None))
#endif // QT_CONFIG(tooltip)
        self.Tabs.setTabText(self.Tabs.indexOf(self.helpTab), QCoreApplication.translate("Main", u"Help", None))
#if QT_CONFIG(tooltip)
        self.Tabs.setTabToolTip(self.Tabs.indexOf(self.helpTab), QCoreApplication.translate("Main", u"What do you expect this to mean?", None))
#endif // QT_CONFIG(tooltip)
        self.logClearButton.setText(QCoreApplication.translate("Main", u"Clear MiniSole", None))
        self.updateCheckerButton.setText(QCoreApplication.translate("Main", u"No Updates Found!", None))
    # retranslateUi

