import random 

user_tries = []
random_number = random.randint(1, 100)    # Генерация случайного числа

def hints(our_number):
    if random_number > our_number:
        return f'Guess number > {our_number}'
    else:
        return f'Guess number < {our_number}'


def start_game(answer):
    if answer == 'yes':
        return game_logic(int(input('Enter your number: ')))
    else:
        print('Bye')


def game_logic(guess):

    count = 0   #Число попыток 
    while guess != random_number:
        guess = input('Enter your number: ')
        if guess == 'hints' or guess == 'h':
            print(hints(user_tries[-1]))
        else:
            count += 1
            user_tries.append(guess)

    

print(random_number)
start_game(input('Are you ready to play my game?: '))
