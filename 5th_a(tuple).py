# Tuples__________________

mytuple = ("Apple,Mango,Banana")
print(mytuple)

print(len(mytuple)) #lenght of tuple

# Create Tuple With One Item -------------
mytuple = ("Manish",) # To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
print(mytuple)

#Access Tuple Items --------------
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[1]) #Result - banana
print(thistuple[-1]) #Result - mango
print(thistuple[2:5]) #Resuil - ('cherry', 'orange', 'kiwi')
print(thistuple[:4]) #Result - ('apple', 'banana', 'cherry', 'orange')
print(thistuple[2:]) #Result - ('cherry', 'orange', 'kiwi', 'melon', 'mango')

#Update Tuples ----------------
#Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
#But there are some workarounds.

x = ("apple", "banana", "cherry") #Change Tuple Values
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

x = ("apple", "banana", "cherry") #Add Items in last
y = list(x)
y.append("Orange")
x = tuple(y)
print(x)

#Remove Items -----
#Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#delete tuple
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists

#Unpack Tuples_______________
fruits = ("apple", "banana", "cherry") #Packing a tuple
#unpacking---
(green,yellow,red) = fruits
print(green)
print(yellow)
print(red)

#Loop Tuples_________________
thistuple = ("apple", "banana", "cherry") #Iterate through the items and print the values
for x in thistuple:
    print(x)

#Loop Through the Index Numbers-----
thistuple = ("apple", "banana", "cherry")
for x in range(len(thistuple)):
    print(thistuple[x])

#Using a While Loop-----
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#Join Tuples____________________

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)


#Multiply Tuples (If you want to multiply the content of a tuple a given number of times, you can use the * operator:)
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple) #result - ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

