# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'JavierUI.ui'
##
# Created by: Qt User Interface Compiler version 6.4.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
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
                               QPlainTextEdit, QProgressBar, QPushButton, QScrollArea,
                               QSizePolicy, QSpinBox, QTabWidget, QTextBrowser,
                               QTextEdit, QVBoxLayout, QWidget)


class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.setEnabled(True)
        Main.resize(500, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main.sizePolicy().hasHeightForWidth())
        Main.setSizePolicy(sizePolicy)
        Main.setMinimumSize(QSize(500, 720))
        Main.setMaximumSize(QSize(500, 720))
        Main.setAutoFillBackground(False)
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
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
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 502, 551))
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
        self.setRamLabel.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
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
        self.buttonScroller.setMinimumSize(QSize(500, 0))
        self.buttonScroller.setMaximumSize(QSize(16777215, 16777215))
        self.buttonScroller.setFrameShadow(QFrame.Sunken)
        self.buttonScroller.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.buttonScroller.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.buttonScroller.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
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
        self.settingtabs = QTabWidget(self.settingsTab)
        self.settingtabs.setObjectName(u"settingtabs")
        self.settingtabs.setGeometry(QRect(0, 0, 501, 551))
        self.settingtabs.setFocusPolicy(Qt.NoFocus)
        self.settingtabs.setLayoutDirection(Qt.LeftToRight)
        self.settingtabs.setAutoFillBackground(False)
        self.settingtabs.setTabPosition(QTabWidget.South)
        self.settingtabs.setDocumentMode(True)
        self.settingtabs.setTabsClosable(False)
        self.settingtabs.setTabBarAutoHide(True)
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
        self.settingtabs.addTab(self.normSettings, "")
        self.verticalLayoutWidget.raise_()
        self.themeScroller.raise_()
        self.themeRefresh.raise_()
        self.javaDownBar.raise_()
        self.downJavaButton.raise_()
        self.javaIntBox.raise_()
        self.advancedSettings = QWidget()
        self.advancedSettings.setObjectName(u"advancedSettings")
        self.jarFileEntry = QLineEdit(self.advancedSettings)
        self.jarFileEntry.setObjectName(u"jarFileEntry")
        self.jarFileEntry.setGeometry(QRect(0, 430, 201, 32))
        self.jarFileEntry.setDragEnabled(True)
        self.defaultCheck = QCheckBox(self.advancedSettings)
        self.defaultCheck.setObjectName(u"defaultCheck")
        self.defaultCheck.setGeometry(QRect(200, 430, 81, 31))
        self.defaultCheck.setLayoutDirection(Qt.LeftToRight)
        self.defaultCheck.setChecked(True)
        self.sJavaOver = QLineEdit(self.advancedSettings)
        self.sJavaOver.setObjectName(u"sJavaOver")
        self.sJavaOver.setGeometry(QRect(290, 430, 191, 32))
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
        self.saveSettings.setGeometry(QRect(0, 350, 251, 38))
        self.jarGuiCheck = QCheckBox(self.advancedSettings)
        self.jarGuiCheck.setObjectName(u"jarGuiCheck")
        self.jarGuiCheck.setGeometry(QRect(0, 390, 71, 22))
        self.jarGuiCheck.setFocusPolicy(Qt.ClickFocus)
        self.jarGuiCheck.setIconSize(QSize(16, 16))
        self.jarGuiCheck.setCheckable(True)
        self.jarGuiCheck.setTristate(False)
        self.safemodeCheck = QCheckBox(self.advancedSettings)
        self.safemodeCheck.setObjectName(u"safemodeCheck")
        self.safemodeCheck.setGeometry(QRect(170, 390, 81, 22))
        self.safemodeCheck.setFocusPolicy(Qt.ClickFocus)
        self.safemodeCheck.setCheckable(True)
        self.javaScroller = QScrollArea(self.advancedSettings)
        self.javaScroller.setObjectName(u"javaScroller")
        self.javaScroller.setGeometry(QRect(310, 100, 171, 291))
        self.javaScroller.setFocusPolicy(Qt.NoFocus)
        self.javaScroller.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.javaScroller.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.javaScroller.setWidgetResizable(True)
        self.javaArea = QWidget()
        self.javaArea.setObjectName(u"javaArea")
        self.javaArea.setGeometry(QRect(0, 0, 146, 287))
        self.javaScroller.setWidget(self.javaArea)
        self.javaRefresh = QPushButton(self.advancedSettings)
        self.javaRefresh.setObjectName(u"javaRefresh")
        self.javaRefresh.setGeometry(QRect(310, 70, 171, 34))
        self.proplabel = QLabel(self.advancedSettings)
        self.proplabel.setObjectName(u"proplabel")
        self.proplabel.setGeometry(QRect(0, 30, 101, 18))
        self.propBrowser = QTextBrowser(self.advancedSettings)
        self.propBrowser.setObjectName(u"propBrowser")
        self.propBrowser.setGeometry(QRect(0, 50, 251, 301))
        font = QFont()
        font.setPointSize(13)
        self.propBrowser.setFont(font)
        self.propBrowser.setUndoRedoEnabled(True)
        self.propBrowser.setLineWrapMode(QTextEdit.NoWrap)
        self.propBrowser.setReadOnly(False)
        self.propBrowser.setOverwriteMode(False)
        self.propBrowser.setAcceptRichText(False)
        self.propBrowser.setOpenLinks(False)
        self.settingtabs.addTab(self.advancedSettings, "")
        self.propBrowser.raise_()
        self.jarFileEntry.raise_()
        self.defaultCheck.raise_()
        self.sJavaOver.raise_()
        self.jraEntry.raise_()
        self.serverSelectLabel.raise_()
        self.saveSettings.raise_()
        self.jarGuiCheck.raise_()
        self.safemodeCheck.raise_()
        self.javaScroller.raise_()
        self.javaRefresh.raise_()
        self.proplabel.raise_()
        self.Tabs.addTab(self.settingsTab, "")
        self.creatorTab = QWidget()
        self.creatorTab.setObjectName(u"creatorTab")
        self.createtabs = QTabWidget(self.creatorTab)
        self.createtabs.setObjectName(u"createtabs")
        self.createtabs.setEnabled(True)
        self.createtabs.setGeometry(QRect(0, 0, 501, 551))
        self.createtabs.setTabPosition(QTabWidget.South)
        self.createtabs.setTabShape(QTabWidget.Rounded)
        self.createtabs.setUsesScrollButtons(False)
        self.createtabs.setDocumentMode(True)
        self.createtabs.setTabsClosable(False)
        self.creator = QWidget()
        self.creator.setObjectName(u"creator")
        self.createtabs.addTab(self.creator, "")
        self.themer = QWidget()
        self.themer.setObjectName(u"themer")
        self.themer.setEnabled(True)
        self.textcolorLabel = QLabel(self.themer)
        self.textcolorLabel.setObjectName(u"textcolorLabel")
        self.textcolorLabel.setGeometry(QRect(0, 70, 81, 18))
        self.widget = QWidget(self.themer)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(240, 50, 251, 381))
        self.plainTextEdit = QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(0, 300, 241, 81))
        self.plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.richardSave = QPushButton(self.widget)
        self.richardSave.setObjectName(u"richardSave")
        self.richardSave.setGeometry(QRect(170, 20, 71, 61))
        self.richardTitle = QLabel(self.widget)
        self.richardTitle.setObjectName(u"richardTitle")
        self.richardTitle.setGeometry(QRect(0, 0, 241, 18))
        self.richardTitle.setFrameShape(QFrame.Box)
        self.richardTitle.setFrameShadow(QFrame.Raised)
        self.spinBox = QSpinBox(self.widget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(120, 50, 51, 32))
        self.spinBox.setMaximum(9)
        self.richardLabel1 = QLabel(self.widget)
        self.richardLabel1.setObjectName(u"richardLabel1")
        self.richardLabel1.setGeometry(QRect(120, 30, 51, 21))
        self.richardLabel1.setAlignment(Qt.AlignCenter)
        self.richardName = QLineEdit(self.widget)
        self.richardName.setObjectName(u"richardName")
        self.richardName.setGeometry(QRect(0, 50, 121, 31))
        self.richardRefresh = QPushButton(self.widget)
        self.richardRefresh.setObjectName(u"richardRefresh")
        self.richardRefresh.setGeometry(QRect(0, 20, 121, 31))
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(128, 350, 91, 34))
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setFlat(True)
        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 80, 241, 221))
        self.scrollArea.setFrameShadow(QFrame.Sunken)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(
            u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 216, 217))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.textColorEnter = QLineEdit(self.themer)
        self.textColorEnter.setObjectName(u"textColorEnter")
        self.textColorEnter.setGeometry(QRect(0, 90, 113, 32))
        self.textColorEnter.setMaxLength(32767)
        self.textColorEnter.setClearButtonEnabled(False)
        self.bgColorLabel = QLabel(self.themer)
        self.bgColorLabel.setObjectName(u"bgColorLabel")
        self.bgColorLabel.setGeometry(QRect(0, 160, 131, 18))
        self.bgColorEnter = QLineEdit(self.themer)
        self.bgColorEnter.setObjectName(u"bgColorEnter")
        self.bgColorEnter.setGeometry(QRect(0, 180, 113, 32))
        self.bgColorEnter.setMaxLength(32767)
        self.bgColorEnter.setClearButtonEnabled(False)
        self.buttonColorLabel = QLabel(self.themer)
        self.buttonColorLabel.setObjectName(u"buttonColorLabel")
        self.buttonColorLabel.setGeometry(QRect(0, 260, 111, 18))
        self.buttonColorEnter = QLineEdit(self.themer)
        self.buttonColorEnter.setObjectName(u"buttonColorEnter")
        self.buttonColorEnter.setGeometry(QRect(0, 280, 113, 32))
        self.buttonColorEnter.setMaxLength(32767)
        self.buttonColorEnter.setClearButtonEnabled(False)
        self.pushButton_2 = QPushButton(self.themer)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(50, 350, 141, 81))
        self.createtabs.addTab(self.themer, "")
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.miniSole.sizePolicy().hasHeightForWidth())
        self.miniSole.setSizePolicy(sizePolicy1)
        self.miniSole.setMinimumSize(QSize(500, 0))
        self.miniSole.setMaximumSize(QSize(16777215, 200))
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
        # Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        self.Tabs.setCurrentIndex(2)
        self.serverRefreshButton.setDefault(False)
        self.startButton.setDefault(False)
        self.settingtabs.setCurrentIndex(0)
        self.createtabs.setCurrentIndex(1)
        self.logClearButton.setDefault(False)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate(
            "Main", u"Javier | MC Server Launcher", None))
