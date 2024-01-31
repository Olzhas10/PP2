fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
  
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

#examples
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#remove random item
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)