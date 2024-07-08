import random

def get_numbers_ticket(min, max, quantity):

    if min >= 1 and max <= 1000 and min < max and quantity < (max - min + 1):

        random_numbers = random.sample(range(min, max + 1), quantity)
        
        random_numbers.sort()
    
        return (f"Ваші лотерейні числа: {random_numbers}")
    else:
        return ("Invalid parameters")

lottery_numbers = get_numbers_ticket(1, 1000, 6)
print(lottery_numbers)