# if QT_CONFIG(tooltip)
        self.searchBar.setToolTip(QCoreApplication.translate(
            "Main", u"<html><head/><body><p>Search/Filter through your servers so that you can find the perfect server even faster!</p></body></html>", None))
# endif // QT_CONFIG(tooltip)
        self.searchBar.setInputMask("")
        self.searchBar.setText("")
        self.searchBar.setPlaceholderText(
            QCoreApplication.translate("Main", u"Query", None))
        self.setRamLabel.setText(
            QCoreApplication.translate("Main", u"Set RAM", None))
# if QT_CONFIG(tooltip)
        self.ramEnter.setToolTip(QCoreApplication.translate(
            "Main", u"<html><head/><body><p>RAM to use for the server, in gigabytes.</p></body></html>", None))
# endif // QT_CONFIG(tooltip)
        self.ramEnter.setSuffix(
            QCoreApplication.translate("Main", u" GB", None))
# if QT_CONFIG(tooltip)
        self.serverRefreshButton.setToolTip(QCoreApplication.translate(
            "Main", u"<html><head/><body><p>Refreshes the serverlist<br/>maybe Javier forgot something?</p></body></html>", None))
# endif // QT_CONFIG(tooltip)
        self.serverRefreshButton.setText(QCoreApplication.translate(
            "Main", u"Refresh Server List / Search", None))
