# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


l = { 1: 'one',
      2: 'two',
      3: 'three',
      4: 'four',
      5: 'five',
      6: 'six',
      7: 'seven',
      8: 'eight',
      9: 'nine'}

def cal(n):
    string = str(n)
    split = string.split()
    print(split)
    # for idx in range(n):
    #     pass
# print(l[1])
def test(n):
  a = []
  for idx in range(n):
    # a.append(l[idx])
    # print(l[idx])
    print idx
  # return a
  

print(test(3))
        