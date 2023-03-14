from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
import sys
import numpy as np


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 691)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graph_label = QtWidgets.QLabel(self.centralwidget)
        self.graph_label.setGeometry(QtCore.QRect(20, 10, 791, 391))
        self.graph_label.setText("")
        self.graph_label.setObjectName("graph_label")
        self.phase_label = QtWidgets.QLabel(self.centralwidget)
        self.phase_label.setGeometry(QtCore.QRect(60, 470, 41, 16))
        self.phase_label.setObjectName("phase_label")
        self.period_label = QtWidgets.QLabel(self.centralwidget)
        self.period_label.setGeometry(QtCore.QRect(60, 500, 41, 16))
        self.period_label.setObjectName("period_label")
        self.execution_label = QtWidgets.QLabel(self.centralwidget)
        self.execution_label.setGeometry(QtCore.QRect(10, 530, 101, 20))
        self.execution_label.setObjectName("execution_label")
        self.phas_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.phas_edit.setGeometry(QtCore.QRect(120, 470, 581, 21))
        self.phas_edit.setObjectName("phas_edit")
        self.period_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.period_edit.setGeometry(QtCore.QRect(120, 500, 581, 21))
        self.period_edit.setObjectName("period_edit")
        self.execution_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.execution_edit.setGeometry(QtCore.QRect(120, 530, 581, 21))
        self.execution_edit.setObjectName("execution_edit")
        self.deadline_label = QtWidgets.QLabel(self.centralwidget)
        self.deadline_label.setGeometry(QtCore.QRect(50, 560, 60, 16))
        self.deadline_label.setObjectName("deadline_label")
        self.deadline_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.deadline_edit.setGeometry(QtCore.QRect(120, 560, 581, 21))
        self.deadline_edit.setObjectName("deadline_edit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 590, 281, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda : self.schedule())
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(290, 430, 241, 26))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.phase_label.setText(_translate("MainWindow", "Phase "))
        self.period_label.setText(_translate("MainWindow", "Period"))
        self.execution_label.setText(_translate("MainWindow", "Execution TIme"))
        self.deadline_label.setText(_translate("MainWindow", "Deadline"))
        self.pushButton.setText(_translate("MainWindow", "Schedule! "))
        self.comboBox.setItemText(0, _translate("MainWindow", "Pick an Algorithm"))
        self.comboBox.setItemText(1, _translate("MainWindow", "First come first serve"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Round robin"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Rate Monotonic"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Shortest job first"))
        self.comboBox.isEditable()

    def schedule(MainWindow):

        test = "When you push the button it shcedules the tasks"
        MainWindow.graph_label.setText(test)
        number = MainWindow.comboBox.currentIndex()


        phase = MainWindow.phas_edit.text()
        phase_arr = []
        period = MainWindow.period_edit.text()
        period_arr = []
        execution = MainWindow.execution_edit.text()
        execution_arr = []
        deadline = MainWindow.deadline_edit.text()
        deadline_arr = []

        for i in phase:
            if i != " " and  not i.isdigit():
                print("Please enter numbers only")
                return
        for i in period:
            if i != " " and  not i.isdigit():
                print("Please enter numbers only")
                return
        for i in execution:
            if i != " " and  not i.isdigit():
                print("Please enter numbers only")
                return
        for i in deadline:
            if i != " " and  not i.isdigit():
                print("Please enter numbers only")
                return
        

        phase_arr = [int(i) for i in phase.split(" ")]
        period_arr = [int(i) for i in period.split(" ")]
        execution_arr = [int(i) for i in execution.split(" ")]
        deadline_arr = [int(i) for i in deadline.split(" ")]

        if len(phase_arr) != len(period_arr) or len(period_arr) != len(execution_arr) or len(execution_arr) != len(deadline_arr):
            MainWindow.graph_label.setText("Please enter the same number of tasks for each field")
            return
        

        if number ==0:
            MainWindow.graph_label.setText("Please pick an algorithm in the drop down list")
            return

        if number == 1:
            # First come first serve
            print("Running First come first serve")
            pass
        if number == 2:
            # Round robin
            print("Running Round robin")
            pass
        if number == 3:
            # Rate monotonic
            print("Running Rate monotonic")
            pass
        if number == 4:
            # Shortest job first
            print("Running Shortest job first")
            pass
            
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())