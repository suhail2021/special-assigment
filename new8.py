class Bank_Account: 
    def __init__(self): 
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ") 
    def bankfees(self):
        self.balance=(95/100)*self.balance 
        print(self.balance)       
  
    def display(self): 
        print("\n Net Available Balance=",self.balance)  
n = Bank_Account() 
n.deposit() 
n.withdraw() 
n.bankfees()
n.display() 
