# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DESUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(491, 382)
        Form.setMinimumSize(QtCore.QSize(491, 382))
        Form.setMaximumSize(QtCore.QSize(491, 382))
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(80, 240, 411, 141))
        self.plainTextEdit_2.setMinimumSize(QtCore.QSize(411, 141))
        self.plainTextEdit_2.setMaximumSize(QtCore.QSize(411, 141))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(80, 10, 150, 30))
        self.plainTextEdit_3.setMinimumSize(QtCore.QSize(150, 30))
        self.plainTextEdit_3.setMaximumSize(QtCore.QSize(200, 30))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(310, 10, 150, 30))
        self.plainTextEdit_4.setMaximumSize(QtCore.QSize(150, 30))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 10, 31, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 10, 41, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 190, 75, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 190, 75, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(80, 50, 411, 136))
        self.plainTextEdit.setMinimumSize(QtCore.QSize(411, 136))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(411, 136))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 89, 61, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 250, 61, 41))
        self.label_4.setObjectName("label_4")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(250, 190, 89, 16))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(250, 220, 89, 16))
        self.radioButton_2.setObjectName("radioButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.plainTextEdit_3, self.plainTextEdit_4)
        Form.setTabOrder(self.plainTextEdit_4, self.plainTextEdit)
        Form.setTabOrder(self.plainTextEdit, self.pushButton)
        Form.setTabOrder(self.pushButton, self.radioButton)
        Form.setTabOrder(self.radioButton, self.radioButton_2)
        Form.setTabOrder(self.radioButton_2, self.pushButton_2)
        Form.setTabOrder(self.pushButton_2, self.plainTextEdit_2)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "DES加密解密"))
        self.label.setText(_translate("Form", "密钥1"))
        self.label_2.setText(_translate("Form", "密钥2"))
        self.pushButton.setText(_translate("Form", "加密"))
        self.pushButton_2.setText(_translate("Form", "解密"))
        self.label_3.setText(_translate("Form", "未加密文本"))
        self.label_4.setText(_translate("Form", "加密后文本"))
        self.radioButton.setText(_translate("Form", "一重加密"))
        self.radioButton_2.setText(_translate("Form", "三重加密"))

