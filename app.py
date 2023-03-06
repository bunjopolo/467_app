from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import random
from algorithms import fcfs, rr

fcfs_processes = [[0,4,3,4], [1,3,1,3], [2,10,2,10], [3, 5, 2, 5], [4,5,2,5], [5,6,7,8]]
runtime = 20

rr_processes = [[4,8], [8,5]]
quantum = 2

# def fcfs(processes):
#     algorithm_name = "First Come First Serve (FCFS)"
#     dl_missed = None
#     n = len(processes)
#     output = []
#     current_time = 0 
#     while current_time < runtime:
#         for i in range(n):
#             start_time = current_time
#             end_time = start_time + processes[i][1]
#             #deadline missed
#             if end_time > processes[i][3]:
#                 dl_missed = i
#             output.append([start_time, end_time])
#             current_time = end_time 
#         if dl_missed:
#             print("Deadline missed for task T{}".format(dl_missed))
#         else:
#             print("No deadline missed")
#     return output, algorithm_name



app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def main():
    values, _ = fcfs(fcfs_processes)
    print(values)
    
    labels = ["T{}".format(i) for i in range(len(values))]
    return render_template('graph.html', data=values, labels=labels)
    # do something

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4444, debug=True)



