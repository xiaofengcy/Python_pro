# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\Python_pro\项目四\天气查询桌面程序.ui'
#
# Created: Mon Jul 10 11:00:58 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from city import city

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(616, 564)
        font = QtGui.QFont()
        font.setPointSize(8)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(True)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 581, 531))
        self.groupBox.setStyleSheet("")
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
        self.groupBox_2.setGeometry(QtCore.QRect(20, 80, 531, 91))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(40, 40, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 40, 151, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 260, 161, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 240, 521, 271))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 471, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet("border-image: url(:/images/1.png);")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox, clicked=self.get_data_2)#今天天气
        self.pushButton_2.setGeometry(QtCore.QRect(40, 190, 151, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox,  clicked=self.get_data_3) #未来五天天气     
        self.pushButton_3.setGeometry(QtCore.QRect(380, 190, 151, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "天气查询"))
        self.label_3.setText(_translate("Dialog", "输入城市名称："))
        self.pushButton_2.setText(_translate("Dialog", "查看今天"))
        self.pushButton_3.setText(_translate("Dialog", "查看未来五天"))
    def get_data_2(self, Dialog):
        citycode = city.get(self.lineEdit_2.text())
        url = ('http://wthrcdn.etouch.cn/weather_mini?citykey=%s'% citycode)
        self.textEdit.setText('\n'+str(url))
        response = requests.request("GET", url)
        a = eval(response.content)
        forecast = a.get('data').get('forecast')
        self.textEdit.setText( 
                '                   '+a.get('data').get('city')+'\n'
                '日期：'+forecast[0].get('date')+'\n'
                '天气：'+forecast[0].get('type')+'\n'
                '温度：'+forecast[0].get('low')+'~'+forecast[0].get('high')+'℃\n'
                '风向：'+forecast[0].get('fengxiang')+'\n'
                '风级：'+forecast[0].get('fengli')+'\n'
                '感冒：'+a.get('data').get('ganmao')+'\n\n')
    def get_data_3(self, Dialog):
        citycode = city.get(self.lineEdit_2.text())
        url = ('http://wthrcdn.etouch.cn/weather_mini?citykey=%s'% citycode)
        self.textEdit.setText('\n'+str(url))
        response = requests.request("GET", url)
        a = eval(response.content)
        forecast = a.get('data').get('forecast')
        self.textEdit.setText( 
                '               '+a.get('data').get('city')+'未来五天天气\n'
                +forecast[0].get('date')+'\n'
                '      天气：'+forecast[0].get('type')+'\n'
                '      温度：'+forecast[0].get('low')+'~'+forecast[0].get('high')+'℃\n'
                '      风向：'+forecast[0].get('fengxiang')+'\n'
                '      风级：'+forecast[0].get('fengli')+'\n\n'
                
                +forecast[1].get('date')+'\n'
                '      天气：'+forecast[1].get('type')+'\n'
                '      温度：'+forecast[1].get('low')+'~'+forecast[0].get('high')+'℃\n'
                '      风向：'+forecast[1].get('fengxiang')+'\n'
                '      风级：'+forecast[1].get('fengli')+'\n\n'
                
                +forecast[2].get('date')+'\n'
                '      天气：'+forecast[2].get('type')+'\n'
                '      温度：'+forecast[2].get('low')+'~'+forecast[0].get('high')+'℃\n'
                '      风向：'+forecast[2].get('fengxiang')+'\n'
                '      风级：'+forecast[2].get('fengli')+'\n\n'
                
                +forecast[3].get('date')+'\n'
                '      天气：'+forecast[3].get('type')+'\n'
                '      温度：'+forecast[3].get('low')+'~'+forecast[0].get('high')+'℃\n'
                '      风向：'+forecast[3].get('fengxiang')+'\n'
                '      风级：'+forecast[3].get('fengli')+'\n\n'
                
                +forecast[4].get('date')+'\n'
                '      天气：'+forecast[4].get('type')+'\n'
                '      温度：'+forecast[4].get('low')+'~'+forecast[0].get('high')+'℃\n'
                '      风向：'+forecast[4].get('fengxiang')+'\n'
                '      风级：'+forecast[4].get('fengli')+'\n\n'
                )
              
                
                
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

