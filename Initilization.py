"""
The class will create necessary information for all process

Group members: Han Zhou 20096862
Tingzhou Jia 20130800
Yilin Zhou 20100336
"""
import random


def initializeProcessInfo(num_process, total_burst_time):
    process_info_dict = {}
    time_left = total_burst_time
    total_burst_time = 0
    for i in range(0, num_process):
        burst_time = random.randint(1, time_left)
        arrival_time = random.randint(0, total_burst_time)  # Make sure there will be at least one process using the timeslot
        process_info_dict.update({i: [burst_time, arrival_time]})
        total_burst_time += burst_time
        time_left -= burst_time
    return process_info_dict
