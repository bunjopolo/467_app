def fcfs(processes, runtime):
    algorithm_name = "First Come First Serve (FCFS)"
    n = len(processes['arrival'])
    output = [[] for _ in range(n)]
    current_time = 0 
    periods = processes['period']

    while current_time < runtime:
        scheduled = False
        for i in range(n):
            # task not arrived yet, try next task
            if processes['arrival'][i] > current_time:
                continue

            # a task is ready to run
            elif (current_time - processes['arrival'][i]) % periods[i] == 0:
                # get start time and end time of current task instance
                start_time = current_time
                end_time = start_time + processes['execution'][i]

                # add task instance to output
                output[i].append([start_time, end_time])
                current_time = end_time 

                # increment period of current task to set new deadline for next instance
                processes['period'][i] += periods[i]
                scheduled = True

        # if no tasks were scheduled in this iteration, increment time
        if not scheduled:
            current_time += 1

    return output, algorithm_name