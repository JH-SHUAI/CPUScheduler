"""
parent selection

Group member: Han Zhou 20096862
Tingzhou Jia 20130800
Yilin Zhou 20100336
"""
import random


def tournament_selection(fitness: list, mating_pool_size: int, tournament_size: int) -> list:
    selected_to_mate = []

    population_size = len(fitness)
    current_member = 0
    while current_member < mating_pool_size:
        candidates = []
        individuals = list(range(population_size))
        # Pick k individuals randomly without replacement
        for k in range(tournament_size):
            individual = random.choice(individuals)
            candidates.append(individual)
            individuals.remove(individual)

        winner = candidates[0]
        # Select the best of k individuals
        for candidate in candidates:
            winner = candidate if fitness[candidate] > fitness[winner] else winner
        selected_to_mate.append(winner)
        current_member += 1

    return selected_to_mate
