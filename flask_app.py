from flask import Flask, render_template, request
from algorithms_v3 import fcfs, rr, fcfs_periodic, check_deadlines
#chrome://net-internals/#sockets if you get a connection error
#processes in form: fcfs_processes = {'arrival': [0, 4, 7], 'period': [8, 3, 5], 'execution': [2, 1, 5], 'deadline': None}
app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':

        deadlines_missed = []
        #get user input
        algorithm = request.form['algorithm']
        arrival_times = request.form['arrival_times']
        execution_times = request.form['execution_times']
        runtime = request.form['runtime']

        #convert all inputs to lists and integers
        arrival_times = [int(i) for i in arrival_times.split(',')]
        execution_times = [int(i) for i in execution_times.split(',')]
        runtime = int(runtime)

        if algorithm == 'fcfs-p':
            period = request.form['period']
            period = [int(i) for i in period.split(',')]
            task_data = {'arrival': arrival_times, 'period': period, 'execution': execution_times, 'deadline': None, 'quantum': None}
        if algorithm == 'rr':
            deadlines = request.form['deadlines']
            quantum = request.form['quantum']
            deadlines = [int(i) for i in deadlines.split(',')]
            quantum = int(quantum)
            task_data = {'arrival': arrival_times, 'period': None, 'execution': execution_times, 'deadline': deadlines, 'quantum': quantum}
        if algorithm == 'fcfs':
            deadlines = request.form['deadlines']
            deadlines = [int(i) for i in deadlines.split(',')]
            task_data = {'arrival': arrival_times, 'period': None, 'execution': execution_times, 'deadline': deadlines, 'quantum': None}


    
        if algorithm == 'fcfs':
            values = fcfs(task_data, runtime)
            deadlines_missed = check_deadlines(values, task_data['deadline'])
        elif algorithm == 'rr':
            values= rr(task_data, runtime)
            deadlines_missed = check_deadlines(values, task_data['deadline'])
        elif algorithm == 'fcfs-p':
            values, deadlines_missed = fcfs_periodic(task_data, runtime)
            
        return render_template('Graph_V3.html', data = values, deadlines = deadlines_missed)

    return render_template('Graph_V3.html', data = [[1,2]])


if __name__ == '__main__':
    app.run(debug=True)



