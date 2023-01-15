Sofia I. Crespo Maldonado
CCOM4017: Operating Systems
Assignment 02: Threads and Scheduling

Program Description

	This program simulates a Shortest Job First scheduling algorithm for
	a distributed system of embedded devices and a central computer server.

	- embedded devices (edevice.py): generates the ID and time it would
	take for the job to be completed on the CPU. The message will be 
	sent to the server in the format ID:job and the device will sleep for
	a short random amount of time between sends.
	- computer server (escheduler.py): this is divided in two threads, the
	producer receives the messages from the devices and places them in a 
	queue sorted by Shortest Job First, the consumer removes the chosen 
	message from the queue, accumulate in a table the amount of time each
	device spent in the queue and sleep the time that it extracted from the
	queue.

	The variable N in both files represent the amount of messages to send to the queue.

Execution Instructions

	After downloading both files, open a terminal window and traverse to the directory where
	the files are stored. Get the devices running by opening a window for each one, and then run the scheduler.

	Example to run server: python scheduler.py localhost 4017
	Example to run device: python edevice.py 2 localhost 4017

	

Additional References
- Sorting Lists in Python https://towardsdatascience.com/sorting-lists-in-python-31477e0817d8
- Python List/Array Methods https://www.w3schools.com/python/python_ref_list.asp