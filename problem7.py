# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def prime(n):
	currentHighestPrime = 2

	for i in range(2,n):
                print i 
		if (n%i) == 0:
			if i > currentHighestPrime:
				currentHighestPrime = i
                return currentHighestPrime

# 7/25 - Below is my rough work to solve problem number 7:

# First let me implement a counter function:

def whil(n):
    counter = 0
    while n > counter:
        for idx in range(n):
            counter += 1
            print idx
    return counter

# Next write a function that is both a counter function and acts as to see if the iterator is even, if so append to a list

def whil(n):
    counter = 0
    events = []
    while n > counter:
        for idx in range(2, n):
            if idx%2 == 0:
               events.append(idx)
            counter += 1
            print idx
    return events, counter