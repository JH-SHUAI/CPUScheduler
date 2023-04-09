"""
The class will execute GA Algorithm

Group member: Han Zhou 20096862
Tingzhou Jia 20130800
Yilin Zhou 20100336
"""

import population
import evaluation

def process(total_burst_time: int, process_info: dict) -> list:
    pop = []
    pop_size = 10

    # first generation
    pop = population.initialize(pop_size, total_burst_time, process_info)
    gen = 0
    gen_limit = 10
    fitness = []

    # evaluate first generation
    for i in range(0, pop_size):
        fitness.append(evaluation.fitness_turnaround_time(pop[i], process_info))
        # fitness.append(evaluation.fitness_avgwait_time(pop[i], process_info))
    print("generation", gen, ": best fitness", max(fitness), "\taverage fitness", sum(fitness) / len(fitness))

    # evolution


    return population
