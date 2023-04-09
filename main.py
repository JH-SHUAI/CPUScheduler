"""
The program will run both GA algorithm and 6 traditional CPU Scheduling methods and comparing
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
    TraditionalScheduler.SJF.process()

    # GA Algorithm
    GASchduler.GA_Scheduler.process()


main()

