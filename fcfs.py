import queue

#phase, period,execution time, deadline
processes = [[0,4,3,4], [1,3,1,3], [2,10,2,10]]
runtime = 20


def fcfs(processes):
    dl_missed = []
    n = len(processes)
    output = []
    current_time = 0 

    #add items to the queue
    q = queue.Queue()
    for i in range(len(processes)):
        q.put(processes[i])


    #run algorithm for the given runtime
    while current_time < runtime:
        
        #get the first item in the queue
        task = q.get()

        #if current time is less than the phase of the process then move to the next process in the queue 
        if current_time < task[0]:
            q.put(task)
            current_time += 1
            continue

        if current_time%task[1] == 0:


        #if the current time is greater than the phase of the process then run the process
        start_time = current_time
        end_time = start_time + task[1]

        else
        
