"""
The program will run both GA algorithm and 4 traditional CPU Scheduling methods and comparing
their performance by the average process waiting time

Group members: Han Zhou 20096862
Tingzhou Jia 20130800
Yilin Zhou 20100336
"""
import Initilization
import GASchduler
import TraditionalScheduler


def main(name):
    num_process = 4
    burst_time_limit = 5
    total_burst_time = 20
    # Generate Process Info
    process_info = Initilization.initializeProcessInfo(num_process, total_burst_time)

    # Traditional Methods
    solution_SJF = TraditionalScheduler.SJF.process(process_info, total_burst_time)
    solution_FCFS = TraditionalScheduler.FCFS.process(process_info, total_burst_time)
    solution_RoundRobin = TraditionalScheduler.RoundRobin.process(process_info, total_burst_time)
    solution_SRT = TraditionalScheduler.SRT.process(process_info, total_burst_time)

    # GA Algorithm
    solution_GA = GASchduler.GA_Scheduler.process(total_burst_time, process_info)

    print("SJF: ", GASchduler.evaluation.fitness_turnaround_time(solution_SJF))
    print("FCFS: ", GASchduler.evaluation.fitness_turnaround_time(solution_FCFS))
    print("RoundRobin: ", GASchduler.evaluation.fitness_turnaround_time(solution_RoundRobin))
    print("SRT: ", GASchduler.evaluation.fitness_turnaround_time(solution_SRT))
    print("GA: ", GASchduler.evaluation.fitness_turnaround_time(solution_GA))


main()

