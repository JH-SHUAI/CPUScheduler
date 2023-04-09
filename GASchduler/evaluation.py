"""
Evaluate the individual fitness

Group member: Han Zhou 20096862
Tingzhou Jia 20130800
Yilin Zhou 20100336
"""


def fitness_turnaround_time(individual: list, process_info: dict):

    fitness = 0
    size = len(process_info)
    total_turnaround_time = 0

    for i in range(0, size):
        arrival_time = process_info[i][1]
        finish_time = 0
        for j in reversed(range(len(individual))):
            if individual[j] == i:
                finish_time = j
        total_turnaround_time += finish_time - arrival_time

    fitness = 1 / 1 + total_turnaround_time
    return fitness


def fitness_avgwait_time(individual: list, process_info: dict):
    fitness = 0

    return fitness