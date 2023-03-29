def fcfs(processes, runtime):
    """
    First Come First Serve (FCFS) Scheduling Algorithm
    """
    n = len(processes['arrival'])
    output = [[] for _ in range(n)]
    current_time = 0 


    while current_time <= runtime:

        scheduled = False
        for i in range(n):
            #task not arrived yet try next task
            if processes['arrival'][i] > current_time:
                continue
            #a task is ready to run
            elif processes['arrival'][i] <= current_time:
                #get start time and end time of current task instance
                start_time = current_time
                if start_time + processes['execution'][i] > runtime:
                    end_time = runtime 
                    output[i].append([start_time, end_time])
                    return output
                else:
                    end_time = start_time + processes['execution'][i]
                    #add task instance to output
                    output[i].append([start_time, end_time])
                print(output)
                current_time = end_time
                #indicate that a task was scheduled in this iteration 
                scheduled = True
        # if no tasks were scheduled in this iteration, incriment time
        if not scheduled:
            current_time +=1
    return output



def fcfs_periodic(processes, runtime):
    """
    First Come First Serve (FCFS) Scheduling Algorithm for Periodic Tasks
    """
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


def rr(processes, runtime):
    n = len(processes['arrival'])
    output = [[] for _ in range(n)]
    current_time = 0
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
                        
                else:
                    end_time = start_time + processes['quantum']
                    processes['execution'][i] -= processes['quantum']
                    output[i].append([start_time, end_time])
                    current_time = end_time
                schueduled = True
            
        if not schueduled:
            current_time += 1
    return output