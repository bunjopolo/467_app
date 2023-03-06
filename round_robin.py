import matplotlib.pyplot as plt
import random

processes = [[4,8], [8,5]]

quantum = 2

def rr(processes, quantum):
    n = len(processes)
    output = [[] for _ in range(n)]
    current_time = 0
    tmp = 0
    count = n 
    algorithm_name = "Round Robin"
    while count > 0:
        if tmp == n:
            current_time += 1
            tmp = 0
        for i in range(n):
            start_time = current_time
            if processes[i][0] > current_time:
                tmp +=1
                continue
            if processes[i][1] <= quantum:
                end_time = start_time + processes[i][1]
                processes[i][1] = 0
                output[i].append([start_time, end_time])
                current_time = end_time
                count -= 1
            if processes[i][1] == 0:
                continue
            else:
                end_time = start_time + quantum
                processes[i][1] -= quantum
                output[i].append([start_time, end_time])
                current_time = end_time
    return output, algorithm_name  



#make array to store individual task output times in order to plot them in format [[]*n]


def gantt_chart(output, algorithm_name):
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
            gantt_chart.text((start_time + end_time)/2, 0.25, f"T{i}", ha="center", va="center")
    gantt_chart.set_xlim(0, end_time)
    plt.show()

output, algorithm_name = rr(processes, quantum)
print(output)


gantt_chart(output, algorithm_name)
