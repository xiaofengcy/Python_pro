# -*—coding:utf-8 -*-
# Created: 07-04-2017
#      by: python 3.4.3 and PyQt5-5.4
import sys
import os      # Python执行系统命令方法所用到的包
from PyQt5 import QtCore,QtGui,QtWidgets 

class Ui_shut(object):   #类 继承object类
	flag = True
	def setupUi(self,shut):  #方法
	    #设置窗体的大小
		shut.setObjectName("shut")
		shut.resize(420,180)             
		shut.setFixedSize(420,180)

		self.label = QtWidgets.QLabel(shut)
		self.label.setGeometry(QtCore.QRect(40,50,41,51)) #标签的位置
		self.label.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
		self.label.setObjectName("label")

		self.lineEdit = QtWidgets.QLineEdit(shut)
		self.lineEdit.setGeometry(QtCore.QRect(70, 50, 71, 41))
		self.lineEdit.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
		self.lineEdit.setObjectName("lineEdit")

		self.label_2 = QtWidgets.QLabel(shut)
		self.label_2.setGeometry(QtCore.QRect(150, 60, 31, 31))
		self.label_2.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
		self.label_2.setObjectName("label_2")

		self.lineEdit_2 = QtWidgets.QLineEdit(shut)
		self.lineEdit_2.setGeometry(QtCore.QRect(180, 50, 71, 41))
		self.lineEdit_2.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
		self.lineEdit_2.setObjectName("lineEdit_2")

		self.label_3 = QtWidgets.QLabel(shut)
		self.label_3.setGeometry(QtCore.QRect(260, 60, 31, 31))
		self.label_3.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
		self.label_3.setObjectName("label_3")

		self.pushButton = QtWidgets.QPushButton(shut,clicked=self.sd)  #为pushButton添加监听事件click。
		self.pushButton.setGeometry(QtCore.QRect(290, 50, 101, 41))
		self.pushButton.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
		self.pushButton.setObjectName("pushButton")

		self.label_4 = QtWidgets.QLabel(shut)
		self.label_4.setGeometry(QtCore.QRect(0, 120, 500, 31))
		self.label_4.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
		self.label_4.setObjectName("label_4")

		self.retranslateUi(shut)
		QtCore.QMetaObject.connectSlotsByName(shut) #connectSlotsByName是一个QMetaObject类里的静态函数，其作用是用来将QObject * o里的子QObject的某些信号按照其objectName连接到o的槽上。
        

	def retranslateUi(self,shut):
		_translate = QtCore.QCoreApplication.translate
		shut.setWindowTitle(_translate("shut", "Windows定时关机器"))
		self.label.setText(_translate("shut", "在："))
		self.label_2.setText(_translate("shut", "时"))
		self.label_3.setText(_translate("shut", "分"))
		self.label_4.setText(_translate("shut", "    请输入关机时间"))
		self.pushButton.setText(_translate("shut", "设置"))
	def sd(self,shut):        #self.sd为触发该事件后，需要执行的操作。
		h = self.lineEdit.text()
		m = self.lineEdit_2.text()
		if self.flag:
			self.flag = False
			try:                     #捕获所有异常
				os.popen('at'+ h + ':' + m + ' shutdown -s') #python执行cmd命令的方法
				self.label_4.setText('    设置成功! 系统将关机在今天 '+h+':'+m)
				self.pushButton.setText('移除')
				self.lineEdit.clear()
				self.lineEdit_2.clear()
			except:
				self.label_4.setText('Something is wrong~')
		else:
			self.flag = True
			try:
				os.popen('at /delete /yes')
				self.label_4.setText('成功，全部移除')
				self.pushButton.setText('Set')
				self.lineEdit.clear()
				self.lineEdit_2.clear()
			except:
				self.label_4.setText('Something is wrong')

if __name__ == '__main__':   
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_shut()
    ui.setupUi(Form) 
    Form.show()
    sys.exit(app.exec_())
		


