import PyQt6
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
import sys
import random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure



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

        
        layout = QVBoxLayout(self)
        self.frame = QFrame(self)
        layout.addWidget(self.frame)
        self.figure = Figure() #set the figure
        self.canvas = FigureCanvas(self.figure) #set the canvas
        self.frame.setLayout(QVBoxLayout(self.frame))
        self.frame.layout().addWidget(self.canvas)
        

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

        #done and in right position
        self.time_quant = QtWidgets.QLineEdit(self.centralwidget) #set the time quantum edit
        self.time_quant.setGeometry(QtCore.QRect(120, size.height()-230, 581, 21)) #set the size and location of the time quantum edit
        self.time_quant.setObjectName("time_quant") #set the name of the time quantum edit
        self.time_quant.setValidator(QtGui.QIntValidator())
        #hide the time quantum
        self.time_quant.hide() #hide the time quantum edit
        
        self.quant_label = QtWidgets.QLabel(self.centralwidget) #set the time quantum label
        self.quant_label.setGeometry(QtCore.QRect(10, size.height()-230, 101, 20)) #set the size and location of the time quantum label
        self.quant_label.setObjectName("time_label") #set the name of the time quantum label
        self.quant_label.setText("Time Quantum") #set the text of the time quantum label
        self.quant_label.hide() #hide the time quantum label

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
        self.comboBox.currentIndexChanged.connect(lambda : self.updateUI()) #connect the combo box to the updateUI function

        MainWindow.setCentralWidget(self.centralwidget) #set the central widget of the window
        self.menubar = QtWidgets.QMenuBar(MainWindow) #set the menu bar
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 24)) #set the size and location of the menu bar
        self.menubar.setObjectName("menubar") #set the name of the menu bar
        MainWindow.setMenuBar(self.menubar) #set the menu bar of the window
        self.statusbar = QtWidgets.QStatusBar(MainWindow) #set the status bar
        self.statusbar.setObjectName("statusbar") #set the name of the status bar
        MainWindow.setStatusBar(self.statusbar) #set the status bar of the window

        self.retranslateUi(MainWindow) #call the retranslateUi function
        QtCore.QMetaObject.connectSlotsByName(MainWindow) #connect the slots to the names
        self.updateUI() #call the updateUI function        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scheduler")) #set the title of the window
        self.phase_label.setText(_translate("MainWindow", "Arrival Time")) #set the text of the phase label
        self.period_label.setText(_translate("MainWindow", "Period")) #set the text of the period label
        self.execution_label.setText(_translate("MainWindow", "Execution Time")) #set the text of the execution label
        self.deadline_label.setText(_translate("MainWindow", "Deadline")) #set the text of the deadline label
        self.runTime_label.setText(_translate("MainWindow", "Run Time")) #set the text of the run time label
        
        # self.time_label.setText(_translate("MainWindow", "Time Quantum"))
        self.pushButton.setText(_translate("MainWindow", "Schedule! ")) #set the text of the push button
        self.clearButton.setText(_translate("MainWindow", "Clear")) #set the text of the clear button
        self.comboBox.setItemText(0, _translate("MainWindow", "Pick an Algorithm")) #set the text of the combo box
        self.comboBox.setItemText(1, _translate("MainWindow", "First come first serve")) #set the text of the combo box
        self.comboBox.setItemText(2, _translate("MainWindow", "Round robin")) #set the text of the combo box
        self.comboBox.setItemText(3, _translate("MainWindow", "Rate Monotonic")) #set the text of the combo box
        self.comboBox.isEditable() #set the combo box to not editable

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
            

    def schedule(MainWindow):
        
        number = MainWindow.comboBox.currentIndex()
        #grab the string from the phase box and create an array for phase
        arrival = MainWindow.phas_edit.text()
        arrival_arr = []
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
    

        #Grab the string from the runtime box and greate a integer variable for it
        run_time = MainWindow.runTime_edit.text()
        if not run_time:
            run_time = 0
        else:
            run_time = int(run_time)
        print(run_time)

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
        # for i in time_quant:
        #     if number ==2 and i != " " and  not i.isdigit():
        #         MainWindow.graph_label.setText("Please enter numbers only")              
        #         return

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

        #check if the user is trying to run round robin and if they are then check if they entered a time quantum if they did then set it what they inputed
        if number ==2:
            if not time_quant:
                MainWindow.graph_label.setText("Please enter a time quantum")
                return
            else:
                time_quant_num = int(time_quant)
        else:
            time_quant_num = 0
    
        
        #Check if the nummber of non zero elements in each array is the same
        if len(arrival_arr) != len(period_arr) or len(arrival_arr) != len(execution_arr) or len(arrival_arr) != len(deadline_arr) or len(period_arr)!= len(execution_arr) or len(period_arr)!= len(deadline_arr) or len(execution_arr)!= len(deadline_arr):
            MainWindow.graph_label.setText("Please enter the same number of tasks for each field")
            return
        
        #Calculate the run time
        if (number ==1 or number ==2) and run_time ==0:
            run_time = sum(execution_arr)


        #Create a dictionary to hold all the arrays
        processes = {'Run Time': run_time, 'arrival': arrival_arr, 'period': period_arr, 'execution': execution_arr, 'deadline': deadline_arr, 'quantum': time_quant_num}
        print(processes)

        #Get the number from the combobox and run the corresponding algorithm
        if number ==0:
            MainWindow.graph_label.setText("Please pick an algorithm in the drop down list")
            return

        if number == 1:
            # First come first serve
            if sum(period_arr) ==0:
                output, algorithm_name = MainWindow.fcfs(processes, run_time)
            else:
                output, algorithm_name = MainWindow.fcfs_periodic(processes, run_time)
            algorithm_name = "First Come First Serve"
            MainWindow.gantt_chart(output, algorithm_name, run_time)

        if number == 2:
            # Round robin
            output, algorithm_name, deadlinesMissed = MainWindow.rr(processes, run_time)
            MainWindow.gantt_chart_rr(output, algorithm_name, run_time, deadlinesMissed)
            
        if number == 3:
            # Rate monotonic
            
            if all(i == 0 for i in period_arr):
                MainWindow.graph_label.setText("Please enter periods")
                return
            
            algorithm_name = "Rate Monotonic"
            output, run_time = MainWindow.RM(processes)
            
            MainWindow.gantt_chart(output, algorithm_name,run_time)
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
    
    #RM works (should test arrival time still)
    def RM(self,info):
      
        tasks = [i for i in range(1, len(info['period'])+1)]
        period = info['period']
        executiontime = info['execution']
        phase = info['arrival']
        deadline = info['deadline']
        stats =[]
        currentstats = []
        time = 0
        currenttask = 1
        newtasks = []
        hyperperiod = 0
        taskorder = []


        #execute 1 time unit of current task
        def execute(time, currenttask, currentstats):
            time = time + 1 #increments the time counter
            column = [i[0] for i in currentstats] # find the current task
            currentstats[column.index(currenttask)][3] -= 1 # decrements the execution time
            return time, currenttask, currentstats
            

        # checks if current task is complete
        def completecheck(time, currentstats, currenttask):
            column = [i[0] for i in currentstats] # finds the current task in the sorted current stats list
            if currentstats[column.index(currenttask)][3] == 0: # checks if the completion time is 0
                currentstats[column.index(currenttask)][7].append(time) # adds current time to the finish time for the current task
                return True, currentstats
            else : # task is not finished
                return False, currentstats
            
            
        #checks if there is a new instance of a task and updates the execution time accordingly
        def newinstance(time, currentstats):
            for i in range(len(currentstats)): # loop through number of tasks
                if (time - stats[i][1]) % stats[i][2] == 0 and time> stats[i][1]: # check if the current time is equal to the time of a new instance
                    currentstats[i][3] = stats[i][3] #task i has a new instance and execution time is updated
                    newtask = True
                else :
                    newtask = False # task i does not have a new instance
            return newtask, currentstats
        
            
        # create fucntion to check if any deadlines were missed
        def deadlinemiss(currentstats):  
            for i in range(len(currentstats)): #loop through number of tasks
                for j in range(len(currentstats[i][7])): #loop through each occurrence of task
                    if currentstats[i][7][j] > j*currentstats[1][2] or currentstats[i][7][j]> currentstats[i][1] + j*currentstats[i][2] + currentstats[i][4]:#check if completion time of task is greater than the next occurence or the next relative deadline
                        currentstats[i][8].append(j) # instance j of task number i was missed
                        return currentstats
                        

        # checks if there is a task that will preempt the current task
        def preemptcheck(currenttask, currentstats):
            for i in range(len(currentstats)): # loop the number of tasks
                column = [i[0] for i in currentstats] # finds the current task in the sorted current stats list
                if currentstats[i][2] < currentstats[column.index(currenttask)][2] and currentstats[i][3] != 0: # checks if there is a task with higher priority and is not finished
                    return True
            return False
                

        # sort the tasks based on period
        def sorttasks(stats, currentstats):
            currentstats.sort(key = lambda x: x[2]) # sorts the current stats by period
            stats.sort(key = lambda x: x[2]) # sorts the stats by period


        def findnexttask(currenttask, currentstats):
            tempcurrenttask = currenttask # creates a temporary value for the current task
            for i in range(len(currentstats)): # loop through the number of tasks
                if currentstats[i][1] < time: # checks if the phase is less that the current time (does the task exist yet)
                    if currentstats[i][3] != 0 : #checks if the execution time is not zero (is task incomplete)
                        currenttask = currentstats[i][0] # sets the current task as the task number satisfying above requirements
                        if currenttask != tempcurrenttask: # checks if new value for current task is same as the old task
                            column = [i[0] for i in currentstats]
                            currentstats[column.index(currenttask)][5].append(time) # updates the start time of the new task 
                        return currenttask, currentstats, tempcurrenttask
                    else:
                        continue # pass to next task
                else:
                    continue #  ppass to next task
            return -1, currentstats, tempcurrenttask # returns a negative 1 if there are no tasks available


        # define funciton to increment time and wait if there are no tasks available
        def wait(time):
            time += 1
            return time


        # create funciton for finding the least common multiple     
        def find_lcm(numbers):
            def gcd(a, b):
                if b == 0:
                    return a
                return gcd(b, a % b)

            lcm = 1
            for number in numbers:
                lcm = (lcm * number) // gcd(lcm, number)

            return lcm


        #create stats list
        for i in range(len(tasks)):
            stats.append([tasks[i], phase[i], period[i], executiontime[i], deadline[i], [], []]) # creates an array of all the information about the tasks
            currentstats.append([tasks[i], phase[i], period[i], executiontime[i], deadline[i], [], [], [], []])# creates an array of all the information about the tasks that will be updated


        # sorts the stats by the period
        stats.sort(key = lambda x: x[2])
        currentstats.sort(key = lambda x: x[2])


        # initializes new tasks to false
        for i in range(len(currentstats)):
            newtasks.append(False)


        hyperperiod = find_lcm(period) # find the hyperperiod
        currenttask = currentstats[0][0] # initializes the current task to the fist in the sorted list
            
        column = [i[0] for i in currentstats]
        if currentstats[column.index(currenttask)][1] == 0:
            currentstats[column.index(currenttask)][5].append(time)

        if currentstats[column.index(currenttask)][1] > 0:
            time = currentstats[column.index(currenttask)][1]
            currentstats[column.index(currenttask)][5].append(time)
            

        while(time< hyperperiod):
            taskorder.append(currenttask)
            time, currenttask, currentstats = execute(time, currenttask, currentstats) # execute current task for one time unit

            done, currentstats = completecheck(time, currentstats, currenttask) # checks if current tasks is complete
            
            newtask, currentstats = newinstance(time, currentstats) # checks if there is a new instance of a task

            preempt = preemptcheck(currenttask, currentstats) # checks if there is a higher priority task  
            
            temp, currentstats, previous = findnexttask(currenttask, currentstats) # find the next task to be executed
            column = [i[0] for i in currentstats] # find the current task in the sorted list


            if temp != previous: # checks if the new task is differnt from the previous task
                column = [i[0] for i in currentstats] # find the current task in the sorted list
                currentstats[column.index(currenttask)][6].append(time) # updates the end time for the previous task ######################################################################################################
            if temp ==-1: # checks if there are no new tasks to execute
                while (temp == -1): 
                    time = wait(time) # sit idle for one time unit
                    newtask, currentstats = newinstance(time, currentstats) # check for a new instance of a task
                    temp, currentstats, previous = findnexttask(currenttask, currentstats) # find what the next task is
                currenttask = temp
            else :
                currenttask = temp
            if currentstats[0][5][-1] == hyperperiod: # checks if the current task is complete and remove last element
                currentstats[0][5].pop() # remove the last element of the end time list
        
                        
        currentstats = deadlinemiss(currentstats)    

        outputs = []
        #reorder by task number
        currentstats.sort(key = lambda x: x[0])
        for i in range(len(currentstats)):
            outputs.append([])
            for j in range(len(currentstats[i][5])):
                outputs[i].append([currentstats[i][5][j], currentstats[i][6][j]])
        
                
        return outputs, hyperperiod

    #works without period
    def fcfs(self,processes, runtime):
        
        algorithm_name = "First Come First Serve (FCFS)"
        dl_missed = []
        n = len(processes['arrival'])
        output = [[] for _ in range(n)]
        current_time = 0
        
        scheduled = None

        while current_time < runtime:
            
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
    
    def fcfs_periodic(self,processes, runtime):
        algorithm_name = "First Come First Serve (FCFS)"
        n = len(processes['arrival'])
        output = [[] for _ in range(n)]
        current_time = 0 
        periods = processes['period']
        next_arrival = processes['arrival'].copy()
        deadlines_missed = [0 for _ in range(n)]

        while current_time <= runtime:
            scheduled = False
            for i in range(n):
                # check if it's time for the task to arrive
                if current_time >= next_arrival[i]:
                    # get start time and end time of current task instance
                    start_time = max(current_time, next_arrival[i])
                    if start_time + processes['execution'][i] > runtime:
                        end_time = runtime 
                        # check if deadline is missed
                        if end_time > next_arrival[i]:
                            deadlines_missed.append(next_arrival[i])
                        # add task instance to output
                        output[i].append([start_time, end_time])
                        return output, algorithm_name
                    else:
                        end_time = start_time + processes['execution'][i]
                        # check if deadline is missed
                        if end_time > next_arrival[i]:
                            deadlines_missed.append(next_arrival[i])
                        # add task instance to output
                        output[i].append([start_time, end_time])
                    current_time = end_time
                    next_arrival[i] = start_time + periods[i]
                    # indicate that a task was scheduled in this iteration 
                    scheduled = True

            # if no tasks were scheduled in this iteration, increment time
            if not scheduled:
                current_time += 1
            print("Deadlines missed", deadlines_missed)
        return output, algorithm_name
    #works
    def rr(MainWindow,processes, runtime):
        n = len(processes['arrival'])
        output = [[] for _ in range(n)]
        current_time = 0
        algorithm_name = "Round Robin"
        deadlines_missed = [[] for _ in range(n)]

        while current_time < runtime:
            schueduled = False

            for i in range(n):
                start_time = current_time
                #check if current process has arrived
                if processes['arrival'][i] <= current_time:
                    
                    #check if current task  has finished
                    if processes['execution'][i] == 0:
                        continue

                    #if current iteration finishes task 
                    if processes['execution'][i] <= processes['quantum']:
                        end_time = start_time + processes['execution'][i]
                        processes['execution'][i] = 0
                        output[i].append([start_time, end_time])
                        current_time = end_time
                        if end_time > processes['deadline'][i]:
                            deadlines_missed[i].append(processes['deadline'][i]) 



                    else:
                        end_time = start_time + processes['quantum']
                        processes['execution'][i] -= processes['quantum']
                        output[i].append([start_time, end_time])
                        current_time = end_time
                        if end_time > processes['deadline'][i]:
                            deadlines_missed[i].append(processes['deadline'][i]) 
                    schueduled = True
                
            if not schueduled:
                current_time += 1
        return output, algorithm_name, deadlines_missed
    #works
    def gantt_chart_rr(MainWindow, output, algorithm_name, runtime, deadlines_missed):
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
                gantt_chart.text((start_time + end_time)/2, 0.25, f"T{i+1}", ha="center", va="center", fontsize= "x-small")
        #check to see if all the deadlines missed are 0 (no deadlines missed)
        deadlines_sum = [item for sublist in deadlines_missed for item in sublist]
        if sum(deadlines_sum) == 0:
            pass
        else:
            for i in range(len(deadlines_missed)):
                if deadlines_missed[i]:
                    gantt_chart.axvline(x=deadlines_missed[i][0], color='r', linestyle='--')
                    gantt_chart.text(deadlines_missed[i][0], 0.25, f"T{i+1} missed deadline", ha="center", va="center", rotation=90, fontsize= "x-small")

        gantt_chart.set_xlim(0, runtime)
        frame = QFrame(MainWindow)
        frame_layout = QHBoxLayout(frame)
        frame.setLayout(frame_layout)
        frame.setFixedSize(791, size.height()-450)
        canvas = FigureCanvas(fig)
        frame_layout.addWidget(canvas)
        image = frame.grab()
        MainWindow.graph_label.setPixmap(image)

    #works
    def gantt_chart(MainWindow,output, algorithm_name,hyperperiod):
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
                    gantt_chart.text((start_time + end_time)/2, 0.25, f"T{i+1}", ha="center", va="center", fontsize = "x-small")
            gantt_chart.set_xlim(0, hyperperiod)
            #plt.show()

            frame = QFrame(MainWindow)
            frame_layout = QHBoxLayout(frame)
            frame.setLayout(frame_layout)
            frame.setFixedSize(791, size.height()-450)
            canvas = FigureCanvas(fig)
            frame_layout.addWidget(canvas)
            image = frame.grab()
            MainWindow.graph_label.setPixmap(image)

            # fig.savefig('/Users/spencermarchand/Documents/VS_code/Python/467_project/img_sav')
            # MainWindow.graph_label.setPixmap(QtGui.QPixmap('/Users/spencermarchand/Documents/VS_code/Python/467_project/img_sav.png'))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyle('Windows')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())