# if QT_CONFIG(tooltip)
        self.startButton.setToolTip(QCoreApplication.translate(
            "Main", u"<html><head/><body><p>What it says on the tin.</p></body></html>", None))
# endif // QT_CONFIG(tooltip)
        self.startButton.setText(QCoreApplication.translate("Main", u"Select a\n"
                                                            "Server!", None))
        self.Tabs.setTabText(self.Tabs.indexOf(
            self.launcherTab), QCoreApplication.translate("Main", u"Launcher", None))
# if QT_CONFIG(tooltip)
        self.Tabs.setTabToolTip(self.Tabs.indexOf(self.launcherTab), QCoreApplication.translate(
            "Main", u"Where you launch your minecraft servers!", None))
# endif // QT_CONFIG(tooltip)
# if QT_CONFIG(tooltip)
        self.addDirButton.setToolTip(QCoreApplication.translate(
            "Main", u"<html><head/><body><p>Adds a new directory for Javier to look through when searching for your servers to display in the Launch tab!</p></body></html>", None))
# endif // QT_CONFIG(tooltip)
        self.addDirButton.setText(QCoreApplication.translate(
            "Main", u"Add New Directory", None))
# if QT_CONFIG(tooltip)
        self.themeRefresh.setToolTip(QCoreApplication.translate(
            "Main", u"<html><head/><body><p>Can't find your current theme?<br/>Themes are stored in Internals/themes</p></body></html>", None))
# endif // QT_CONFIG(tooltip)
        self.themeRefresh.setText(QCoreApplication.translate(
            "Main", u"Refresh Theme Selector", None))
