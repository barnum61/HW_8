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
"""
Конфлікт виник через те, що різні процедури одного модуля були створені в різних
гілках. При злитті гілок виникла невизначеність, яку процедуру включити в гілку master.
В цьому випадку обидві процедури залишаємо, і так вирішуємо конфлікт.
тому 
"""
<<<<<<< HEAD
def minus_one(num):
    num -= 1
    print(num)
    if num > 0:
        minus_one(num)
=======
def test_finction():
    print("My name is ...")
>>>>>>> test
