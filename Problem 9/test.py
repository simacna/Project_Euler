# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


for a in range(1000):
  #print "this is the outter a", a
  # print numbers from 0 to 999
  for b in range(a, 1000 - a):
    #print "this is the inner b", b
   # print numbers from 
    c2 = a**2 + b**2 
    #print "this is c2 printed", c2
    if c2**0.5 == int(c2 ** 0.5):
      if a + b + (c2 ** 0.5)== 1000:
        print "yo"
        print (a*b* int(c2**0.5))