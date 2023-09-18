class BankAccount:
 def_init_      (self,_accountNumber,_accountHolderName,__initialBalance=0):
self._accountNumber=_accountNumber self._accountHolder=_accountHolderName
self._AccountBalance=_initialBalance

 def depositMoney(self,amount):
  self._AccountBalance+=amount
  print("Rs.",amount,"has been deposited in your account.")

 def withdrawMoney(self,amount):
if
amount>self._AccountBalance:
 print("insufficient Balance")
else:
amount>self._AccountBalance-=amount
print("Rs.",amount,"has been withdrawn from your account.")
def checkBalance(self):
  print("current balance:",_AccountBalance)
  
 obj=BankAccount9876543210,"Lavanya"
 obj.depositMoney(10000)
 obj.withdrawMoney(6000)
 obj.checkBalance()