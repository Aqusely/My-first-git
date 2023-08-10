import random 

random_number = random.randint(1, 100)

def start_game(answer):
    if answer == 'yes':
        game_logic(int(input("Enter your number: ")))
    else:
        print('Bye')
    
def game_logic(count):
    while count != random_number:
        count = int(input('Enter your number: '))
    print('You win')

print(random_number)
start_game(input('Are you ready to play my game?: '))
