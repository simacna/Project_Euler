def collatz(num):
    '''
    Calculates the longest sequence of steps to reach one
    in a Collatz sequence
    '''
    steps = 0
    number = num
    limit = 0
    while limit < 10:
        while number > 1:
         
         if (number % 2 == 0):
          number = (number / 2)
          steps += 1
         else:
          number =  3*(number) + 1
          steps += 1
    limit += 1
        
    return steps + 1, "steps"

		
		
	
