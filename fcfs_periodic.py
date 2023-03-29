import random
import matplotlib.pyplot as plt

fcfs_processes = {'arrival': [0, 4, 7], 'period': [8, 3, 10], 'execution': [2, 1, 5], 'deadline': None}

runtime = 30

def fcfs(processes, runtime):
    algorithm_name = "First Come First Serve (FCFS) - Periodic Tasks"
    n = len(processes['arrival'])
    output = [[] for _ in range(n)]
    current_time = 0 
    periods = processes['period']
    next_arrival = processes['arrival'].copy()

    while current_time <= runtime:
        scheduled = False
        for i in range(n):
            # check if it's time for the task to arrive
            if current_time >= next_arrival[i]:
                # get start time and end time of current task instance
                start_time = max(current_time, next_arrival[i])
                end_time = start_time + processes['execution'][i]


                ##THIS MIGHT BE WRONG - CHECK
                if start_time > next_arrival[i] and start_time > processes['arrival'][i]:
                    # task missed deadline
                    print(f"Task {i+1} missed deadline at {next_arrival[i]}")
                # add task instance to outputq
                output[i].append([start_time, end_time])
                current_time = end_time
                next_arrival[i] = start_time + periods[i]
                # indicate that a task was scheduled in this iteration 
                scheduled = True

        # if no tasks were scheduled in this iteration, increment time
        if not scheduled:
            current_time += 1

    return output, algorithm_name


def gantt_chart(output, algorithm_name, runtime):
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
    gantt_chart.set_xlim(0, runtime)
    plt.show()

output, algorithm_name = fcfs(fcfs_processes, runtime)
gantt_chart(output, algorithm_name, runtime)
