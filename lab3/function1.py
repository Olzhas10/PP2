from itertools import permutations
import random
import math
#task1
# def gramToOunce():
#     ounce = int(input("Ounce: "))
#     gram = ounce/28.3495231
#     print("Grams: " + str(gram))

# gramToOunce()

#task2
# def fToC():
#     F = float(input("Fahrenheit: "))
    
#     C = (F - 32) * 5/9
#     print("Centigrade: " + str(C))

# fToC()

#task 3
# def solve(numheads, numlegs):
#     num_chickens = 0
#     num_rabbits = 0
#     for i in range(1, numheads + 1):
#         num_chickens = i
#         num_rabbits = numheads - i
#         if(num_chickens * 2 + num_rabbits * 4 == numlegs):
#             break
#     print(f"Number of rabbits = {num_rabbits} and Number of chicks = {num_chickens}")
# solve(35, 94)

#task4
# nums = []
# pnums = []
# rang = int(input())
# for i in range (rang):
#     nums.append(int(input()))

# def getPrime():
#     for i in nums:
#         c = 0
#         for j in range(1, i):
#             if i % j == 0:
#                 c += 1
#         if c == 1:
#             pnums.append(i)
#     print(pnums)
    
# getPrime()

#task5
# def strPermut():
#     word = input()
#     perm = permutations(word)
#     for i in list(perm):
#         print(i)

# strPermut()

#task6
# def wordRev():
#     word = input()
#     a = word.split()
#     b = list(a)
#     b.reverse()
#     x = ' '.join(b)
#     print(x)

# wordRev()

#task7
# def has_33(nums):
#    for i in range(len(nums) - 1 ):
#       if nums[i] == 3 and nums[i + 1] == 3:
#          return True
#       elif nums[i] == 3 and nums[i + 1] != 3:
#          return False
    
        
# print(has_33([3, 3, 1]))
# print(has_33([1, 1, 3, 3]))
# print(has_33([1, 3, 1]))

#task8
# def spy_game(nums):
#     zero_count = 0
#     for num in nums:
#         if num == 0:
#             zero_count += 1
#         if zero_count == 2:
#             if num == 7:
#                 return True
#     return False

# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))


#task9
# def volume():
#     radius = int(input())
#     vol = 4/3 * (math.pi* radius**3)
#     print(vol)
    
# volume()

#task10
# x = int(input())
# nums = []
# unums = []
# for i in range(x):
#     nums.append(int(input()))

# def uni_list():
#     for i in range(len(nums)):
#         if nums[i] != nums[i - 1]:
#             unums.append(nums[i])
            
#     print(unums)

# uni_list()

#task11
# def isPalin():
#     word = input()
#     if word == word[::-1]:
#         return True
#     else:
#         return False

# print(isPalin())

#task12
# def his():
#     x = int(input())
#     s = []
#     for i in range(x):
#         i = int(input())
#         s.append(i)
        
#     for num in s:
#         print("*" * num)
        
# his()

    
#task13
# def guess():
#     print("Hello! What is your name?")
#     a = input()
#     print(f"""Well, {a}, I am thinking of a number between 1 and 20.
# Take a guess.""")
    
#     rand = random.randint(1, 20)
    
#     for i in range(20):
#         num = int(input())
#         if num == rand:
#             print(f"Good job, KBTU! You guessed my number in {i+1} guesses!")
#             break
        
#         elif num < rand:
#             print("""Your guess is too low.
# Take a guess""")
            
#         elif num > rand:
#             print("""Your guess is too high.
# Take a guess""")
            
# guess()
            

    

    

     