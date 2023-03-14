import random
import matplotlib.pyplot as plt


#arrival time, period,execution time
#fcfs_processes = [[3,2,3], [0,4,1]]


##############################T1#T2#############T1#T2################T1#T2########...etc
fcfs_processes = {'arrival': [0, 4], 'period': [4, 5], 'execution': [2, 1], 'deadline': None}

#output_format = [[['t1_start_1','t1_end_1'],['t1_start_2','t1_end_2']], [['t2_start_1','t2_end_1'],['t2_start_2','t2_end_2']]] 


runtime = 30


def fcfs(processes, runtime):
    algorithm_name = "First Come First Serve (FCFS)"
    dl_missed = []
    n = len(processes['arrival'])
    print(n)
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


            

        print(output)
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
gantt_chart(output, algorithm_name)





