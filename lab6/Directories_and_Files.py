import os
from string import ascii_uppercase
#task 1
path = 'C:\\'

print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files:")
print([ name for name in os.listdir(path)])

# task 2
# print('Path exists:', os.access(r'C:', os.F_OK))
# print('Path readable:', os.access(r'C:', os.R_OK))
# print('Path writable:', os.access(r'C:', os.W_OK))
# print('Path executable:', os.access(r'C:', os.X_OK))

# task 3
# path = input('Insert path \n')
# path_bool = os.access(path, os.F_OK)
# if path_bool == False:
#     print("Path does not exist")
# elif path_bool == True:
#     print("Directories:", ', '.join([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]))
#     print("Files:", ', '.join([name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))]))
    
# task 4
# with open('C:\\PP2\\lab6\\file.txt', 'r') as file:
#     x = len(file.readlines())
#     print("Number of lines:", x)

# task 5
# mylist = ['qwr', 'etw', 'etr', 'wet']
# with open('C:\\PP2\\lab6\\file2.txt', 'w') as file:
#     for i in mylist:
#         file.write(i + '\n')


# task 6
# for char in ascii_uppercase:
#     file = open('C:\\PP2\\lab6\\{fchar}.txt'.format(fchar = char), 'x')
#     file.close()

# task 7
# with open('file.txt', 'r') as file1, open('file3.txt', 'a') as file2:
#     for line in file1:
#         file2.write(line) 

# task 8
# path = 'C:\\PP2\\lab6\\testfile.txt'
# path_bool = os.access(path, os.F_OK)
# if path_bool == False:
#     print('Path does not exist')
# elif path_bool == True:
#     os.remove(path)
#     print("File has been removed")