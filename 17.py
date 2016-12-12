dict = {0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'}

dict = {0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'}

def number_letters(num):
    a = 0
    for idx in range(num):
        b = [int(i) for i in str(idx)]
        count = 0
        for _ in b:
            count += len(str(_)) #zero, one, two
        print(count)

        

number_letters(11)



