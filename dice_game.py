import random;

while True:

    choice = input("Roll the dice (Y/N): ").lower()

    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'Output: ({die1},{die2})')
        # break
    elif choice == 'n':
        print("Thank you message")
        break
    else:
        print("Invalid choice")
        break
        