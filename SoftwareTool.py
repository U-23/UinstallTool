# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SoftwareTool.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # 窗体最大化设置
        MainWindow.showMaximized()
        MainWindow.setWindowFlags(
            QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        # MainWindow.resize(418, 549)
        MainWindow.setMinimumSize(QtCore.QSize(450, 549))
        MainWindow.move(400, 50)
        icon = QtGui.QIcon()
        self.cwd = os.getcwd() 
        icon.addPixmap(QtGui.QPixmap(self.cwd+"\\src_dir\\SoftwareTool.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(2, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("输入需查找的应用程序")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMargin(5)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        '''
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        '''
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setStyleSheet("padding:5px")
        self.menubar.setGeometry(QtCore.QRect(0, 0, 436, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setShortcut('Ctrl+S')
        self.actionsave.setObjectName("actionsave")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionuninstall = QtWidgets.QAction(MainWindow)
        self.actionuninstall.setObjectName("actionuninstall")
        self.actionuninstall.setShortcut('Del')
        self.actionmodify = QtWidgets.QAction(MainWindow)
        self.actionmodify.setObjectName("actionmodify")
        self.actionwinregLocation = QtWidgets.QAction(MainWindow)
        self.actionwinregLocation.setObjectName("actionwinregLocation")
        self.actionwinregLocation.setShortcut('Ctrl+R')
        self.actionfolderLocation = QtWidgets.QAction(MainWindow)
        self.actionfolderLocation.setObjectName("actionfolderLocation")
        self.actionfolderLocation.setShortcut('Ctrl+E')
        self.actiondelete = QtWidgets.QAction(MainWindow)
        self.actiondelete.setObjectName("actiondelete")
        self.actiondelete.setShortcut('Shift+Del')
        self.actionrefresh = QtWidgets.QAction(MainWindow)
        self.actionrefresh.setObjectName("actionrefresh")
        self.actionrefresh.setShortcut('F5')

        self.actioninterface_language = QtWidgets.QMenu(self.menu_3)
        self.actioninterface_language.setObjectName("actioninterface_language")
        self.action_english = QtWidgets.QAction(MainWindow)
        self.action_english.setObjectName("action_english")
        self.action_chinese = QtWidgets.QAction(MainWindow)
        self.action_chinese.setObjectName("action_chinese")
       


    
        self.menu.addAction(self.actionsave)
        self.menu.addAction(self.actionexit)

        self.menu_2.addAction(self.actionuninstall)
        self.menu_2.addAction(self.actionmodify)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionwinregLocation)
        self.menu_2.addAction(self.actionfolderLocation)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actiondelete)

        self.menu_3.addAction(self.actionrefresh)
        self.menu_3.addSeparator()
        self.menu_3.addMenu(self.actioninterface_language)

        self.actioninterface_language.addAction(self.action_english)
        self.actioninterface_language.addSeparator()
        self.actioninterface_language.addAction(self.action_chinese)



        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addMenu(self.menu_3)
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SoftewareTool"))
        self.menu.setTitle(_translate("MainWindow", "文件(F)"))
        self.menu_2.setTitle(_translate("MainWindow", "操作(O)"))
        self.menu_3.setTitle(_translate("MainWindow", "查看(V)"))
        self.menu_4.setTitle(_translate("MainWindow", "帮助(H)"))
        self.actionsave.setText(_translate("MainWindow", "导出为excel"))
        self.actionexit.setText(_translate("MainWindow", "退出"))

        self.actionuninstall.setText(_translate("MainWindow", "卸载(U)"))
        self.actionmodify.setText(_translate("MainWindow", "修改(M)"))
        self.actionwinregLocation.setText(_translate("MainWindow", "注册表位置(R)"))
        self.actionfolderLocation.setText(_translate("MainWindow", "文件夹位置(I)"))
        self.actiondelete.setText(_translate("MainWindow", "强制卸载(F)"))

        self.actionrefresh.setText(_translate("MainWindow", "刷新(R)"))

        self.actioninterface_language.setTitle(_translate("MainWindow", "界面语言"))
        self.action_english.setText(_translate("MainWindow", "English"))
        self.action_chinese.setText(_translate("MainWindow", "Chinese_Simplified(简体中文)"))

        #self.label.setText(_translate("MainWindow", '总共'+str(self.tableWidget.rowCount())+'个软件'))
        #self.tableWidget.setHorizontalHeaderLabels(_translate("MainWindow", '软件名称','大小','待定'))
        self.lineEdit.setPlaceholderText(_translate("MainWindow","输入需查找的应用程序"))







