#1, 1, 2, 3, 5, 8

def fib(n):
  if (n > 0):
    return(n*fib(n-1))

# print(fib(3))

gen = (x for x in range(3))
print(type(gen))

# for idx in gen:
#   print(idx)

li = [x for x in range(3)]
# for _ in li:
  # print(_)


