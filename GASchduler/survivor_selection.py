"""
survivor selection

Group member: Han Zhou 20096862
Tingzhou Jia 20130800
Yilin Zhou 20100336
"""


def mu_plus_lambda(current_pop: list, current_fitness: list, offspring: list, offspring_fitness: list) -> list:
    population = []
    fitness = []

    mu_num = len(current_pop)
    lambda_num = len(offspring)
    merged_pop = current_pop.copy()
    merged_fitness = current_fitness.copy()
    merged_pop.extend(offspring.copy())
    merged_fitness.extend(offspring_fitness.copy())
    while len(population) < mu_num:
        max_fitness = max(merged_fitness)
        max_fitness_index = merged_fitness.index(max_fitness)
        optimal_individual = merged_pop[max_fitness_index]

        population.append(optimal_individual)
        fitness.append(max_fitness)

        # Remove individual from the merged pop and fitness list
        merged_pop.remove(optimal_individual)
        merged_fitness.remove(max_fitness)

    return population, fitness