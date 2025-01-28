import os

def read_file(filename):
  with open(filename, 'r') as file:
    return file.read()

def main():
  filename = input('Enter the filename to open or create: ').strip()
  try:
    if os.path.exists(filename):
      print(read_file(filename))
      
    print(f'{filename} saved.')
  except OSError:
    print(f'{filename} could not be opened.')

if __name__ == '__main__':
  main()