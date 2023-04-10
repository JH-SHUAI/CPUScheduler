"""
The class will execute GA Algorithm

Group member: Han Zhou 20096862
Tingzhou Jia 20130800
Yilin Zhou 20100336
"""
import random
import population
import evaluation
import parent_selection
import survivor_selection
import crossover
import mutation


def process(total_burst_time: int, process_info: dict) -> list:
    # Parameters
    pop = []
    pop_size = 10
    mating_pool_size = int(pop_size * 0.5)  # has to be even
    tournament_size = 4
    xover_rate = 0.9
    mut_rate = 0.2
    gen = 0
    gen_limit = 10

    # First generation
    pop = population.initialize(pop_size, total_burst_time, process_info)
    fitness = []

    # evaluate first generation
    for i in range(0, pop_size):
        fitness.append(evaluation.fitness_turnaround_time(pop[i], process_info))
        # fitness.append(evaluation.fitness_avgwait_time(pop[i], process_info))
    print("generation", gen, ": best fitness", max(fitness), "\taverage fitness", sum(fitness) / len(fitness))

    # evolution
    while gen < gen_limit:
        parents_index = parent_selection.tournament_selection(fitness, mating_pool_size, tournament_size)
        random.shuffle(parents_index)

        offspring = []
        offspring_fitness = []
        i = 0  # initialize the counter for parents in the mating pool

        # offspring are generated using selected parents in the mating pool
        while len(offspring) < mating_pool_size:
            if random.random() < xover_rate:
                off1, off2 = crossover(pop[parents_index[i]], pop[parents_index[i + 1]])
            else:
                off1 = pop[parents_index[i]].copy()
                off2 = pop[parents_index[i + 1]].copy()

            # mutation
            if random.random() < mut_rate:
                off1 = mutation.mutate(off1, process_info)
            if random.random() < mut_rate:
                off2 = mutation.mutate(off2, process_info)

            offspring.append(off1)
            offspring_fitness.append(evaluation.fitness_turnaround_time(off1))
            offspring.append(off2)
            offspring_fitness.append(evaluation.fitness_turnaround_time(off2))
            i = i + 2  # update the counter

        pop, fitness = survivor_selection.mu_plus_lambda(pop, fitness, offspring, offspring_fitness)

    # return the best individual
    for i in range(0, pop_size):
        if fitness[i] == max(fitness):
            return pop[i]
