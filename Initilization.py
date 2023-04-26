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
    process_left = num_process - 1
    burst_time = 0
    arrival_time_upperbound = 0
    for i in range(0, num_process - 1):
        if time_left - process_left <= 1:
            burst_time = 1
        else:
            burst_time = random.randint(1, time_left - process_left)
        arrival_time = random.randint(0, arrival_time_upperbound)  # Make sure there will be at least one process using the timeslot
        process_info_dict.update({i: [burst_time, arrival_time]})
        time_left -= burst_time
        arrival_time_upperbound += burst_time
    process_info_dict.update({num_process - 1: [time_left, random.randint(0, arrival_time_upperbound)]})
    return process_info_dict


# for test purpose only
if __name__ == '__main__':
    print(initializeProcessInfo(4, 20))

