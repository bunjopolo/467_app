import queue

processes = [[0,8], [2,5]]
quantum = 2
q = queue.Queue()

def round_robin(processes, quantum):
    n = len(processes)
    output = []
    current_time = 0
    tmp = 0

    for i in range(len(processes)):
        q.put(processes[i])
    

    while not q.empty():

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
                output.append([start_time, end_time])
                current_time = end_time
            
            else:
                end_time = start_time + quantum
                processes[i][1] -= quantum
                output.append([start_time, end_time])
                current_time = end_time



    return output   
print(round_robin(processes, quantum))

