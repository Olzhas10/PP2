#task1
# def squares_generator(N):
#     for i in range(1, N+1):
#         yield i*i
        
# print(*squares_generator(5))
    
#task2
# def even_numbers(n):
#     for i in range(0, n+1, 2):
#         yield i

# n = int(input("Write a number: "))

# print(*even_numbers(n), sep =', ')

# #task3
# def number(n):
#     for i in range(n+1):
#         if i % 3 == 0 and i % 4 == 0:
#             yield i

# n = int(input("Write a number: "))
# print(*number(n))
      
#task4    
# def squares(a, b):
#     for i in range(a, b+1):
#         yield i*i

# n = int(input("Write a number: "))
# q = int(input("Write b number: "))
# print(*squares(n, q))

#task5
# def countdown(n):
#     while n >= 0:
#         yield n
#         n -= 1
# n = int(input("Write a number: ")) 
# for i in countdown(n):
#     print(i)