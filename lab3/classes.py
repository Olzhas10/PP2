import math
#task 1
# class Name:
#     def __init__(self):
#         self.name = ""
        
#     def getString(self):
#         self.name = input()
        
#     def printString(self):
#         print(self.name.upper())
        
# word = Name()
# word.getString()
# word.printString()
    
#task 2
# class Shape:
#     def area(self):
#         print(0)

# class Square(Shape):
#     def __init__(self, length):
#         super().__init__()
#         self.length = length
        
#     def area(self):
#         print(self.length **2)

# shape = Shape()
# square = Square(5)
# shape.area()
# square.area()

# task 3
# class Shape:
#     def area(self):
#         print(0)
        
# class Rectangle(Shape):
#     def __init__(self, lenght, width):
#         super().__init__()
#         self.lenght = lenght
#         self.width = width
        
#     def area(self):
#         print(self.lenght * self.width)

# rect = Rectangle(5, 20)
# rect.area()

# task 4
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def show(self):
#         print(self.x, self.y)
        
#     def move(self, x, y):
#         self.x += x
#         self.y += y
        
#     def dist(self, point):
#         return math.sqrt((self.x - point.x) **2 + (self.y - point.y) **2)
    
# p1 = Point(2, 3)
# p2 = Point(3, 4)
# p1.show()
# p2.show()
# print(p1.dist(p2))
# p1.move(2, 2)
# p1.show()

# task 5
# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
    
#     def show_owner(self):
#         print(self.owner)
        
#     def show_balance(self):
#         print(self.balance)
        
#     def deposit(self, amount):
#         self.balance += amount
        
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawal of", amount, "completed.")
#         else:
#             print("Insufficient funds on the account.")
        
# test = Account("Olzhas", 50000)
# test.show_owner()
# test.show_balance()
# test.deposit(2000)
# test.show_balance()
# test.withdraw(53000)
# test.show_balance()

# task 6
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True


# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# prime_numbers = list(filter(lambda x: is_prime(x), numbers))

# print("Prime numbers in the list:", prime_numbers)





    
    
