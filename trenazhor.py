import random

alph = 'abcefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ1234567890   '
health = 100
MISTAKE = 10
input_string = ''

while input_string != 'EXIT' and health > 0:
    tmp = alph[random.randint(0, 61)]
    print(tmp + '   ' + str(health))
    input_string = input()
    
    if input_string == tmp:
        print('Ok!')
    else:
        print('Wrong answer!')
        health -= MISTAKE

if health <= 0:
    print('Game Over!')