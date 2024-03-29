# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import login
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    dlg = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 356)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblWelcome = QtWidgets.QLabel(self.centralwidget)
        self.lblWelcome.setGeometry(QtCore.QRect(150, 20, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblWelcome.setFont(font)
        self.lblWelcome.setObjectName("lblWelcome")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSkin = QtWidgets.QMenu(self.menuFile)
        self.menuSkin.setObjectName("menuSkin")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSkin_1 = QtWidgets.QAction(MainWindow)
        self.actionSkin_1.setObjectName("actionSkin_1")
        self.actionSkin_2 = QtWidgets.QAction(MainWindow)
        self.actionSkin_2.setObjectName("actionSkin_2")
        self.actionNone = QtWidgets.QAction(MainWindow)
        self.actionNone.setObjectName("actionNone")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.menuSkin.addAction(self.actionSkin_1)
        self.menuSkin.addAction(self.actionSkin_2)
        self.menuSkin.addAction(self.actionNone)
        self.menuFile.addAction(self.actionLogin)
        self.menuFile.addAction(self.menuSkin.menuAction())
        self.menuFile.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblWelcome.setText(_translate("MainWindow", "ĐĂNG NHẬP THÀNH CÔNG"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSkin.setTitle(_translate("MainWindow", "Skin"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSkin_1.setText(_translate("MainWindow", "Skin 1"))
        self.actionSkin_2.setText(_translate("MainWindow", "Skin 2"))
        self.actionNone.setText(_translate("MainWindow", "None"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))

        self.actionLogin.triggered.connect(self.login)
        self.actionClose.triggered.connect(lambda: MainWindow.close())
    def login(self):
        global dlg
        dlg = QtWidgets.QDialog()
        ui = login.Ui_Dialog()
        ui.setupUi(dlg)
        dlg.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
