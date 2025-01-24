from termcolor import colored

X = 'X'
O = 'O'

board = [
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [' ', ' ', ' ']
]

def cell(mark):
  color = 'red' if mark == X else 'green'
  return colored(mark, color)


def get_position(prompt):
  while True:
    try:
      position = int(input(prompt))
      if position < 0 or position > 2:
        raise ValueError
      return position
    except ValueError:
      print('Invalid input!')


def get_move(current_player):
  print(f"Player {current_player}'s turn")
  while True:
    row = get_position('Enter row (0-2): ')
    column = get_position('Enter column (0-2): ')

    if board[row][column] == ' ':
      board[row][column] = current_player
      break
    
    print('This spot is already taken')
        

def main():

  current_player = X

  while True:
    get_move(current_player)

    current_player = O if current_player == X else X


if __name__ == '__main__':
  main()