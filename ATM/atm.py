class atm(object):
    def __init__(self,atmCardNumber, pinNumber):
        self.atmCardNumber = atmCardNumber
        self.pinNumber = pinNumber
    
    def CashWithdrawal(self):
        print("Cash Withdrawn")
    
    def BalanceEnquiry(self):
        print("Balance Enquired")
    
Atm=atm("3423 7509 3421","1803 5407")

print("Details of ATM Card:")
print("ATM Card Number: ", Atm.atmCardNumber)
print("Pin Number: ", Atm.pinNumber)
print(Atm.CashWithdrawal())
print(Atm.BalanceEnquiry())