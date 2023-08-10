import random 

user_trys = []     #список пользовательских попыток
random_number = random.randint(1, 100)    # Генерация случайного числа
count = 0  #Переменная счета кол-ва попыток 

def start_game(answer):
    if answer == 'yes':
        return game_logic()
    else:
        print('Bye')


def game_logic():
    tries  = input('Enter your number: ')
    while int(tries) != random_number:
        user_trys.append(tries)
        tries  = input('Enter your number: ')
    print('You win')

print(random_number)
start_game(input('Are you ready to play my game?: '))
