import math 

def pythtrip(a, b, c):
    a = [] #just testing to see what a = 40, b = 40 (their addition 40+40 = 80) leading c = 20, i.e. justified
           #in assuming their range will suffice
    b = []
    temp = 0
    while 40 < (range(len(a)) and range(len(b))): 
        a.append(1) and b.append(1)

        if (a + b + c == 1000):
            if (math.pow(a, 2) and math.pow(b, 2) == math.pow(c, 2)):
                temp = a * b * c

    # return temp
    return a, b

print(pythtrip(1,1,1))