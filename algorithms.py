import matplotlib.pyplot as plt
import random

#phase, period,execution time, deadline
fcfs_processes = [[0,4,3,4], [1,3,1,3], [2,10,2,10], [3, 5, 2, 5]]
runtime = 20

rr_processes = [[4,8], [8,5]]
quantum = 2

def fcfs(processes):
    algorithm_name = "First Come First Serve (FCFS)"
    dl_missed = None
    n = len(processes)
    output = [[] for _ in range(n)]
    current_time = 0 
    while current_time < runtime:
        for i in range(n):
            start_time = current_time
            end_time = start_time + processes[i][1]

            #deadline missed
            if end_time > processes[i][3]:
                dl_missed = i

            output[i].append([start_time, end_time])
            current_time = end_time 

        if dl_missed:
            print("Deadline missed for task T{}".format(dl_missed))
        else:
            print("No deadline missed")
    return output, algorithm_name



def rr(processes, quantum):
    n = len(processes)
    output = [[] for _ in range(n)]
    current_time = 0
    tmp = 0
    count = n 
    algorithm_name = "Round Robin"
    runtime = 50
    
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


def rr_with_runtime(processes, quantum, runtime):
    n = len(processes)
    output = [[] for _ in range(n)]
    current_time = 0
    tmp = 0
    algorithm_name = "Round Robin"
    
    while current_time < runtime:
        processes_tmp = processes
        count = n
        while count > 0:
            print(processes_tmp)
            if tmp == n:
                current_time += 1
                tmp = 0
            for i in range(n):
                start_time = current_time
                if processes_tmp[i][0] > current_time:
                    tmp +=1
                    continue
                if processes_tmp[i][1] <= quantum:
                    end_time = start_time + processes_tmp[i][1]
                    processes_tmp[i][1] = 0
                    output[i].append([start_time, end_time])
                    current_time = end_time
                    count -= 1
                if processes[i][1] == 0:
                    continue
                else:
                    end_time = start_time + quantum
                    processes_tmp[i][1] -= quantum
                    output[i].append([start_time, end_time])
                    current_time = end_time
    return output, algorithm_name



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


if __name__ == "__main__":
    output, algorithm_name = fcfs(fcfs_processes)
    gantt_chart(output, algorithm_name)
    output, algorithm_name = rr(rr_processes, quantum)
    gantt_chart(output, algorithm_name)
    output = rr_with_runtime(rr_processes, quantum, 50)
    gantt_chart(output, algorithm_name)

