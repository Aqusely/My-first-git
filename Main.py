import random 

gues_number = random.randint(1, 100)

def start_game(answer):
    if answer == 'yes':
        while input() != gues_number:
            input()
        else:
            return 'You win'
    else:
        return 'Bye'

    
    
print(start_game(input('Are you ready to play my game?: ')))