class Player:
   def play(self):
       print("The player is playing cricket.")

class Batsman(Player):
   def play(self):
       print("The batsman is batting.")

class Bowler(Player):  
   def play(self):
       print("The bowler is bowling.")

batsman = Batsman() 
bowler  = Bowler()

batsman.play()
bowler.play()

class BankAccount:

  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
  def deposit(self,amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposited Rs.{}. New Balance Rs.{}".format(amount,self.__account_balance))
    else :
      print("Invalid deposit amount. Please deposit a positive amount.")

  def withdraw(self,amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance = amount
      print("Withdrew Rs.{} . New Balance Rs.{}".format(amount,self.__account_balance))

    else :
      print("Invalid withdrawal amount or insufficient balance.")

  def display_balance(self):
    print("Account balance for {} (Account # {}): Rs.{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))

account = BankAccount(account_number = "123456789",
                     account_holder_name = "divya",
                     initial_balance = 5000.0)

account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()

