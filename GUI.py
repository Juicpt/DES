import wx

import DataProcess
import noname


class CalcFrame(noname.MyFrame1):
    def __init__(self, parent):
        noname.MyFrame1.__init__(self, parent)

#加密
    def encode(self, event):
        txt = str(self.m_textCtrl1.GetValue())
        key = str(self.m_textCtrl4.GetValue())
        self.m_textCtrl2.SetValue(DataProcess.encodemain(txt,key))

    def decode(self,event):
        txt = str(self.m_textCtrl2.GetValue())
        key = str(self.m_textCtrl4.GetValue())
        self.m_textCtrl1.SetValue(DataProcess.decodemain(txt, key))
app = wx.App(False)
frame = CalcFrame(None)
frame.Show(True)
# 主循环
app.MainLoop()