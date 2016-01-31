# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Even with the above condition, c2 must == 1000, hence a2 + b2 = 1000 = c2. Hm how to use this to solve the problem more efficiently
# Not sure how I came up with the above conjecture, that's not the case.. must've been drunk. Removing the default 'c=100' parameter

import math


# def pythtrip(a, b, c):
#     a = [] #just testing to see what a = 40, b = 40 (their addition 40+40 = 80) leading c = 20, i.e. justified
#            #in assuming their range will suffice
#     b = []
#     temp = 0
#     while 40 < (range(len(a)) and range(len(b))): e5821454@telecomitalia.it  UPA8A6WP
#         a.append(1) and b.append(1)
#
#         if (a + b + c == 1000):
#             if (math.pow(a, 2) and math.pow(b, 2) == math.pow(c, 2)):
#                 temp = a * b * c
#
#     # return temp
#     return a, b
#
# print(pythtrip(1,1,1))

# Divergence from the above - now I will write two functions, one in which returns a multi-dimensional array and
# a second which will see if the values in the returned array will equal 1000 ([[9, 16, 25]....] if 3+4+5==10)


def createPyt(desiredLength):
    """Return a multidimensional array - length of array is described by the desiredLength"""
    a = []
    b = []
    c = []
    finalArray = []

    while len(a) < desiredLength:
        for val in range(2000):
            print("this is val at top of for loop", val)
            if math.sqrt(val) == int(val):
                a.append(val)
    return len(a)



def itVals(arrayList, desiredOutput):
    """iterate through the mutli-dimensional array passed and return the value given the specified desired output"""

    pass

print(createPyt(10))

