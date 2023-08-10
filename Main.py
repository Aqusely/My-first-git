random_number = 50

def game_logic(count):
    while count != random_number:
        count = int(input('Enter your number: '))
    print('You win')

game_logic(int(input('Enter your number: ')))