"""
The program will run both GA algorithm and 4 traditional CPU Scheduling methods and comparing
their performance by the average process waiting time

Group members: Han Zhou 20096862
Tingzhou Jia 20130800
Yilin Zhou 20100336
"""
import Initilization
import GASchduler
from GASchduler import evaluation, GA_Scheduler
from TraditionalScheduler import SJF
from TraditionalScheduler import FCFS
from TraditionalScheduler import RoundRobin
from TraditionalScheduler import SRT
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    num_process = 3
    burst_time_limit = 5
    total_burst_time = 20
    # Generate Process Info
    process_info = Initilization.initializeProcessInfo(num_process, total_burst_time)
    rounds = 5
    round = 0

    performance_GA = 0;
    performance_SJF = 0;
    performance_FCFS = 0;
    performance_RoundRobin = 0;
    performance_SRT = 0
    while round < rounds:
        # Traditional Methods
        solution_SJF = SJF.process(process_info, total_burst_time)
        solution_FCFS = FCFS.process(process_info, total_burst_time)
        solution_RoundRobin = RoundRobin.process(process_info, total_burst_time)
        solution_SRT = SRT.process(process_info, total_burst_time)

        # GA Algorithm
        solution_GA = GA_Scheduler.process(total_burst_time, process_info)

        # fitness evaluation
        performance_GA += evaluation.fitness_turnaround_time(solution_GA, process_info)
        performance_SJF += evaluation.fitness_turnaround_time(solution_SJF, process_info)
        performance_FCFS += evaluation.fitness_turnaround_time(solution_FCFS, process_info)
        performance_RoundRobin += evaluation.fitness_turnaround_time(solution_RoundRobin, process_info)
        performance_SRT += evaluation.fitness_turnaround_time(solution_SRT, process_info)

        round += 1
    # raw data
    print("GA: ", performance_GA)
    print("SJF: ", performance_SJF)
    print("FCFS: ", performance_FCFS)
    print("RoundRobin: ", performance_RoundRobin)
    print("SRT: ", performance_SRT)

    # data visualization
    performance_list = [performance_GA / rounds, performance_SJF / rounds, performance_FCFS / rounds,
                        performance_RoundRobin / rounds, performance_SRT / rounds]
    algorithms = ["GA", "SJF", "FCFS", "RoundRobin", "SRT"]

    plt.bar(algorithms, performance_list)
    plt.xlabel("Algorithms")
    plt.ylabel("Performance(fitness)")
    plt.title("Algorithm Comparison after {} rounds".format(rounds))
    plt.show()


main()
