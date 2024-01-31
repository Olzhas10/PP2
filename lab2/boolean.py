print(10 > 9)
print(10 == 9)
print(10 < 9)
print(bool("abc"))
print(bool(0))

#exampls
print(bool(""))

print(bool(1))

def myFunction() :
  return False

print(myFunction())

if myFunction():
  print("YES!")
else:
  print("NO!")
  
x = 200
print(isinstance(x, int))