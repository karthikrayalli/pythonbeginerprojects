import random

def generate_secret():
  digits = list(range(10))
  random.shuffle(digits)
  return ''.join([str(digit) for digit in digits[:4]])


def main():
  secret = generate_secret()
  print('I have generated a 4-digit number with unique digits. Try to guess it!')

  while True:
    guess = input('Guess: ')
      

if __name__ == '__main__':
  main()