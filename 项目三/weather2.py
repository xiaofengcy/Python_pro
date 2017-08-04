# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\Python_pro\???\????????.ui'
#
# Created: Thu Jul  6 21:59:09 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!
import urllib.request ,sys  
import re  
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(711, 629)
        font = QtGui.QFont()
        font.setPointSize(8)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(True)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 681, 591))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(250, 10, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 80, 631, 91))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 191, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 181, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(220, 20, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 60, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2,clicked=self.get_data)
        self.pushButton.setGeometry(QtCore.QRect(490, 40, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 161, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 220, 621, 351))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 611, 321))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.textEdit.show)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "????"))
        self.label_2.setText(_translate("Dialog", "????(??):"))
        self.label_3.setText(_translate("Dialog", "????(??):"))
        self.pushButton.setText(_translate("Dialog", "??"))
        self.label_4.setText(_translate("Dialog", "??????"))
    def get_data(self,Dialog):
        #?????url  
        url = "http://qq.ip138.com/weather/"+self.lineEdit.text()+'/'+ self.lineEdit_2.text()+'.htm' 

        #??????  
        weatherhtml = urllib.request.urlopen(url)  
        res = weatherhtml.read().decode('GB2312')  
                #???????????  
        pattern = 'Title.+<b>(.+)</b>'  
        Title = re.search(pattern,res).group(1)  
          
        pattern = '>(\d*-\d*-\d*.+?)<'  
        date = re.findall(pattern,res)  
          
        pattern = 'alt="(.+?)"'  
        weather = re.findall(pattern,res)

        self.textEdit.setText(str( "                  " +Title)+'\n\n\n'+"                    "+date[0]+"      "+weather[0]+'\n'+"                    "+date[1]+"      "+weather[1]+'\n'+"                    "+date[2]+"      "+weather[2]+'\n'+"                    "+date[3]+"      "+weather[3]+'\n'+"                    "+date[4]+"      "+weather[4]+'\n')

  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

