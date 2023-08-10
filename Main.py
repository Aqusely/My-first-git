import random 

user_tries = []
random_number = random.randint(1, 100)    # Генерация случайного числа

def hints(people_number):
    if people_number < random_number:
        return f'Guess number > {people_number}'
    else:
        return f'Guess number < {people_number}'

def start_game(answer):
    if answer == 'yes':
        print(game_logic())
    else:
        print('Bye')


def game_logic():
    count = 1

    guess = input("Enter your number: ")
    user_tries.append(guess)

    while user_tries[-1] != str(random_number):

        guess = input("Enter your number. If you want you can use hints. Write 'hints' or 'h' for them: ")
        user_tries.append(guess)

        if guess == 'hints' or guess == 'h':
            print(hints(int(user_tries[-2])))
        else:
            count += 1
            user_tries.append(guess)

    return f'You win. You use {count} tries'


print(random_number)
start_game(input('Are you ready to play my game?: '))
