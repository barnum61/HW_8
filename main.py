import random

def main_function():

    upper_bound = 100
    lower_bound = 1
    to_be_guessed = random.randint(lower_bound, upper_bound)
    
    for i in range(6):
        guess = int(input("нове число: "))    
        if guess < lower_bound or guess > upper_bound:
            print("число за межами діапазону!")
            continue
        if guess == to_be_guessed:
            print('число вгадане з {} спроби'.format(i+1))
            break
        elif guess < to_be_guessed:
            print('ваше число меньше завданого')                
            lower_bound = guess + 1
        elif guess > to_be_guessed:
            print('ваше число більше завданого')                
            upper_bound = guess - 1
    else:
        print('спроба невдала')
