def print_menu():
  print('\nTodo List Menu:')
  print('1. View Tasks')
  print('2. Add a Task')
  print('3. Remove a Task')
  print('4. Exit')


def get_choice():
  while True:
    choice = input('Enter your choice: ')
    valid_choices = ('1', '2', '3', '4')
    if choice not in valid_choices:
      print('Invalid choice')
      continue
    else:
      return choice


def display_tasks(tasks):
  if not tasks:
    print('No tasks in the list.')
    return
  
  for index, task in enumerate(tasks, start=1):
    print(f'{index}. {task}')

def main():
  tasks = []

  while True:
    print_menu()

    choice = get_choice()

    if choice == '1':
      display_tasks(tasks)
    else:
      break
  

if __name__ == '__main__':
  main()