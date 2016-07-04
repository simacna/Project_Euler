""" The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

# def isPrime(n):
#   if ((int(n**0.5)+1)):
#     print (int(n**0.5)+1)
#     return True

# print isPrime(8)


def isprime(n):
    '''check if integer n is a prime'''

    # make sure n is a positive integer
    n = abs(int(n))

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2: 
        return True    

    # all other even numbers are not primes
    if not n & 1: 
        return False

    # range starts with 3 and only needs to go up 
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True

# print isprime(7)

def sums(n):
  summed_primes = []
  for idx in range(n):
    if idx < n and isprime(idx):
      summed_primes.append(idx)
  return summed_primes

print(sums(10))






