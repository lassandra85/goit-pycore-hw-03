import random

def get_numbers_ticket(min, max, quantity):

    correct_number = min < 1 or max > 1000 or quantity < 1 

    if correct_number: 
        return []
    else:
        random_numbers = random.sample(range(min, max + 1), quantity)
    
        return sorted(random_numbers)
   


print( "Ваші лотерейні числа:", get_numbers_ticket(1, 1000, 10))

