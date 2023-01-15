# Sofia I. Crespo Maldonado

# Scheduler

import sys
import socket
from threading import Thread, Semaphore
import time

buffersize = 1024                

N = 10                       # Total number of messages allowed
mutex = Semaphore(1)         # controls access to Critical Region
empty = Semaphore(N) ;       # counts empty buffer slots
full = Semaphore(0) ;        # counts full buffer slots
queue = [] * N               # queue for messages received
device_jobs = [0] * (N+1)    # array to accumulate total jobs per device

# Listen to messages from the devices and insert them in a queue
def insert_item(UDPServerSocket):

    # Receive the message from the device
    data = UDPServerSocket.recvfrom(buffersize)
    msg, connection_info = data # Separate the id and time out of the message
    msg = msg.decode('utf-8')   # Change from bytes to string
    data = msg.split(':') # Split the id and job time
    id = int(data[0])
    job = int(data[1])

    # Insert item to queue
    empty.acquire()       # decrement empty
    mutex.acquire()       # enter CriticalReg
    queue.append((id,job))   # Enter new message to the queue
    queue.sort(key=lambda device: device[1])      # Sort according to Shortest Job First
    mutex.release()          # exit CriticalReg
    full.release()          # increment full

# Extract shortest job from queue
def remove_item():
    msg_to_consume = queue[0] # Take the first element in queue as the message to consume
    queue.pop(0) # Remove element from queue
    return msg_to_consume

def consume_item(item): # Accumulates time of jobs on each device
    id = item[0]
    job = item[1]
    device_jobs[id] += job
    time.sleep(job)


def producer():
    HOST = sys.argv[1] # The remote host
    PORT = int(sys.argv[2]) # The same port as used by the server

    # Connects and receives message from device
    # Create a datagram socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Bind to address and ip
    UDPServerSocket.bind((HOST, PORT))

    for i in range(N):   # loop for N messages
        insert_item(UDPServerSocket)

def consumer():
    for i in range(N):
        full.acquire()           # decrement full
        mutex.acquire()         # enter CriticalReg
        item = remove_item()        # Get the message to be consumed and remove from queue
        mutex.release()            # exit CriticalReg
        empty.release()            # increment empty
        consume_item(item)

def main():

    # Create and start running producer and consumer thread
    producer_t = Thread(target=producer)
    consumer_t = Thread(target=consumer)

    producer_t.start()
    consumer_t.start()

    # Join the threads so the program doesn't end without them finishing
    producer_t.join()
    consumer_t.join()

    # Display the amount of time each device consumed in the CPU
    for i in range (N):
        if device_jobs[i] != 0:
            print("Device "+ str(i) + " consumed " + str(device_jobs[i]) + " seconds of CPU time")

if __name__ == "__main__":
    main()
