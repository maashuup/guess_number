from random import randint
number = randint(1,100)
print('Угадайте число от 1 до 100')
while True: 
    quess = int(input('Введите число: '))

    if quess < number:
        print('Ваше число меньше того, что загадано.')

    elif quess > number:
        print('Ваше число больше того, что загадано.')

    else:
        print('Отличная интуиция! Вы угадали число :)')
        break