# note this project is Python 3
from random import randint
from sys import argv

# these values are inclusive
min = int(input("Minimum bound: "))
max = int(input("Maximum bound: "))
print(randint(min, max))

if "-w" in argv[1:]:
	input("Press any key to exit")
