"""
First Come First Serve Algorithm - non preemptive

Group Members: Han Zhou 20096862
Tingzhou Jia 20130800
Yilin Zhou 20100336
"""
from itertools import repeat


def process(process_info: dict, total_burst_time: int) -> list:
    solution = []
    fifo_queue = []
    size = len(process_info)
    i = 0
    process_info_copy = process_info.copy()
    for j in range(size):
        earlist_arrival_time = 0
        earlist_process = 0
        for process in process_info_copy.keys():
            if process_info_copy[process][1] <= earlist_arrival_time:
                earlist_arrival_time = process_info_copy[process][1]
                earlist_process = process
        fifo_queue.append(earlist_process)
        process_info_copy.pop(earlist_process)

    for process in fifo_queue:
        solution.extend(repeat(process * process_info[process][0]))



    return solution