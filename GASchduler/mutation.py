"""
individual mutation

Group member: Han Zhou 20096862
Tingzhou Jia 20130800
Yilin Zhou 20100336
"""
import random


def mutate(individual: list, process_info: dict) -> list:
    mutant = permutation_swap(individual)

    return mutant


def permutation_swap(individual: list, process_info: dict) -> list:
    size = len(individual)

    index1 = random.randint(0, size - 1)
    index2 = random.randint(0, size - 1)

    process1 = individual[index1]
    process2 = individual[index2]
    arrival_time1 = process_info[process1][1]
    arrival_time2 = process_info[process2][1]

    if index1 < arrival_time2 or index2 < arrival_time1:
        permutation_swap(individual, process_info)

    mutant = individual.copy()

    mutant[index1] = individual[index2]
    mutant[index2] = individual[index1]

    return mutant
