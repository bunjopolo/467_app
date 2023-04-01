from flask import Flask, render_template, request
from algorithms import fcfs, rr, fcfs_periodic
#chrome://net-internals/#sockets if you get a connection error
#processes in form: fcfs_processes = {'arrival': [0, 4, 7], 'period': [8, 3, 5], 'execution': [2, 1, 5], 'deadline': None}
app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':

        #get user input
        arrival_times = request.form['arrival_times']
        execution_times = request.form['execution_times']
        runtime = request.form['runtime']
        algorithm = request.form['algorithm']
        period = request.form['period']
        quantum = request.form['quantum']

        #convert all inputs to lists and integers
        arrival_times = [int(i) for i in arrival_times.split(',')]
        execution_times = [int(i) for i in execution_times.split(',')]
        runtime = int(runtime)
        if algorithm == 'fcfs-p':
            period = [int(i) for i in period.split(',')]
        if algorithm == 'rr':
            quantum = int(quantum)

        #processes in form: fcfs_processes = {'arrival': [0, 4, 7], 'period': [8, 3, 5], 'execution': [2, 1, 5], 'deadline': None}
        task_data = {'arrival': arrival_times, 'period': period, 'execution': execution_times, 'deadline': None, 'quantum': quantum}
    
        if algorithm == 'fcfs':
            values = fcfs(task_data, runtime)
        elif algorithm == 'rr':
            values= rr(task_data, runtime)
        elif algorithm == 'fcfs-p':
            values = fcfs_periodic(task_data, runtime)
            
        return render_template('Graph_V3.html', data = values)

    return render_template('Graph_V3.html', data = [[1,2]])


if __name__ == '__main__':
    app.run(debug=True)