# if QT_CONFIG(tooltip)
        self.javaIntBox.setToolTip(QCoreApplication.translate(
            "Main", u"<html><head/><body><p>this is the major java version number</p><p>generally 8 and 16 are used, but maybe you need something esle!<br/>8 is mainly for forge/older versions of MC<br/>and 16+ is for anything above 1.15</p></body></html>", None))
# endif // QT_CONFIG(tooltip)
# if QT_CONFIG(tooltip)
        self.downJavaButton.setToolTip(QCoreApplication.translate(
            "Main", u"download the java major version selected!", None))
# endif // QT_CONFIG(tooltip)
        self.downJavaButton.setText(QCoreApplication.translate(
            "Main", u"Download Java        ", None))
        self.settingtabs.setTabText(self.settingtabs.indexOf(
            self.normSettings), QCoreApplication.translate("Main", u"Javier Related", None))
# if QT_CONFIG(tooltip)
        self.jarFileEntry.setToolTip(QCoreApplication.translate(
            "Main", u"<html><head/><body><p>DEFAULT: EMPTY (JAVIER WILL FIND IT)</p><p>.jar file override should really only be used incase Javier manages to get the wrong server jar file for your server.</p><p>if you don't know what this means, don't worry about it!</p></body></html>", None))
# endif // QT_CONFIG(tooltip)
        self.jarFileEntry.setText("")
        self.jarFileEntry.setPlaceholderText(
            QCoreApplication.translate("Main", u".jar file override", None))
# if QT_CONFIG(tooltip)
        self.defaultCheck.setToolTip(QCoreApplication.translate(
            "Main", u"<html><head/><body><p>TEMPORARY</p><p>used for if you want your settings to be saved as the default, or if they're for the specific server</p></body></html>", None))
# endif // QT_CONFIG(tooltip)
        self.defaultCheck.setText(
            QCoreApplication.translate("Main", u"Default", None))
# if QT_CONFIG(tooltip)
        self.sJavaOver.setToolTip(QCoreApplication.translate(
            "Main", u"<html><head/><body><p>DEFAULT: EMPTY (java)<br/>Java Runtime Binary is the filepath at which your java goes, this one is server specific- the Forge modloader on any MC version likes to use Java 8.</p><p>besides that you should be good with java 18 for all versions</p><p>if you don't know what any of this means, don't worry about it!</p></body></html>", None))
# endif // QT_CONFIG(tooltip)
        self.sJavaOver.setPlaceholderText(QCoreApplication.translate(
            "Main", u"java binary runtime override", None))
# if QT_CONFIG(tooltip)
        self.jraEntry.setToolTip(QCoreApplication.translate(
            "Main", u"<html><head/><body><p>DEFAULT: NONE<br/>Java Runtime Arguments, these can help your server run more efficiently </p><p>if you don't know what this means, don't worry about it!</p></body></html>", None))
# endif // QT_CONFIG(tooltip)
        self.jraEntry.setPlaceholderText(QCoreApplication.translate(
            "Main", u"Java Runtime Arguments", None))
# if QT_CONFIG(tooltip)
        self.serverSelectLabel.setToolTip(
            QCoreApplication.translate("Main", u"The server Selected", None))
# endif // QT_CONFIG(tooltip)
        self.serverSelectLabel.setText(QCoreApplication.translate(
            "Main", u"No Server Selected!", None))
        self.saveSettings.setText(
            QCoreApplication.translate("Main", u"Save Settings", None))
# if QT_CONFIG(tooltip)
        self.jarGuiCheck.setToolTip(QCoreApplication.translate(
            "Main", u"<html><head/><body><p>DEFAULT: OFF</p><p>Toggles the server .jar GUI</p><p>if you don't know what this means, leave it off</p></body></html>", None))
# endif // QT_CONFIG(tooltip)
        self.jarGuiCheck.setText(
            QCoreApplication.translate("Main", u"Jar GUI", None))
# if QT_CONFIG(tooltip)
        self.safemodeCheck.setToolTip(QCoreApplication.translate(
            "Main", u"<html><head/><body><p>DEFAULT: OFF</p><p>Safemode will only run the vanilla jar without any datapacks if there are any.</p><p>mainly used for troubleshooting issues</p></body></html>", None))
# endif // QT_CONFIG(tooltip)
        self.safemodeCheck.setText(
            QCoreApplication.translate("Main", u"Safemode", None))
# if QT_CONFIG(tooltip)
        self.javaRefresh.setToolTip(QCoreApplication.translate(
            "Main", u"<html><head/><body><p>Can't find a java version?<br/>make sure it's downloaded!</p></body></html>", None))
