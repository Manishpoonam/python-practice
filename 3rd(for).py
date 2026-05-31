# For Loop | Functions in Python | Import Statement


#-------------loop----


fruits = ["apple", "banana", "gauva", "cherry"]
for x in fruits:
    print(x)

#Looping Through a String------
for x in "Banana":
    print(x)
    
#break Statement-----
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for x in range (1,20,2):
    print(x)



#-------------function---


def myfun():
    print("hello world")

def sum(a,b):
    print(a+b)

def add(a,b):
    return a+b

myfun()

sum(5,5)

c= add(10,7)

print(c)




