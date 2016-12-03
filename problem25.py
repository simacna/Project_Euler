# #1, 1, 2, 3, 5, 8
# from datetime import datetime
import time
# def fib(n):
#   if n > 1:
#     return ()

# print(fib(3))

# gen = (x for x in range(3))
# print(type(gen))

# # for idx in gen:
# #   print(idx)

# li = [x for x in range(3)]
# # for _ in li:
#   # print(_)


start = time.clock()

def fib(n):
  c = 0
  a, b = 1, 1
  for i in range(n-1):
    # print(i)
    a, b = b, a + b
    c = b
    if len(str(c)) == 3:
      return c
    print("this is c", )
  return a #4e-6
# print(fib(3))

# def fibb(): runs into timeout error
#   c = 0
#   a, b = 1, 1
#   while(len(str(3)) < 2):
#     print(cß)
#     a = b
#     b = b+a
#     c = b
#   return c
# print(fibb())


# def fibR(n):
#   if n>2:
#     n-1
#     return fibR()
# print(time.clock() - start)
# print(fib(4))
# print('yo')




















