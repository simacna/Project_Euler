"""
a = []

#have function, for i in range(11) ->remainder of dividing parameter is 0, add


def not_the_best(n):
    global a
    while n < 5000:
        for i in xrange(1,11,1):
            if (n % i == 0):
                a.append(n)
            n += 1
        return a

b = []

def function2(n):
    b = 11
    c = 1

    for b > c:
        if n%c == 0:
            b.app """

def smallestDiv(n):
    
    end=False
    while end == False:
        divisors = [x for x in range(1,11)]    # get divisors
        allDivisions = zip(n % i for i in divisors)    # get values for  n % all integers in divisors
        check = all(item[0]  == 0 for item in allDivisions )   # check if all values of n % i are equal to zero
        if check:         # if all values are equal to zero return n
            end =  True
            return n
        else:             # else increase n by 1
            n +=1
