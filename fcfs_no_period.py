import random
import matplotlib.pyplot as plt


fcfs_processes = {'arrival': [0, 0], 'period': [4,7], 'execution': [2, 5], 'deadline': None}

#output_format = [[['t1_start_1','t1_end_1'],['t1_start_2','t1_end_2']], [['t2_start_1','t2_end_1'],['t2_start_2','t2_end_2']]] 


runtime = 40


def fcfs(processes, runtime):
    algorithm_name = "First Come First Serve (FCFS)"
    n = len(processes['arrival'])
    print(n)
    output = [[] for _ in range(n)]
    current_time = 0 
    scheduled = None
    periods = processes['period']

    while True:
        scheduled = False
        for i in range(n):
            #task not arrived yet try next task
            if processes['arrival'][i] > current_time:
                continue
            #a task is ready to run
            else:
                #get start time and end time of current task instance
                start_time = current_time
                end_time = start_time + processes['execution'][i]

                # #deadline missed
                # if end_time > processes['period'][i]:
                #     dl_missed.append(["T{}".format(dl_missed), current_time])

                output[i].append([start_time, end_time])
                current_time = end_time 
                scheduled = True

        # if no tasks were scheduled in this iteration, incriment time
        if not scheduled:
            current_time +=1
        if current_time > runtime:
            break

    return output, algorithm_name




def fcfs_period(processes, runtime):
    algorithm_name = "First Come First Serve (FCFS)"
    n = len(processes['arrival'])
    output = [[] for _ in range(n)]
    current_time = 0 
    scheduled = None
    periods = processes['period']
    next_arrival = processes['arrival'].copy()
    running_task = None

    while current_time < runtime:
        scheduled = False
        for i in range(n):
            # check if task has arrived and if it's time to run the next instance of the task
            if next_arrival[i] <= current_time and (current_time - next_arrival[i]) % periods[i] == 0:
                # if no task is currently running, schedule the current task
                if running_task is None:
                    # get start time and end time of current task instance
                    start_time = current_time
                    end_time = start_time + processes['execution'][i]

                    # append the instance to the output and update the next arrival time
                    output[i].append([start_time, end_time])
                    next_arrival[i] += periods[i]
                    running_task = i
                    scheduled = True

        # if a task is currently running, check if it has finished
        if running_task is not None:
            # if the current task has finished, update the running task to None
            if current_time == output[running_task][-1][1]:
                running_task = None

        # if no tasks were scheduled in this iteration, increment time
        if not scheduled:
            current_time += 1

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
            gantt_chart.text((start_time + end_time)/2, 0.25, f"T{i+1}", ha="center", va="center")
    gantt_chart.set_xlim(0, end_time)
    plt.show()

output, algorithm_name = fcfs(fcfs_processes, runtime)
print(output)
gantt_chart(output, algorithm_name)