# endif // QT_CONFIG(tooltip)
        self.javaRefresh.setText(QCoreApplication.translate(
            "Main", u"Refresh Java Selector", None))
        self.proplabel.setText(QCoreApplication.translate(
            "Main", u"Server Properties", None))
        self.propBrowser.setDocumentTitle(
            QCoreApplication.translate("Main", u"server properties", None))
        self.propBrowser.setHtml(QCoreApplication.translate("Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>server properties</title><style type=\"text/css\">\n"
                                                            "p, li { white-space: pre-wrap; }\n"
                                                            "</style></head><body style=\" font-family:'Noto Sans'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.propBrowser.setPlaceholderText(QCoreApplication.translate(
            "Main", u"Whoops! you haven't selected a server, the server doesn't have a server.properties yet,  or somehow someway Javier messed something up.  you tell me.", None))
        self.settingtabs.setTabText(self.settingtabs.indexOf(
            self.advancedSettings), QCoreApplication.translate("Main", u"Server Related", None))
        self.Tabs.setTabText(self.Tabs.indexOf(
            self.settingsTab), QCoreApplication.translate("Main", u"Settings", None))
# if QT_CONFIG(tooltip)
        self.Tabs.setTabToolTip(self.Tabs.indexOf(
            self.settingsTab), QCoreApplication.translate("Main", u"The Settings Page", None))
# endif // QT_CONFIG(tooltip)
        self.createtabs.setTabText(self.createtabs.indexOf(
            self.creator), QCoreApplication.translate("Main", u"Server Creation", None))
        self.textcolorLabel.setText(
            QCoreApplication.translate("Main", u"text color", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("Main", u"server!!!\n"
                                                                   "themes succes!\n"
                                                                   "yay!   Richard!", None))
        self.richardSave.setText(QCoreApplication.translate("Main", u"Save\n"
                                                            "Nothing!", None))
        self.richardTitle.setText(QCoreApplication.translate(
            "Main", u"[  ]  Richard | Javier Theme Helper     [X]", None))
        self.spinBox.setSuffix(QCoreApplication.translate("Main", u"kb", None))
        self.richardLabel1.setText(
            QCoreApplication.translate("Main", u"SETTER", None))
        self.richardName.setPlaceholderText(
            QCoreApplication.translate("Main", u"Enter Name", None))
        self.richardRefresh.setText(
            QCoreApplication.translate("Main", u"Refresh Theme", None))
# if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate(
            "Main", u"the spooky secret button ooooooo", None))
# endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate(
            "Main", u"Quirky Button!", None))
        self.textColorEnter.setInputMask("")
        self.textColorEnter.setText("")
        self.textColorEnter.setPlaceholderText(
            QCoreApplication.translate("Main", u"#Hexcode", None))
        self.bgColorLabel.setText(QCoreApplication.translate(
            "Main", u"background color", None))
        self.bgColorEnter.setInputMask("")
        self.bgColorEnter.setText("")
        self.bgColorEnter.setPlaceholderText(
            QCoreApplication.translate("Main", u"#Hexcode", None))
        self.buttonColorLabel.setText(
            QCoreApplication.translate("Main", u"button color", None))
        self.buttonColorEnter.setInputMask("")
        self.buttonColorEnter.setText("")
        self.buttonColorEnter.setPlaceholderText(
            QCoreApplication.translate("Main", u"#Hexcode", None))
        self.pushButton_2.setText(QCoreApplication.translate("Main", u"See it in action\n"
                                                             "using Richard", None))
        self.createtabs.setTabText(self.createtabs.indexOf(
            self.themer), QCoreApplication.translate("Main", u"Theme Creation", None))
        self.Tabs.setTabText(self.Tabs.indexOf(
            self.creatorTab), QCoreApplication.translate("Main", u"Creator", None))
# if QT_CONFIG(tooltip)
        self.Tabs.setTabToolTip(self.Tabs.indexOf(self.creatorTab), QCoreApplication.translate(
            "Main", u"The Server Creator, where you make your servers", None))
# endif // QT_CONFIG(tooltip)
        self.Tabs.setTabText(self.Tabs.indexOf(
            self.helpTab), QCoreApplication.translate("Main", u"Help", None))
# if QT_CONFIG(tooltip)
        self.Tabs.setTabToolTip(self.Tabs.indexOf(self.helpTab), QCoreApplication.translate(
            "Main", u"What do you expect this to mean?", None))
# endif // QT_CONFIG(tooltip)
        self.logClearButton.setText(
            QCoreApplication.translate("Main", u"Clear MiniSole", None))
        self.updateCheckerButton.setText(
            QCoreApplication.translate("Main", u"No Updates Found!", None))
    # retranslateUi
