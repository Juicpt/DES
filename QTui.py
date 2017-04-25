from PyQt5 import QtWidgets
from DESUI import Ui_Form
import DataProcess


class mywindow(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.encode) #点击加密按钮
        self.pushButton_2.clicked.connect(self.decode)#点击解密按钮


    def encode(self):#加密
        txt = self.plainTextEdit.toPlainText()
        k1 = self.plainTextEdit_3.toPlainText()
        k2 = self.plainTextEdit_4.toPlainText()
        self.plainTextEdit_2.clear()
        if self.radioButton.isChecked() == True:#判断加密方式
            self.plainTextEdit_2.appendPlainText(DataProcess.encodemain(txt,k1))
        else:
            self.plainTextEdit_2.appendPlainText(DataProcess.tripleencodemain(txt,k1,k2))


    def decode(self):#解密
        txt = self.plainTextEdit_2.toPlainText()
        k1 = self.plainTextEdit_3.toPlainText()
        k2 = self.plainTextEdit_4.toPlainText()
        self.plainTextEdit.clear()
        if self.radioButton.isChecked() == True:#判断解密方式
            self.plainTextEdit.appendPlainText(DataProcess.decodemain(txt,k1))
        else:
            self.plainTextEdit.appendPlainText(DataProcess.tripledecodemain(txt,k1,k2))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
