import random;

guess_a_number = random.randint(1, 100)

while True:

    try:
        choice = int(input("Guess a number between 1 and 100: "))
        
        if choice < guess_a_number:
            print('Too low')
        elif choice > guess_a_number:
            print('Too high')
        else:
            print("Congradulations you guessed a number")
    except ValueError:
        print('enter a valid number')