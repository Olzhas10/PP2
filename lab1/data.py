x = 5
print(type(x))

x = ["apple", "banana", "cherry"]	#list can change	
print(x)
x = ("apple", "banana", "cherry")	#tuple cant 
print(x)
x = range(6)	#range
print(x)

x = {"name" : "John", "age" : 36}	#dict	
print(x["name"])
x = {"apple", "banana", "cherry"}	#set	
print(x)
x = frozenset({"apple", "banana", "cherry"})	#frozenset не изменяемый сет
print(x)	
x = True	#bool	
print(x)
x = b"Hello"	#bytes	
print(x[0])
x = bytearray(5)	#bytearray как bytes но можно изменить
print(x)
x = memoryview(bytes(5))	#memoryview	
print(x)
x = None	#NoneType
print(x)


x = str("Hello World")		
x = int(20)		
x = float(20.5)		
x = complex(1j)	
	
x = list(("apple", "banana", "cherry"))		
print(x)
x = tuple(("apple", "banana", "cherry"))		
print(x)
x = range(6)		
print(x)
x = dict(name="John", age=36)	
print(x)	
x = set(("apple", "banana", "cherry", "banana"))	
print(x)	
x = frozenset(("apple", "banana", "cherry"))		
x = bool(5)	
print(x)	
x = bytes(5)	
print(x)	
x = bytearray(5)		
print(x)
x = memoryview(bytes(5))
print(x)