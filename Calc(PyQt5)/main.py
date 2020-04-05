# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from latest import main_producer


class Ui_MainWindow(object):

    def __init__(self):
        self.main_eq=''

    def add_b(self):
        self.main_eq+='+'
        self.equationlabel.setText(self.main_eq)

    def sub_b(self):
        self.main_eq+='-'
        self.equationlabel.setText(self.main_eq)

    def mul_b(self):
        self.main_eq+='*'
        self.equationlabel.setText(self.main_eq)

    def div_b(self):
        self.main_eq+='/'
        self.equationlabel.setText(self.main_eq)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.equationlabel = QtWidgets.QLabel(self.centralwidget)
        self.equationlabel.setGeometry(QtCore.QRect(50, 60, 581, 61))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(22)
        self.equationlabel.setFont(font)
        self.equationlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.equationlabel.setObjectName("equationlabel")

        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(60, 200, 131, 111))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.add_button.clicked.connect(self.add_b)

        self.sub_button = QtWidgets.QPushButton(self.centralwidget)
        self.sub_button.setGeometry(QtCore.QRect(220, 200, 131, 111))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.sub_button.setFont(font)
        self.sub_button.setObjectName("sub_button")
        self.sub_button.clicked.connect(self.sub_b)

        self.mul_button = QtWidgets.QPushButton(self.centralwidget)
        self.mul_button.setGeometry(QtCore.QRect(60, 340, 131, 111))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.mul_button.setFont(font)
        self.mul_button.setObjectName("mul_button")
        self.mul_button.clicked.connect(self.mul_b)

        self.div_button = QtWidgets.QPushButton(self.centralwidget)
        self.div_button.setGeometry(QtCore.QRect(220, 340, 131, 111))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.div_button.setFont(font)
        self.div_button.setObjectName("div_button")
        self.div_button.clicked.connect(self.div_b)

        self.Inputbox = QtWidgets.QGroupBox(self.centralwidget)
        self.Inputbox.setGeometry(QtCore.QRect(440, 190, 301, 341))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Inputbox.setFont(font)
        self.Inputbox.setObjectName("Inputbox")

        self._1_button = QtWidgets.QPushButton(self.Inputbox)
        self._1_button.setGeometry(QtCore.QRect(10, 20, 81, 71))
        self._1_button.setObjectName("_1_button")
        self._1_button.clicked.connect(self._1_b)

        self._2_button = QtWidgets.QPushButton(self.Inputbox)
        self._2_button.setGeometry(QtCore.QRect(110, 20, 81, 71))
        self._2_button.setObjectName("_2_button")
        self._2_button.clicked.connect(self._2_b)

        self._3_button = QtWidgets.QPushButton(self.Inputbox)
        self._3_button.setGeometry(QtCore.QRect(210, 20, 81, 71))
        self._3_button.setObjectName("_3_button")
        self._3_button.clicked.connect(self._3_b)

        self._4_button = QtWidgets.QPushButton(self.Inputbox)
        self._4_button.setGeometry(QtCore.QRect(10, 100, 81, 71))
        self._4_button.setObjectName("_4_button")
        self._4_button.clicked.connect(self._4_b)

        self._7_button = QtWidgets.QPushButton(self.Inputbox)
        self._7_button.setGeometry(QtCore.QRect(10, 180, 81, 71))
        self._7_button.setObjectName("_7_button")
        self._7_button.clicked.connect(self._7_b)

        self._5_button = QtWidgets.QPushButton(self.Inputbox)
        self._5_button.setGeometry(QtCore.QRect(110, 100, 81, 71))
        self._5_button.setObjectName("_5_button")
        self._5_button.clicked.connect(self._5_b)

        self._6_button = QtWidgets.QPushButton(self.Inputbox)
        self._6_button.setGeometry(QtCore.QRect(210, 100, 81, 71))
        self._6_button.setObjectName("_6_button")
        self._6_button.clicked.connect(self._6_b)

        self._8_button = QtWidgets.QPushButton(self.Inputbox)
        self._8_button.setGeometry(QtCore.QRect(110, 180, 81, 71))
        self._8_button.setObjectName("_8_button")
        self._8_button.clicked.connect(self._8_b)

        self._9_button = QtWidgets.QPushButton(self.Inputbox)
        self._9_button.setGeometry(QtCore.QRect(210, 180, 81, 71))
        self._9_button.setObjectName("_9_button")
        self._9_button.clicked.connect(self._9_b)

        self._0_button = QtWidgets.QPushButton(self.Inputbox)
        self._0_button.setGeometry(QtCore.QRect(110, 260, 81, 71))
        self._0_button.setObjectName("_0_button")
        self._0_button.clicked.connect(self._0_b)

        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(60, 470, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")
        self.submit_button.clicked.connect(self.submit_b)

        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(640, 80, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.delete_button.setFont(font)
        self.delete_button.setObjectName("delete_button")
        self.delete_button.clicked.connect(self.del_b)

        
        self.clr_button = QtWidgets.QPushButton(self.centralwidget)
        self.clr_button.setGeometry(QtCore.QRect(260, 470, 91, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.clr_button.setFont(font)
        self.clr_button.setObjectName("clr_button")
        self.clr_button.clicked.connect(self.clr_b)


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def submit_b(self):
        self.main_eq = main_producer(self.main_eq)
        self.equationlabel.setText(self.main_eq)

    def del_b(self):
    	if len(self.main_eq)>0:
	        r = self.main_eq[::-1]
	        self.main_eq = r.replace(r[0],'',1)[::-1]
	        self.equationlabel.setText(self.main_eq)

    def clr_b(self):
        self.main_eq = ''
        self.equationlabel.setText(self.main_eq)

    def _1_b(self):
        self.main_eq+='1'
        self.equationlabel.setText(self.main_eq)

    def _2_b(self):
        self.main_eq+='2'
        self.equationlabel.setText(self.main_eq)

    def _3_b(self):
        self.main_eq+='3'
        self.equationlabel.setText(self.main_eq)

    def _4_b(self):
        self.main_eq+='4'
        self.equationlabel.setText(self.main_eq)

    def _5_b(self):
        self.main_eq+='5'
        self.equationlabel.setText(self.main_eq)

    def _6_b(self):
        self.main_eq+='6'
        self.equationlabel.setText(self.main_eq)

    def _7_b(self):
        self.main_eq+='7'
        self.equationlabel.setText(self.main_eq)

    def _8_b(self):
        self.main_eq+='8'
        self.equationlabel.setText(self.main_eq)

    def _9_b(self):
        self.main_eq+='9'
        self.equationlabel.setText(self.main_eq)

    def _0_b(self):
        self.main_eq+='0'
        self.equationlabel.setText(self.main_eq)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MyCalcy"))
        self.equationlabel.setText(_translate("MainWindow", "Equation Here"))
        self.add_button.setText(_translate("MainWindow", "+"))
        self.sub_button.setText(_translate("MainWindow", "-"))
        self.mul_button.setText(_translate("MainWindow", "*"))
        self.div_button.setText(_translate("MainWindow", "/"))
        self._1_button.setText(_translate("MainWindow", "1"))
        self._2_button.setText(_translate("MainWindow", "2"))
        self._3_button.setText(_translate("MainWindow", "3"))
        self._4_button.setText(_translate("MainWindow", "4"))
        self._7_button.setText(_translate("MainWindow", "7"))
        self._5_button.setText(_translate("MainWindow", "5"))
        self._6_button.setText(_translate("MainWindow", "6"))
        self._8_button.setText(_translate("MainWindow", "8"))
        self._9_button.setText(_translate("MainWindow", "9"))
        self._0_button.setText(_translate("MainWindow", "0"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.delete_button.setText(_translate("MainWindow", "Del"))
        self.clr_button.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
