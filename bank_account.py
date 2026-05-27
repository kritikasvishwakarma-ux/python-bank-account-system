class account:
      def __init__(self,balance, account_number):
            self.balance=balance
            self.account_number=account_number
      def debit(self,amount):
            self.balance-=amount
            print("balance after debit",self.balance)
      def credit(self,amount):
            self.balance+=amount
            print("balance after credit",self.balance)
      def display(self):
            return self.balance,self.account_number
      
a1=account(10000,12345)
print(a1.display())

a1.debit(500)
a1.credit(2000)