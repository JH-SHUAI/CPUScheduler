"""
Initialize the first generation

Group member: Han Zhou 20096862
Tingzhou Jia 20130800
Yilin Zhou 20100336
"""
import random
from itertools import repeat


def initialize(popsize: int, total_burst_time: int, process_info: dict) -> list:
    population = []

    for i in range(0, popsize):
        population.append(generate_individual(total_burst_time, process_info))

    return population


def generate_individual(total_burst_time: int, process_info: dict) -> list:
    individual = []
    individual.extend(repeat(-1, total_burst_time))
    process_num = len(process_info)
    for i in range(0, process_num):
        left_burst_time = process_info[i][0]
        arrival_time = process_info[i][1]
        while left_burst_time > 0:
            individual = assign_timeslot(individual, process_info, i)
            left_burst_time -= 1
    return individual


""" 
Recursively assign timeslot to current process until a legal timeslot is found
"""

def assign_timeslot(individual: list, process_info: dict, process_num: int) -> list:
    arrival_time = process_info[process_num][1]
    index = random.randint(arrival_time, len(individual) - 1)
    if individual[index] == -1:
        individual[index] = process_num
    else:
        available_timeslots = find_available_timeslot(individual, arrival_time)
        if len(available_timeslots) != 0:
             index = random.choice(available_timeslots)
             individual[index] = process_num
        else:
            process_tradeoff = find_earlier_process(process_info, individual, process_num)
            for process in process_tradeoff:
                available_tradeoff_timeslots = find_tradeoff_timeslots(find_available_timeslot(individual, process_info[process][1]), arrival_time)
                if len(available_tradeoff_timeslots) > 0:
                    switch_index = random.choice(available_tradeoff_timeslots)
                    index = random.choice(find_process_indexes(individual, arrival_time, len(individual), process))
                    individual[index] = process_num
                    individual[switch_index] = process
                    break
    return individual


def find_process_indexes(individual: list, lower_bound: int, upper_bound: int, process: int) -> list:
    indexes = []
    for i in range(lower_bound, upper_bound):
        if individual[i] == process:
            indexes.append(i)
    return indexes

def find_tradeoff_timeslots(timeslot: list, upper_bound: int) -> list:
    indexes = []
    for slot in timeslot:
        if upper_bound > slot:
            indexes.append(slot)
    return indexes


def find_available_timeslot(individual: list, lower_bound: int) -> list:
    indexes = []
    for i in range(len(individual)):
        if individual[i] == -1 and i >= lower_bound:
            indexes.append(i)
    return indexes


def find_earlier_process(process_info: dict, individual: list, process_num: int) -> list:
    earlier_process = []
    arrival_time = process_info[process_num][1]
    for i in range(arrival_time, len(individual)):
        process = individual[i]
        if process != process_num and process_info[process][1] < arrival_time and process not in earlier_process:
            earlier_process.append(process)
    return earlier_process

# for test purpose only
if __name__ == '__main__':
    process_info_1 = {0: [15, 0], 1: [2, 5], 2: [1, 13], 3: [2, 11]}
    process_info_2 = {0: [1, 0], 1: [1, 1], 2: [3, 2], 3: [15, 4]}
    process_info_3 = {0: [17, 0], 1: [1, 11], 2: [1, 2], 3: [1, 18]}
    initialize(10, 20, process_info_3)