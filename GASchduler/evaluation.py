"""
Evaluate the individual fitness, sometimes illegal individual will occasionally exist. the violation checker will detect
it and set fitness to 0 as the punishment for the violation

Group member: Han Zhou 20096862
Tingzhou Jia 20130800
Yilin Zhou 20100336
"""


def fitness_turnaround_time(individual: list, process_info: dict) -> int:
    size = len(process_info)
    total_turnaround_time = 0
    fitness = 0
    if check_violation(individual):
        return fitness
    else:
        for process in range(0, size):
            arrival_time = process_info[process][1]
            finish_time = 0
            for j in reversed(range(len(individual))):
                if individual[j] == process:
                    finish_time = j
                    break
            total_turnaround_time += finish_time - arrival_time
        try:
            fitness = 1 / (1 + total_turnaround_time)
        except ZeroDivisionError:
            print("turnaround time: ", total_turnaround_time)
            fitness = 0
    return fitness


def fitness_avgwait_time(individual: list, process_info: dict):
    size = len(process_info)
    total_waiting_time = 0
    fitness = 0
    if check_violation(individual):
        return fitness
    else:
        for process in range(0, size):
            arrival_time = process_info[process][1]
            burst_time = process_info[process][0]
            finish_time = 0
            for j in reversed(range(len(individual))):
                if individual[j] == process:
                    finish_time = j
                    break
            total_waiting_time += finish_time - arrival_time - burst_time
        try:
            fitness = 1 / (1 + (total_waiting_time / size))
        except ZeroDivisionError:
            print("turnaround time: ", total_waiting_time)
            fitness = 0
    return fitness


def check_violation(individual: list) -> bool:
    for slot in individual:
        if slot == -1:
            return True
    return False




