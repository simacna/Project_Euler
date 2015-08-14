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

# 7/25 - Below is my rough work to solve problem number 7 :

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

#The below function checks if number is prime, replaces highest prime, and has counter -- the only needed addition is a counte
# that checks if it's the 10001st prime

def whil(n):
    highestPrime = 2
    counter = 0
    while n > counter:
        numberOfPrimes = [2,3]
        for idx in range(2, n):
            if (idx%2 != 0 and idx%3 !=0):
               highestPrime = idx
               numberOfPrimes.append(idx)
            counter += 1
            print idx
    return highestPrime, counter, numberOfPrimes


# The below algo returns a list of primes, all placed into an array with the range(2,1000). This is not what the question wanted. But
# there is a discrepency between the question and correct answer. The correct answer to this problem is 547. How is that possible
# since the 10001st prime should at least be... greater than 100001 assuming every n is a prime.

def whil(n):
    highestPrime = 2
    counter = 0
    while n > counter:
        numberOfPrimes = [2,3]
        for idx in range(2, 1000):
            if (idx%2 != 0 and idx%3 !=0):
                highestPrime = idx
                    numberOfPrimes.append(idx)
                counter += 1

return highestPrime,numberOfPrimes

#the below function takes in an input (which prime you'd want, eg 10001st) and returns said number unlike the above which returns all

def factors(n):
    primes = [2]
    cur = 3
    
    while len(primes) < n:
        cur += 2
        
        
        if (cur % 2 == 0):
            continue #this was added later
        for idx in primes:
            print "idx", idx
            if (idx % cur == 0):
                #if (cur % idx == 0):
                break
        else:
            #primes.append(idx)
            primes.append(cur)

else:
    return max(primes)

#The above code doesn't return proper value... let'ss try what we have below, hacking awaya

def whil(n):
    highestPrime = [2,3]
    div = 3
    while n > len(counter):
        div += 2
        
        for idx in range(2, n):
            if (idx%2 != 0 and idx%3 !=0):
               highestPrime = idx
               numberOfPrimes.append(idx)
            counter += 1
            print idx
    return highestPrime, counter, numberOfPrimes
    
print whil(11)



#VICTORY! Good ol' math to the rescue. One can decide if a number is prime if pow(x,y,z)==1
#unanswered question!!!
#there is a discrepency between for example the len(primes) and the actual values of say the first 1000 prime as can be found: https://primes.utm.edu/lists/small/1000.txt
#I don't know why this is

import time

def problem7(n):
    primes = [2,3]
    div = 3
    while n > (len(primes)-1):
        div += 2
        if ( pow(2, div-1, div) == 1):
            primes.append(div)
    return max(primes)
    
print problem7(101)
        
start = time.time()
prime = problem7(101)
elapsed = (time.time() - start)
print "found %s in %s seconds" % (prime,elapsed)











