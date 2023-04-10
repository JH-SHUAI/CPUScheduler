"""
Adjusted Order Crossover fit for specific CPU Scheduling Problem to avoid violation

Group member: Han Zhou 20096862
Tingzhou Jia 20130800
Yilin Zhou 20100336
"""

import random


def permutation_order(parent1: list, parent2: list) -> list:
    offspring1 = []
    offspring2 = []

    size = len(parent1)
    index1 = random.randint(0, size - 1)
    index2 = random.randint(index1, size - 1)

    offspring1 += parent1[index1:index2 + 1]
    offspring2 += parent2[index1:index2 + 1]

    return copy_second_parent(offspring1, parent2, index1, index2), \
           copy_second_parent(offspring2, parent1, index1, index2)


def copy_second_parent(offspring: list, parent: list, index1: int, index2: int) -> list:
    index_taken = []
    size = len(parent)
    leftover = size - 1 - index2
    start = 0
    for element in offspring:
        for i in range(size):
            if i in index_taken:
                continue
            if parent[i] == element:
                index_taken.append(i)
                break

    for i in range(index2, size):
        if i not in index_taken:
            if leftover == 0:
                offspring.insert(start, parent[i])
                start += 1
            else:
                offspring.append(parent[i])
                leftover -= 1
    for i in range(0, index2):
        if i not in index_taken:
            if leftover == 0:
                offspring.insert(start, parent[i])
                start += 1
            else:
                offspring.append(parent[i])
                leftover -= 1

    return offspring
