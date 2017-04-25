# import DataProcess
# # import tkinter
# # top = tkinter .Tk()
# # 进入消息循环
# # top.mainloop()
# txt = 'asdzxcfgsdnkjbkl'
# key1 = 'asdccdvb'
# key2 = 'acvcfghj'
# print('需要加密的文本：',txt)
# print('加密后的结果：',DataProcess.tripleencodemain(txt,key1,key2))
# print('解密后的结果：',DataProcess.tripledecodemain(DataProcess.tripleencodemain(txt,key1,key2),key1,key2))
# DataProcess.key('asdccdvb')
# print(DataProcess.F('11101110111010110011100000001100',0))
# for i in range(15,-1,-1):
#     print(i)
# a = '01234567890123456789012345678901'
# print(a[0:16])
# print(a[16:32])
# print(DataProcess.key(key))
#
# from tkinter
# root = tkinter.Tk()
# root.mainloop()


#
# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
#                              QVBoxLayout, QApplication)
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         lcd = QLCDNumber(self)
#         sld = QSlider(Qt.Horizontal, self)
#
#         vbox = QVBoxLayout()
#         vbox.addWidget(lcd)
#         vbox.addWidget(sld)
#
#         self.setLayout(vbox)
#         sld.valueChanged.connect(lcd.display)
#
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('Signal & slot')
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())