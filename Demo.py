import DataProcess
f = open("F:\魅吧群第二次不记名投票.docx", "rb")
g = open("F:\加密","w+")
txt = f.read()

g.write(DataProcess.encodemain(txt,"adsdczda"))