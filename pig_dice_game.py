import random 

def roll_die():
  return random.randint(1, 6)

def main():
  scores = [0, 0]
  current_player = 0 

  while True:
    player_name = f'Player {current_player + 1}'
    print(f'Current scores: Player 1: {scores[0]}, Player 2: {scores[1]}')

    if scores[current_player] >= 100:
      print(f'{player_name} wins!')
      break

    current_player = 1 if current_player == 0 else 0

if __name__ == '__main__':
  main()