# class Fruits:
#     def __int__(self, color):
#         self.color = color
#     def colortest():
#         print(f"the color of fruit is {self.color}")   
#      def Taste(self):
#         print("yummy")


# apple = Fruits("red")
# apple.colortest()
# banana = Fruits("yellow")
# banana.colortest()

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no= acc

     def debit(self, amount):
         self.balance =  self.balance - amount
         print("Rs", amount,"From account no", self.account_no, "was debited")
         print("total balance", self.get_bal())

     def credit(self, amount):
        self.balace :
        print("Rs", amount,"From account no", self.account_no, "was debited")
        print("total balance", self.get_bal())

     def get_bal(self):
         return self.balance

acc1 = Account(10000, 12220)
acc1.debit(3000)

acc2 = Account(40000, 122232)
acc2.credit(3000)

