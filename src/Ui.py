# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 652)
        MainWindow.setMaximumSize(QtCore.QSize(874, 652))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(67, 67, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(67, 67, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(67, 67, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(67, 67, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(67, 67, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 44, 44))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(67, 67, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(67, 67, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(67, 67, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("font: 75 12pt \"Arial\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.export_progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.export_progress_bar.setGeometry(QtCore.QRect(570, 600, 301, 23))
        self.export_progress_bar.setStyleSheet("color: white;\n"
"\n"
"QProgressBar::horizontal {\n"
"border: 1px solid gray;\n"
"border-radius: 3px;\n"
"background: white;\n"
"padding: 1px;\n"
"text-align: right;\n"
"margin-right: 4ex;\n"
"};")
        self.export_progress_bar.setMaximum(100)
        self.export_progress_bar.setProperty("value", 0)
        self.export_progress_bar.setInvertedAppearance(False)
        self.export_progress_bar.setObjectName("export_progress_bar")
        self.version_label = QtWidgets.QLabel(self.centralwidget)
        self.version_label.setGeometry(QtCore.QRect(770, 10, 81, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.version_label.setFont(font)
        self.version_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.version_label.setText("")
        self.version_label.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.version_label.setScaledContents(True)
        self.version_label.setObjectName("version_label")
        self.parser_selector = QtWidgets.QTabWidget(self.centralwidget)
        self.parser_selector.setGeometry(QtCore.QRect(10, 80, 851, 451))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.parser_selector.setPalette(palette)
        self.parser_selector.setAutoFillBackground(False)
        self.parser_selector.setStyleSheet("QWidget {\n"
"background: #1e1e1e;\n"
"}\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"border-top: 2px solid #C2C7CB;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"left: 0px; /* move to the right by 5px */\n"
"}\n"
"/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"background: #2d2d2d;\n"
"border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"min-width: 8ex;\n"
"padding: 10px;\n"
"color: white;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"background: #1e1e1e;\n"
"}\n"
"QTabBar::tab:selected {\n"
"border-color: #1e1e1e;\n"
"bottom-left-color:white;\n"
"border-right-color:white;\n"
"border: 1px;\n"
"border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"QTabBar::tab:!selected {\n"
"margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}")
        self.parser_selector.setTabPosition(QtWidgets.QTabWidget.North)
        self.parser_selector.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.parser_selector.setTabsClosable(False)
        self.parser_selector.setObjectName("parser_selector")
        self.jg_tab = QtWidgets.QWidget()
        self.jg_tab.setObjectName("jg_tab")
        self.jg_profile_list = QtWidgets.QListWidget(self.jg_tab)
        self.jg_profile_list.setEnabled(True)
        self.jg_profile_list.setGeometry(QtCore.QRect(20, 171, 256, 171))
        self.jg_profile_list.setStyleSheet("QListView::item {\n"
"color: white\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"background: blue;\n"
"color: white\n"
"}")
        self.jg_profile_list.setAlternatingRowColors(False)
        self.jg_profile_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.jg_profile_list.setObjectName("jg_profile_list")
        item = QtWidgets.QListWidgetItem()
        self.jg_profile_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.jg_profile_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.jg_profile_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.jg_profile_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.jg_profile_list.addItem(item)
        self.jg_available_profiles_label = QtWidgets.QLabel(self.jg_tab)
        self.jg_available_profiles_label.setGeometry(QtCore.QRect(20, 120, 251, 21))
        self.jg_available_profiles_label.setStyleSheet("color:white")
        self.jg_available_profiles_label.setObjectName("jg_available_profiles_label")
        self.jg_select_profile_button = QtWidgets.QPushButton(self.jg_tab)
        self.jg_select_profile_button.setGeometry(QtCore.QRect(20, 60, 261, 23))
        self.jg_select_profile_button.setStyleSheet("color:white;\n"
"border: 1px solid white;")
        self.jg_select_profile_button.setObjectName("jg_select_profile_button")
        self.label = QtWidgets.QLabel(self.jg_tab)
        self.label.setGeometry(QtCore.QRect(20, 29, 221, 20))
        self.label.setStyleSheet("color:white")
        self.label.setObjectName("label")
        self.jg_option_inherit_checkbox = QtWidgets.QCheckBox(self.jg_tab)
        self.jg_option_inherit_checkbox.setGeometry(QtCore.QRect(410, 60, 421, 20))
        self.jg_option_inherit_checkbox.setStyleSheet("color: white")
        self.jg_option_inherit_checkbox.setChecked(True)
        self.jg_option_inherit_checkbox.setObjectName("jg_option_inherit_checkbox")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/3rd_party/jg.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.parser_selector.addTab(self.jg_tab, icon1, "")
        self.dcs_tab = QtWidgets.QWidget()
        self.dcs_tab.setObjectName("dcs_tab")
        self.dcs_world_label = QtWidgets.QLabel(self.dcs_tab)
        self.dcs_world_label.setGeometry(QtCore.QRect(20, 30, 241, 16))
        self.dcs_world_label.setStyleSheet("color:white")
        self.dcs_world_label.setObjectName("dcs_world_label")
        self.dcs_directory_select_button = QtWidgets.QPushButton(self.dcs_tab)
        self.dcs_directory_select_button.setGeometry(QtCore.QRect(20, 80, 261, 23))
        self.dcs_directory_select_button.setStyleSheet("color:white;\n"
"border: 1px solid white;")
        self.dcs_directory_select_button.setObjectName("dcs_directory_select_button")
        self.dcs_saved_games_label = QtWidgets.QLabel(self.dcs_tab)
        self.dcs_saved_games_label.setGeometry(QtCore.QRect(20, 50, 261, 20))
        self.dcs_saved_games_label.setStyleSheet("font-size: 11px;\n"
"color:white;")
        self.dcs_saved_games_label.setObjectName("dcs_saved_games_label")
        self.dcs_profiles_list = QtWidgets.QListWidget(self.dcs_tab)
        self.dcs_profiles_list.setEnabled(True)
        self.dcs_profiles_list.setGeometry(QtCore.QRect(20, 180, 331, 201))
        self.dcs_profiles_list.setStyleSheet("color: white")
        self.dcs_profiles_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.dcs_profiles_list.setObjectName("dcs_profiles_list")
        item = QtWidgets.QListWidgetItem()
        self.dcs_profiles_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.dcs_profiles_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.dcs_profiles_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.dcs_profiles_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.dcs_profiles_list.addItem(item)
        self.label_7 = QtWidgets.QLabel(self.dcs_tab)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(20, 130, 241, 16))
        self.label_7.setStyleSheet("color:white")
        self.label_7.setObjectName("label_7")
        self.dcs_easy_mode_checkbox = QtWidgets.QCheckBox(self.dcs_tab)
        self.dcs_easy_mode_checkbox.setGeometry(QtCore.QRect(480, 80, 351, 20))
        self.dcs_easy_mode_checkbox.setStyleSheet("color: white")
        self.dcs_easy_mode_checkbox.setChecked(True)
        self.dcs_easy_mode_checkbox.setObjectName("dcs_easy_mode_checkbox")
        self.dcs_selected_directory_label = QtWidgets.QLabel(self.dcs_tab)
        self.dcs_selected_directory_label.setGeometry(QtCore.QRect(20, 150, 261, 20))
        self.dcs_selected_directory_label.setStyleSheet("font-size: 11px;\n"
"color:white;")
        self.dcs_selected_directory_label.setObjectName("dcs_selected_directory_label")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/3rd_party/dcs.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.parser_selector.addTab(self.dcs_tab, icon2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 821, 41))
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.parser_selector.addTab(self.tab, "")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(20, 10, 221, 41))
        self.title_label.setAutoFillBackground(False)
        self.title_label.setStyleSheet("color: white;\n"
"font-size: 20px")
        self.title_label.setTextFormat(QtCore.Qt.RichText)
        self.title_label.setObjectName("title_label")
        self.export_button = QtWidgets.QPushButton(self.centralwidget)
        self.export_button.setGeometry(QtCore.QRect(570, 550, 291, 41))
        self.export_button.setStyleSheet("colour: rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"QAbstractButton: {\n"
"font-color:white\n"
"};\n"
"QPushButton { color: red; background-color: white };\n"
"background-color: white;\n"
"\n"
"QAbstractButton::text {\n"
"color=white;\n"
"}")
        self.export_button.setIcon(icon)
        self.export_button.setCheckable(False)
        self.export_button.setChecked(False)
        self.export_button.setFlat(False)
        self.export_button.setObjectName("export_button")
        self.application_information_textbrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.application_information_textbrowser.setGeometry(QtCore.QRect(40, 550, 521, 71))
        self.application_information_textbrowser.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.application_information_textbrowser.setObjectName("application_information_textbrowser")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 580, 31, 16))
        self.label_8.setStyleSheet("color: white;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 43, 141, 30))
        self.label_9.setStyleSheet("color: white;")
        self.label_9.setObjectName("label_9")
        self.settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.settings_button.setGeometry(QtCore.QRect(620, 20, 121, 23))
        self.settings_button.setObjectName("settings_button")
        self.logs_button = QtWidgets.QPushButton(self.centralwidget)
        self.logs_button.setGeometry(QtCore.QRect(620, 50, 121, 23))
        self.logs_button.setObjectName("logs_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionVersion_Info = QtWidgets.QAction(MainWindow)
        self.actionVersion_Info.setObjectName("actionVersion_Info")

        self.retranslateUi(MainWindow)
        self.parser_selector.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Joystick Diagrams - V1.1.0"))
        __sortingEnabled = self.jg_profile_list.isSortingEnabled()
        self.jg_profile_list.setSortingEnabled(False)
        item = self.jg_profile_list.item(0)
        item.setText(_translate("MainWindow", "Base"))
        item = self.jg_profile_list.item(1)
        item.setText(_translate("MainWindow", "DCS A-10"))
        item = self.jg_profile_list.item(2)
        item.setText(_translate("MainWindow", "KA-50"))
        item = self.jg_profile_list.item(3)
        item.setText(_translate("MainWindow", "FC3"))
        item = self.jg_profile_list.item(4)
        item.setText(_translate("MainWindow", "FA18-C"))
        self.jg_profile_list.setSortingEnabled(__sortingEnabled)
        self.jg_available_profiles_label.setText(_translate("MainWindow", "Available Profiles"))
        self.jg_select_profile_button.setText(_translate("MainWindow", "Select your profile file"))
        self.label.setText(_translate("MainWindow", "Select your .XML profile "))
        self.jg_option_inherit_checkbox.setText(_translate("MainWindow", "Inherit Joystick Binds from Parents"))
        self.parser_selector.setTabText(self.parser_selector.indexOf(self.jg_tab), _translate("MainWindow", "Joystick Gremlin"))
        self.dcs_world_label.setText(_translate("MainWindow", "DCS World Directory"))
        self.dcs_directory_select_button.setText(_translate("MainWindow", "Select your installation"))
        self.dcs_saved_games_label.setText(_translate("MainWindow", "This should be your Saved Games/DCS folder"))
        __sortingEnabled = self.dcs_profiles_list.isSortingEnabled()
        self.dcs_profiles_list.setSortingEnabled(False)
        item = self.dcs_profiles_list.item(0)
        item.setText(_translate("MainWindow", "A10-C II"))
        item = self.dcs_profiles_list.item(1)
        item.setText(_translate("MainWindow", "FA-18C"))
        item = self.dcs_profiles_list.item(2)
        item.setText(_translate("MainWindow", "KA-50"))
        item = self.dcs_profiles_list.item(3)
        item.setText(_translate("MainWindow", "F-14B"))
        item = self.dcs_profiles_list.item(4)
        item.setText(_translate("MainWindow", "F-14B_Rio"))
        self.dcs_profiles_list.setSortingEnabled(__sortingEnabled)
        self.label_7.setText(_translate("MainWindow", "Available DCS Profiles"))
        self.dcs_easy_mode_checkbox.setText(_translate("MainWindow", "Exclude \"Easy\" Mode Profiles"))
        self.dcs_selected_directory_label.setText(_translate("MainWindow", "c:test"))
        self.parser_selector.setTabText(self.parser_selector.indexOf(self.dcs_tab), _translate("MainWindow", "DCS World"))
        self.label_2.setText(_translate("MainWindow", "Do you have a game you want to see included?"))
        self.parser_selector.setTabText(self.parser_selector.indexOf(self.tab), _translate("MainWindow", "+"))
        self.title_label.setText(_translate("MainWindow", "Joystick Diagrams"))
        self.export_button.setText(_translate("MainWindow", "Export Joystick Profiles"))
        self.application_information_textbrowser.setDocumentTitle(_translate("MainWindow", "Testsd"))
        self.application_information_textbrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Testsd</title><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">WELCOME bruv, joysticks innit</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Info"))
        self.label_9.setText(_translate("MainWindow", "1.1.0"))
        self.settings_button.setText(_translate("MainWindow", "Settings"))
        self.logs_button.setText(_translate("MainWindow", "Logs"))
        self.actionVersion_Info.setText(_translate("MainWindow", "Version.Info"))
