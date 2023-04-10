"""
Shortest Job First Algorithm - non preemptive

Group Members: Han Zhou 20096862
Tingzhou Jia 20130800
Yilin Zhou 20100336
"""
from itertools import repeat


def process(process_info: dict, total_burst_time: int) -> list:
    solution = []
    i = 0
    process_info_copy = process_info.copy()
    while i < total_burst_time:

        # check all available process to see which one has the shortest burst time
        shortest_process = 0
        shortest_time = 0
        for process in process_info_copy.keys():
            if process_info_copy[process][1] <= i and process_info_copy[process][0] <= shortest_time:
                shortest_process = process
                shortest_time = process_info_copy[process][0]
        solution.extend(repeat(shortest_process * shortest_time))
        i += shortest_time
        process_info_copy.pop(shortest_process)

    return solution
