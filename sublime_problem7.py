"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

	"""

def prime(n):
	maxNumber = n
	numberOfPrimes = 0


	while maxNumber > numberOfPrimes:
		print numberOfPrimes

def isPrime(n):
	start = 0
	for i in range(1,n):
		if (n%i) ==0:
			print "not a prime"


def isPrime(highNumber):
	prime = 2
	counter = 0
	while maxPrime > counter:
		for i in range(2,10000000):
			if (n%i) == 0:
				counter += 1
				prime = i 
	return counter
