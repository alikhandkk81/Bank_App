class Account: # this is a class
    def __init__(self, name, balance, min_balance): # this is constructer
      self.name = name
      self.balance = balance
      self.min_balance = min_balance



    def deposit(self, amount): # this is method
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Desculpe não há fundos suficientes")

    def statment(self):
        print("Saldo da conta: ${}".format(self.balance))

class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)


    def __str__(self):
        return "{}'S conta atual:Saldo ${}".format(self.name, self.balance)

class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)
    def __str__(self):
        return "{}'S Conta poupança:saldo ${}".format(self.name, self.balance)
        

# basta usar o comando acima para usar banco

# S = Currnt("sajjad", 500)
# S.deposit(300)
#S.statment()

#S.withdraw(100)
#S.statment()
            
        
    
