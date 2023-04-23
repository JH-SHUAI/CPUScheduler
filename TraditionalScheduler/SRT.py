"""
Shortest Remaining Time Algorithm - preemptive

Group Members: Han Zhou 20096862
Tingzhou Jia 20130800
Yilin Zhou 20100336
"""
import copy


def process(process_info: dict, total_burst_time: int) -> list:
    solution = []

    i = 0
    current_process = 0
    process_info_copy = copy.deepcopy(process_info)
    keys = list(process_info.keys())
    while i < total_burst_time:
        solution.append(current_process)
        process_info_copy[current_process][0] -= 1
        shortest_remaining_time = process_info_copy[current_process][0]
        for process in keys:
            if 0 < process_info_copy[process][0] < shortest_remaining_time and process_info_copy[process][1] <= i or \
                    shortest_remaining_time <= 0:
                current_process = process
                shortest_remaining_time = process_info_copy[process][0]
        i += 1

    return solution