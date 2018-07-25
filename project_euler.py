# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
import time
x_start = time.time()

def powers(pow):
  added = 0
  
  
  for idx in range(pow+1):
    # print(idx)
    added += idx**idx
  # length_of_num = len(last_ten_digits) - 10

  # return last_ten_digits[length_of_num:]
  last_ten_digits = (str(added))
  a = last_ten_digits[(len(last_ten_digits)-10):]
  # return len(a)
  return a


print(powers(1000))

print(time.time() - x_start)
# num = 132
# ar = [int(x) for x in str(num)]
# summed = 0
# for x in ar:
#   summed = summed + x
# print(summed)
# print(ar)