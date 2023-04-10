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
    individual.extend(repeat(0, total_burst_time))
    process_num = len(process_info)
    for i in range(0, process_num):
        left_burst_time = process_info[i][0]
        arrival_time = process_info[i][1]
        while left_burst_time > 0:
            individual = assign_timeslot(individual, process_info, i, arrival_time, total_burst_time)
            left_burst_time -= 1
    return individual


""" 
Recursively assign timeslot to current process until a legal timeslot is found
"""


def assign_timeslot(individual: list, process_info: dict,
                    process_num: int, arrival_time: int, total_burst_time: int) -> list:
    index = random.randint(arrival_time, total_burst_time)
    if individual[index] == 0:
        individual[index] = process_num
    else:
        current_process_num = individual[index]
        current_process_arrival_time = process_info[current_process_num][1]
        if arrival_time > current_process_arrival_time:
            individual[index] = process_num
            individual = assign_timeslot(individual, process_info, current_process_num, current_process_arrival_time,
                                         total_burst_time)
        else:
            individual = assign_timeslot(individual, process_info, process_num, arrival_time, total_burst_time)
    return individual
