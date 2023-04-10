"""
Round Robin Algorithm - preemptive

Group Members: Han Zhou 20096862
Tingzhou Jia 20130800
Yilin Zhou 20100336
"""
import random


def process(process_info: dict, total_burst_time: int) -> list:
    solution = []

    i = 0
    current_process = 0
    process_info_copy = process_info.copy()
    while i < total_burst_time:
        solution.append(current_process)
        process_info_copy[current_process][0] -= 1
        for process in random.shuffle(process_info_copy.keys()):
            if process != current_process and process_info_copy[process][0] > 0 and process_info_copy[process][1] <= i:
                current_process = process
                break
        i += 1

    return solution