class ATM:
  def __init__(self):
    self.balance = 0

  def check_balance(self):
    return self.balance

  def deposit(self, amount):
    if amount <= 0:
      raise ValueError('Deposit amount must be positive.')
    
    self.balance += amount
    
  def withdraw(self, amount):
    if amount <= 0:
      raise ValueError('Withdrawal amount must be positive.')
    if amount > self.balance:
      raise ValueError('Insufficient funds.')

    self.balance -= amount

class ATMController:
  def __init__(self):
    self.atm = ATM()

  def get_number(self, prompt):
    while True:
      try:
        number = float(input(prompt))
        return number
      except ValueError:
        print('Please enter a valid number.')


def main():
  atm = ATMController()


if __name__ == '__main__':
  main()