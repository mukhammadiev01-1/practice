''' CLASS deep diving
    (1) ENCAPSULATION <
    (2) INHERITENCE
    (3) POLIMORPHISM
'''

print("===== ENCAPSULATION =====")
# ENCAPSULATION > public __private _protected
# comparison magic methods > __init__() __str__() __repr__() __add__() __len__()


class Account():
    # state
    description = "The class makes bank accounts"

    # constructor
    # __init__ means initialize, it's a special method that is called when an object is created from the class
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount

    @property  # getter for __owner private variable and means that we can access the __owner variable outside the class using the holder method
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("holder.setter:", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("change_ownership:", new_owner)
        self.__owner = new_owner


my_account = Account("Shawn", 1000)
my_account.get_balance()

print("-----")
my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()

print("-----")

try:
    result = my_account.__amount
    print("result:", result)
except Exception as err:
    print("No target state found:", err)

# getter vs setter
print("owner before:", my_account.holder)  # state
my_account.holder = "Martin"  # state
print("owner after:", my_account.holder)

# "#"is used to define private in Javascript, but in Python we use __ to define private variables and methods.
#   _ is used to define protected variables and methods, which can be accessed by subclasses but not by other classes.


# getter va setter bu yerda __owner private variable uchun ishlatilgan, getter va setter yordamida biz __owner variable ni tashqaridan o'qish va o'zgartirish(setter) imkoniyatiga ega bo'lamiz.
# class User {
# constructor(name) {
#   this.name = name;
#  }
# }

# const user = new User("Ali");
# console.log(user.name);

# user.name = "John";
