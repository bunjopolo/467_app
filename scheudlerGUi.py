from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
import sys
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PIL import Image


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
    
        screen = QApplication.primaryScreen() #get the screen size
        global size #make it global so we can use it in other functions
        size = screen.size() #get the size of the screen
        MainWindow.setObjectName("MainWindow") #set the name of the window
        MainWindow.resize(830, size.height()) #set the size of the window
        MainWindow.setFixedWidth(830) #set the width of the window
        self.centralwidget = QtWidgets.QWidget(MainWindow) #set the central widget
        self.centralwidget.setObjectName("centralwidget") #set the name of the central widget

        
        self.graph_label = QtWidgets.QLabel(self.centralwidget) #set the graph label
        self.graph_label.setGeometry(QtCore.QRect(20, 10, 791, size.height()-450)) #set the size and location of the graph label
        self.graph_label.setScaledContents(True) #scale the graph label to fit the size of the graph
        self.graph_label.setText("") #set the text of the graph label
        self.graph_label.setObjectName("graph_label") #set the name of the graph label
        self.graph_label.setStyleSheet("border: 1px solid black;") #set the border of the graph label

        self.phase_label = QtWidgets.QLabel(self.centralwidget) #set the phase label
        self.phase_label.setGeometry(QtCore.QRect(25, size.height()-350, 101, 16)) #set the size and location of the phase label
        self.phase_label.setObjectName("phase_label") #set the name of the phase label

        self.period_label = QtWidgets.QLabel(self.centralwidget) #set the period label
        self.period_label.setGeometry(QtCore.QRect(60, size.height()-320, 41, 16)) #set the size and location of the period label
        self.period_label.setObjectName("period_label") #set the name of the period label
         
        self.execution_label = QtWidgets.QLabel(self.centralwidget) #set the execution label
        self.execution_label.setGeometry(QtCore.QRect(10, size.height()-290, 101, 20)) #set the size and location of the execution label
        self.execution_label.setObjectName("execution_label") #set the name of the execution label

        self.runTime_label = QtWidgets.QLabel(self.centralwidget) #set the
        self.runTime_label.setGeometry(QtCore.QRect(50, size.height()-380, 60, 16)) #set the size and location of the run time label
        self.runTime_label.setObjectName("runTime_label") #set the name of the run time label
        #Done and in right position
        # self.time_label = QtWidgets.QLabel(self.centralwidget)
        # self.time_label.setGeometry(QtCore.QRect(10, size.height()-230, 101, 20))
        # self.time_label.setObjectName("time_label")
        
        self.runTime_edit = QtWidgets.QLineEdit(self.centralwidget) #set the run time edit
        self.runTime_edit.setGeometry(QtCore.QRect(120, size.height()-380, 581, 21)) #set the size and location of the run time edit
        self.runTime_edit.setObjectName("runTime_edit") #set the name of the run time edit
        self.runTime_edit.setValidator(QtGui.QIntValidator()) #set the validator of the run time edit to only accept integers

        self.phas_edit = QtWidgets.QLineEdit(self.centralwidget) #set the phase edit
        self.phas_edit.setGeometry(QtCore.QRect(120, size.height()-350, 581, 21)) #set the size and location of the phase edit
        self.phas_edit.setObjectName("phas_edit") #set the name of the phase edit
 
        self.period_edit = QtWidgets.QLineEdit(self.centralwidget) #set the period edit
        self.period_edit.setGeometry(QtCore.QRect(120, size.height()-320, 581, 21)) #set the size and location of the period edit
        self.period_edit.setObjectName("period_edit") #set the name of the period edit

        self.execution_edit = QtWidgets.QLineEdit(self.centralwidget) #set the execution edit
        self.execution_edit.setGeometry(QtCore.QRect(120, size.height()-290, 581, 21)) #set the size and location of the execution edit
        self.execution_edit.setObjectName("execution_edit") #set the name of the execution edit

        #done and in right position
        self.deadline_label = QtWidgets.QLabel(self.centralwidget) #set the deadline label
        self.deadline_label.setGeometry(QtCore.QRect(50, size.height()-260, 60, 16)) #set the size and location of the deadline label
        self.deadline_label.setObjectName("deadline_label") #set the name of the deadline label

        #done and in right position
        self.deadline_edit = QtWidgets.QLineEdit(self.centralwidget) #set the deadline edit
        self.deadline_edit.setGeometry(QtCore.QRect(120, size.height()-260, 581, 21)) #set the size and location of the deadline edit
        self.deadline_edit.setObjectName("deadline_edit") #set the name of the deadline edit

        
        #done and in right position
        # self.time_quant = QtWidgets.QLineEdit(self.centralwidget)
        # self.time_quant.setGeometry(QtCore.QRect(120, size.height()-230, 581, 21))
        # self.time_quant.setObjectName("time_quant")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget) #set the push button
        self.pushButton.setGeometry(QtCore.QRect(270, size.height()-200, 100, 51)) #set the size and location of the push button
        self.pushButton.setObjectName("pushButton") #set the name of the push button
        self.pushButton.clicked.connect(lambda : self.schedule()) #connect the push button to the schedule function
        

        self.clearButton = QtWidgets.QPushButton(self.centralwidget) #set the clear button
        self.clearButton.setGeometry(QtCore.QRect(400, size.height()-200, 100, 51)) #set the size and location of the clear button
        self.clearButton.clicked.connect(lambda : self.clearAll()) #connect the clear button to the clearAll function

        self.comboBox = QtWidgets.QComboBox(self.centralwidget) #set the combo box
        self.comboBox.setGeometry(QtCore.QRect(290, size.height()-420, 241, 26)) #set the size and location of the combo box
        self.comboBox.setEditable(False) #set the combo box to editable
        self.comboBox.setObjectName("comboBox") #set the name of the combo box
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentIndexChanged.connect(lambda : self.updateUI())

        self.time_quant = QtWidgets.QLineEdit(self.centralwidget)
        self.time_quant.setGeometry(QtCore.QRect(120, size.height()-230, 581, 21))
        self.time_quant.setObjectName("time_quant")
       
        #hide the time quantum
        self.time_quant.hide()
        
        self.quant_label = QtWidgets.QLabel(self.centralwidget)
        self.quant_label.setGeometry(QtCore.QRect(10, size.height()-230, 101, 20))
        self.quant_label.setObjectName("time_label")
        self.quant_label.setText("Time Quantum")
        self.quant_label.hide()

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
        self.updateUI()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.phase_label.setText(_translate("MainWindow", "Arrival Time"))
        self.period_label.setText(_translate("MainWindow", "Period"))
        self.execution_label.setText(_translate("MainWindow", "Execution Time"))
        self.deadline_label.setText(_translate("MainWindow", "Deadline"))
        self.runTime_label.setText(_translate("MainWindow", "Run Time"))
        
        # self.time_label.setText(_translate("MainWindow", "Time Quantum"))
        self.pushButton.setText(_translate("MainWindow", "Schedule! "))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Pick an Algorithm"))
        self.comboBox.setItemText(1, _translate("MainWindow", "First come first serve"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Round robin"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Rate Monotonic"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Shortest job first"))
        self.comboBox.isEditable()

    def updateUI(MainWindow):
        #update the windwow based on what combo box is selected
        if MainWindow.comboBox.currentIndex() == 0: #Pick an algorithm
            MainWindow.runTime_edit.setReadOnly(True)
            MainWindow.phas_edit.setReadOnly(True)
            MainWindow.period_edit.setReadOnly(True)
            MainWindow.execution_edit.setReadOnly(True)
            MainWindow.deadline_edit.setReadOnly(True)
            MainWindow.time_quant.hide()
            MainWindow.quant_label.hide()
        elif MainWindow.comboBox.currentIndex() == 1: #First come first serve
            MainWindow.runTime_edit.setReadOnly(False)
            MainWindow.phas_edit.setReadOnly(False)
            MainWindow.period_edit.setReadOnly(False)
            MainWindow.execution_edit.setReadOnly(False)
            MainWindow.deadline_edit.setReadOnly(False)
            MainWindow.time_quant.hide()
            MainWindow.quant_label.hide()
            MainWindow.clearAll()

        elif MainWindow.comboBox.currentIndex() == 2: #Round robin
            MainWindow.runTime_edit.setReadOnly(False)
            MainWindow.phas_edit.setReadOnly(False)
            MainWindow.period_edit.setReadOnly(False)
            MainWindow.execution_edit.setReadOnly(False)
            MainWindow.deadline_edit.setReadOnly(False)
            MainWindow.time_quant.show()
            MainWindow.quant_label.show()
            MainWindow.clearAll()

        elif MainWindow.comboBox.currentIndex() == 3: #Rate monotonic
            MainWindow.runTime_edit.setReadOnly(False)
            MainWindow.phas_edit.setReadOnly(False)
            MainWindow.period_edit.setReadOnly(False)
            MainWindow.execution_edit.setReadOnly(False)
            MainWindow.deadline_edit.setReadOnly(False)
            MainWindow.time_quant.hide()
            MainWindow.quant_label.hide()
            MainWindow.clearAll()
            
        elif MainWindow.comboBox.currentIndex() == 4: #Shortest job first
            MainWindow.runTime_edit.setReadOnly(False)
            MainWindow.phas_edit.setReadOnly(False)
            MainWindow.period_edit.setReadOnly(False)
            MainWindow.execution_edit.setReadOnly(False)
            MainWindow.deadline_edit.setReadOnly(False)
            MainWindow.time_quant.hide()
            MainWindow.quant_label.hide()
            MainWindow.clearAll()

    def schedule(MainWindow):
        
        number = MainWindow.comboBox.currentIndex()
        print(number)
        #grab the string from the phase box and create an array for phase
        arrival = MainWindow.phas_edit.text()
        arrival_arr = []
        print(arrival_arr)
        #grab the string from the period box and create an array for period
        period = MainWindow.period_edit.text()
        period_arr = []
        #grab the string from the execution box and create an array for execution
        execution = MainWindow.execution_edit.text()
        execution_arr = []
        #grab the string from the deadline box and create an array for deadline
        deadline = MainWindow.deadline_edit.text()
        deadline_arr = []
        #grab the string from the time quantum box and create an array for time quantum
        time_quant = MainWindow.time_quant.text()
        time_quant_arr = []

        #Grab the string from the runtime box and greate a integer variable for it
        run_time = MainWindow.runTime_edit.text()
        if not run_time:
            MainWindow.graph_label.setText("Please enter a run time")
            return
        else:
            run_time = int(run_time)

        #check if the user entered numbers only
        for i in arrival:
            if i != " " and  not i.isdigit():
                MainWindow.graph_label.setText("Please enter numbers only")
                return
        for i in period:
            if i != " " and  not i.isdigit():
                MainWindow.graph_label.setText("Please enter numbers only")
                return
        for i in execution:
            if i != " " and  not i.isdigit():
                MainWindow.graph_label.setText("Please enter numbers only")                   
                return
        for i in deadline:
            if i != " " and  not i.isdigit():
                MainWindow.graph_label.setText("Please enter numbers only")              
                return
            for i in time_quant:
                if number ==2 and i != " " and  not i.isdigit():
                    MainWindow.graph_label.setText("Please enter numbers only")              
                    return




        #Check if any of the fields are empty and if they are then populate it with 0's of the size of one of the non empty fields
        if not arrival:
            if len(period_arr) != 0:
                arrival_arr = [0]*len(period_arr)
            elif len(execution_arr) != 0:
                arrival_arr = [0]*len(execution_arr)
            elif len(deadline_arr) != 0:
                arrival_arr = [0]*len(deadline_arr)
            else:
                MainWindow.graph_label.setText("Please enter at least one task")
        else:
            arrival_arr = MainWindow.get_numbers(arrival)
            
        
        if not period:
            if len(arrival_arr) != 0:
                period_arr = [0]*len(arrival_arr)
            elif len(execution_arr) != 0:
                period_arr = [0]*len(execution_arr)
            elif len(deadline_arr) != 0:
                period_arr = [0]*len(deadline_arr)
            else:
                MainWindow.graph_label.setText("Please enter at least one task")
        else:
            period_arr = MainWindow.get_numbers(period)
                
        
        if not execution:
            if len(arrival_arr) != 0:
                execution_arr = [0]*len(arrival_arr)
            elif len(period_arr) != 0:
                execution_arr = [0]*len(period_arr)
            elif len(deadline_arr) != 0:
                execution_arr = [0]*len(deadline_arr)
            else:
                MainWindow.graph_label.setText("Please enter at least one task")
        else:
            execution_arr = MainWindow.get_numbers(execution)
                
        if not deadline:
            if len(arrival_arr) != 0:
                deadline_arr = [0]*len(arrival_arr)
            elif len(period_arr) != 0:
                deadline_arr = [0]*len(period_arr)
            elif len(execution_arr) != 0:
                deadline_arr = [0]*len(execution_arr)
            else:
                MainWindow.graph_label.setText("Please enter at least one task")
        else:
            deadline_arr = MainWindow.get_numbers(deadline)
        
        if not time_quant:
            if len(arrival_arr) != 0:
                time_quant_arr = [0]*len(arrival_arr)
            elif len(period_arr) != 0:
                time_quant_arr = [0]*len(period_arr)
            elif len(execution_arr) != 0:
                time_quant_arr = [0]*len(execution_arr)
            elif len(deadline_arr) != 0:
                time_quant_arr = [0]*len(deadline_arr)
            else:
                MainWindow.graph_label.setText("Please enter at least one task")
        else:
            time_quant_arr = MainWindow.get_numbers(time_quant)
        
        #Check if the nummber of non zero elements in each array is the same
        if len(arrival_arr) != len(period_arr) or len(arrival_arr) != len(execution_arr) or len(arrival_arr) != len(deadline_arr) or len(arrival_arr) != len(time_quant_arr):
            MainWindow.graph_label.setText("Please enter the same number of tasks for each field")
            return

        #Create a dictionary to hold all the arrays
        processes = {'Run Time': run_time, 'arrival': arrival_arr, 'period': period_arr, 'execution': execution_arr, 'deadline': deadline_arr, 'time_quantum': time_quant_arr}
        print(processes)
        #Get the number from the combobox and run the corresponding algorithm
        if number ==0:
            MainWindow.graph_label.setText("Please pick an algorithm in the drop down list")
            return

        if number == 1:
            # First come first serve
            print("Running First come first serve")
            output, algorithm_name = MainWindow.fcfs(processes, run_time)
            print(output)
            print(algorithm_name)
            MainWindow.gantt_chart(output, algorithm_name)

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

    def clearAll(MainWindow):
        MainWindow.runTime_edit.setText("")
        MainWindow.phas_edit.setText("")
        MainWindow.period_edit.setText("")
        MainWindow.execution_edit.setText("")
        MainWindow.deadline_edit.setText("")
        MainWindow.time_quant.setText("")
        MainWindow.graph_label.setPixmap(QtGui.QPixmap())

    def get_numbers(self,string):
            string = string.strip()
            numbers = string.split()
            numbers = [int(i) for i in numbers]
            return numbers
        
        

    def fcfs(self,processes, runtime):
        
        algorithm_name = "First Come First Serve (FCFS)"
        dl_missed = []
        n = len(processes['arrival'])
        output = [[] for _ in range(n)]
        current_time = 0
        
        scheduled = None

        while current_time < runtime:
            current_time +=1
            for i in range(n):
                #task not arrived yet try next task
                if processes['arrival'][i] > current_time:
                    continue

                #a task is ready to run
                elif current_time >= processes['period'][i] and processes['arrival'][i] <= current_time:
                    #get start time and end time of current task instance
                    start_time = current_time
                    end_time = start_time + processes['execution'][i]

                    # #deadline missed
                    # if end_time > processes['period'][i]:
                    #     dl_missed.append(["T{}".format(dl_missed), current_time])

                    output[i].append([start_time, end_time])
                    current_time = end_time 

                    #incriment period of current task to set new deadline for next instance
                    processes['period'][i] += processes['period'][i]
                    scheduled = True
            # if no tasks were scheduled in this iteration, incriment time
            if not scheduled:
                current_time +=1
            return output, algorithm_name

        

    def gantt_chart(MainWindow,output, algorithm_name):
            """
            output has to be in the format [[start_time, end_time], [start_time, end_time], ...]
            """
            colors = [f"#{random.randint(0, 0xFFFFFF):06x}" for _ in range(len(output))]
            fig, gantt_chart = plt.subplots()
            gantt_chart.set_title(algorithm_name)
            gantt_chart.set_xlabel("Time")
            gantt_chart.set_yticks([0])
            gantt_chart.set_yticklabels([""])
            for i in range(len(output)):
                for j in range(len(output[i])):
                    start_time, end_time = output[i][j]
                    gantt_chart.broken_barh([(start_time, end_time - start_time)], (0, 0.5), color=colors[i])
                    gantt_chart.text((start_time + end_time)/2, 0.25, f"T{i+1}", ha="center", va="center")
            gantt_chart.set_xlim(0, end_time)
            #plt.show()
            
            #canvas = FigureCanvas(fig)
            fig.savefig('/Users/spencermarchand/Documents/VS_code/Python/467_project/img_sav')
            MainWindow.graph_label.setPixmap(QtGui.QPixmap('/Users/spencermarchand/Documents/VS_code/Python/467_project/img_sav.png'))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())