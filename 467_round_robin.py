import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

tasks = [1, 3, 6, 8]

def round_robin(tasks, quantum):
    colors = [f"#{random.randint(0, 0xFFFFFF):06x}" for _ in range(len(tasks))]
    time = 0

    fig, gantt_chart = plt.subplots()
    gantt_chart.set_title("First Come First Serve (FCFS)")
    gantt_chart.set_xlabel("Time")
    gantt_chart.set_yticks([0])
    gantt_chart.set_yticklabels([""])
    gantt_chart.grid(True)
    


    for i in range(sum(tasks)):
        start_time = time
        tasks[i] -= quantum
        time += quantum
        end_time = time
        gantt_chart.broken_barh([(start_time, end_time - start_time)], (0, 0.5))

    gantt_chart.set_xlim(0, time)
    plt.show()

round_robin(tasks, 2)
