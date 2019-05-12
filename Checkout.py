"""
Alexander Urbanyak
CS4720(01)
Created: 02-16-2019
Python 3.6
"""

# program simulates checkout at supermarket
# By default:
# simulation length is 60 seconds
# process 1st customer every second
# customer is generated every 2 seconds
# max queue size is 5
# screen clear is cross-platform, effect only visible in shell

from threading import Thread
import time
from random import randint
import os


# process customer every second
def process():
    # wait if there are no customers in a queue
    if len(queue) == 0:
        time.sleep(2)

    while time.time() < simulation_time:
        time.sleep(1)
        # clear screen effect only visible in shell
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Checkout: " + str(wait_time)[1:-1])
        wait_time[0] -= 1
        if wait_time[0] == 0:
            del wait_time[0]
            del queue[0]
            # print("customer checked out ")


# generate customer every T2 seconds
def customer():

    while time.time() < simulation_time:
        time.sleep(T2)
        # customer is a thread object
        c = Thread()
        # generate processing time for a customer
        processing_time = randint(1, 30)
        # customer will join the queue if there are less that R customers in a queue
        # will leave otherwise
        if len(queue) < R:
            queue.append(c)
            wait_time.append(processing_time)


if __name__ == '__main__':
    # checkout queue
    queue = []
    # integer sequence to record remaining wait time for each customer
    wait_time = []
    # simulation length (60 = 60 seconds)
    T1 = 60
    simulation_time = time.time() + T1
    # generate customer every T2 seconds
    T2 = 2
    # how many customers are allowed to be in a queue
    R = 5
    # thread generates a new customer every T2 seconds
    Thread1 = Thread(target=customer, args=())
    # thread runs every second to simulate checking out process
    Thread2 = Thread(target=process, args=())
    Thread1.start()
    Thread2.start()
