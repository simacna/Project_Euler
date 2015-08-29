# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Even with the above condition, c2 must == 1000, hence a2 + b2 = 1000 = c2. Hm how to use this to solve the problem more efficiently

import math

def pythtrip(a,b,c=100):

	temp = 0
	if (a+b+c == 1000):
		if (math.pow(a,2) && math.pow(b,2) == math.pow(c,2)):
			temp = a*b*c

	return temp


