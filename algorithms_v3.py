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
                current_time = end_time
                #indicate that a task was scheduled in this iteration 
                scheduled = True
        # if no tasks were scheduled in this iteration, incriment time
        if not scheduled:
            current_time +=1
    return output



def fcfs_periodic(processes, runtime):
    n = len(processes['arrival'])
    output = [[] for _ in range(n)]
    current_time = 0 
    periods = processes['period']
    next_arrival = processes['arrival'].copy()
    deadlines_missed = [0 for _ in range(n)]

    while current_time <= runtime:
        scheduled = False
        for i in range(n):
            # check if it's time for the task to arrive
            if current_time >= next_arrival[i]:
                # get start time and end time of current task instance
                start_time = max(current_time, next_arrival[i])
                if start_time + processes['execution'][i] > runtime:
                    end_time = runtime 
                    # check if deadline is missed
                    if end_time > next_arrival[i]:
                        deadlines_missed.append('Deadline for task {} missed at time {}'.format(i+1, next_arrival[i]))
                    # add task instance to output
                    output[i].append([start_time, end_time])
                    return output, deadlines_missed
                else:
                    end_time = start_time + processes['execution'][i]
                    # check if deadline is missed
                    if end_time > next_arrival[i]:
                        deadlines_missed.append('Deadline for task {} missed at time {}'.format(i+1, next_arrival[i]))
                    # add task instance to output
                    output[i].append([start_time, end_time])
                current_time = end_time
                next_arrival[i] = start_time + periods[i]
                # indicate that a task was scheduled in this iteration 
                scheduled = True

        # if no tasks were scheduled in this iteration, increment time
        if not scheduled:
            current_time += 1
    return output, deadlines_missed


def rr(processes, runtime):
    n = len(processes['arrival'])
    output = [[] for _ in range(n)]
    current_time = 0
    execution_time = processes['execution'].copy()
    while current_time < runtime:

            #if execution of all tasks are 0 but current time is less than runtime start agaiin
        if all([processes['execution'][i] == 0 for i in range(n)]):
            processes['execution'] = execution_time.copy()

        schueduled = False
        for i in range(n):
            start_time = current_time
            #check if current process has arrived
            if processes['arrival'][i] <= current_time:
                
                #check if current task  has finished
                if processes['execution'][i] == 0:
                    continue

                #check if current iteration finishes task 
                if processes['execution'][i] <= processes['quantum']:

                    #check if the current iteration finishes the task before the runtime cap the task at runtime 
                    if start_time + processes['execution'][i] > runtime:
                        end_time = runtime
                        processes['execution'][i] = 0
                        output[i].append([start_time, end_time])
                        return output
                    
                    #task finishes before runtime
                    else:
                        end_time = start_time + processes['execution'][i]
                        processes['execution'][i] = 0
                        output[i].append([start_time, end_time])
                        current_time = end_time
                
                #task does not finish in this iteration
                else:
                    if start_time + processes['quantum'] > runtime:
                        end_time = runtime
                        processes['execution'][i] -= processes['quantum']
                        output[i].append([start_time, end_time])
                        return output
                    
                    else:
                        end_time = start_time + processes['quantum']
                        processes['execution'][i] -= processes['quantum']
                        output[i].append([start_time, end_time])
                        current_time = end_time
                schueduled = True
        if not schueduled:
            current_time += 1

    return output


def check_deadlines(schedule, deadlines):
    missed = []
    for i in range(len(schedule)):
        for instance in schedule[i]:
            if instance[1] > deadlines[i]:
                missed.append('Deadline for task {} missed at time {}'.format(i+1, deadlines[i]))
                break
    return missed
            

