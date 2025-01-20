import random;

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

emojis = { ROCK: '🪨', SCISSORS: '✂️', PAPER: '📃' }
choices = tuple(emojis.keys())


def getChoices():
    user_choice = input("Rock,paper, scissors? (r,p,s): ").lower()
    if user_choice in choices:
        return user_choice
    else:
        print("Invalid Choice")
        
def displayChoices(computer_choice, user_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

def displayWinner(computer_choice, user_choice):
    if user_choice == computer_choice:
        print("Tie")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or 
        (user_choice == SCISSORS and computer_choice == PAPER) or 
        (user_choice == PAPER and computer_choice == ROCK)):
        print('You win')
    else:
        print('You lose')

def playGame():
    while True:

        user_choice = getChoices()
        computer_choice = random.choice(choices)
        displayChoices(computer_choice,user_choice)
        displayWinner(computer_choice,user_choice)

    
        should_continue = input("Continue?: ").lower()
        if should_continue == 'n':
            break

playGame()

    