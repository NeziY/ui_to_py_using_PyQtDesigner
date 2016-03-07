# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CLIENT.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4 import QtWebKit
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow():
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(407, 219)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.send_txtbx = QtGui.QLineEdit(self.centralwidget)
        self.send_txtbx.setGeometry(QtCore.QRect(30, 70, 191, 21))
        self.send_txtbx.setObjectName(_fromUtf8("send_txtbx"))
        self.send_btn = QtGui.QPushButton(self.centralwidget)
        self.send_btn.setEnabled(True)
        self.send_btn.setGeometry(QtCore.QRect(21, 120, 110, 32))
        self.send_btn.setObjectName(_fromUtf8("send_btn"))
        self.rqst_label = QtGui.QLabel(self.centralwidget)
        self.rqst_label.setGeometry(QtCore.QRect(30, 40, 56, 13))
        self.rqst_label.setObjectName(_fromUtf8("rqst_label"))

        self.send_btn.clicked.connect(self.send_to_server)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def send_to_server(self):
        try:
            msg = str(self.send_txtbx.text())
            print(msg)
        except:
            pass


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Client", None))
        self.send_btn.setText(_translate("MainWindow", "Send", None))
        self.rqst_label.setText(_translate("MainWindow", "Requests", None))


app = QApplication([])
window_widget = QWidget()
window = Ui_MainWindow()
window.setupUi(window_widget)
window_widget.show()
app.exec_()

