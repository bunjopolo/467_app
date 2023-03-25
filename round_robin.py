
import random
import matplotlib.pyplot as plt
rr_processes = {'arrival': [0, 3, 10], 'period': None, 'execution': [30, 10, 40], 'deadline': [35, 25, 40], 'quantum': 5}

runtime = sum(rr_processes['execution']) 


def rr(processes, runtime):
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


def gantt_chart_rr(output, algorithm_name, runtime, deadlines_missed):
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

    for i in range(len(deadlines_missed)):
        if deadlines_missed[i]:
            gantt_chart.axvline(x=deadlines_missed[i][0], color='r', linestyle='--')
            gantt_chart.text(deadlines_missed[i][0], 0.25, f"T{i+1} missed deadline", ha="center", va="center", rotation=90)

    gantt_chart.set_xlim(0, runtime)
    plt.show()

output, algorithm_name, missed_dl = rr(rr_processes, runtime)
print(missed_dl)
print(output, algorithm_name) 
gantt_chart_rr(output, algorithm_name, runtime, missed_dl)


