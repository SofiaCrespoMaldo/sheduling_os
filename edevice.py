# Sofia I. Crespo Maldonado

# Embedded Devices

from pickle import TRUE
import sys
from random import randint
from this import s
from threading import Thread
import time
import socket

from scheduler import N

buffersize = 1024
N = 10				 # Total number of messages allowed

def main():
	id = int(sys.argv[1])
	HOST = sys.argv[2] # The remote host
	PORT = int(sys.argv[3]) # The same port as used by the server
	serverHostPort = (HOST, PORT)

	# Create a UDP socket at client side
	UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

	while(TRUE):
		job_time = randint(1,5) # Generate job time randomly
		msg = "%s:%s"%(id, job_time)    # Format the message
		t = randint(1,5) # Generate random sleeping time

		# Send to server using created UDP socket
		UDPClientSocket.sendto(msg.encode('utf-8'), serverHostPort)

if __name__ == "__main__":
    main()
