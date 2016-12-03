# #1, 1, 2, 3, 5, 8
# from datetime import datetime

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


start = datetime.now()

def fib(n):
  a, b = 1, 1
  for i in range(n-1):
    print(i)
    a, b = b, a + b
  return a

print(datetime().now - start)
# print(fib(4))
# print('yo')




















