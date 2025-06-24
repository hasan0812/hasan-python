# class Animal:
#     def make_sound(self):
#         return "Some generic animal sound"

# class Dog(Animal):
#     def make_sound(self):
#         return "Bark"

# class Cat(Animal):
#     def make_sound(self):
#         return "Meow"


# def animal_sound(OBJ):
#     print(OBJ.make_sound())


# dog = Dog()
# print(dog.make_sound())
# cat = Cat()
# print(cat.make_sound())

# print("using animal sound function")
# animal_sound(dog)
# animal_sound(cat)

class Bankaccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

def get_balance(self):
    return self.__balance

def deposit(self, amount):
    if amount > 0:
        self.__balance += amount
        print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Invalid amount!")

  def withdraw(self, amount):
    if 0 < amount <= self.__balance:
        self.__balance -= amount
        print(f"Withdraw: {amount}. Remaining balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount!")

account = Bankaccount("Hasan", 5000)

print("Account Owner:", account.owner)

print("Initial Balance:", account.get_balance())

account.deposit(2000)
account.withdraw(1000)





