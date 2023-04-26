"""
Shortest Job First Algorithm - non preemptive

Group Members: Han Zhou 20096862
Tingzhou Jia 20130800
Yilin Zhou 20100336
"""
import copy
import sys
import numpy

def process(process_info: dict, total_burst_time: int) -> list:
    solution = []
    i = 0
    process_info_copy = copy.deepcopy(process_info)
    while i < total_burst_time:

        # check all available process to see which one has the shortest burst time
        keys = list(process_info_copy.keys())
        shortest_process = 0
        shortest_time = sys.maxsize
        for process in process_info_copy.keys():
            if process_info_copy[process][1] <= i and process_info_copy[process][0] <= shortest_time:
                shortest_process = process
                shortest_time = process_info_copy[process][0]
        solution.extend(numpy.repeat(shortest_process, shortest_time))
        i += shortest_time
        process_info_copy.pop(shortest_process)

    return solution
