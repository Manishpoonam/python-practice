#Sets________________________________________

#Sets are used to store multiple items in a single variable.
#A set is a collection which is unordered, unchangeable*, and unindexed.

myset = {"apple", "mango"}
print(myset) #Sets are unordered, so you cannot be sure in which order the items will appear.

#Duplicates Not Allowed

thisset = {"apple", "banana", "cherry", True, 1, 2} #True and 1 is considered the same value:
print(thisset) #Result - {True, 'banana', 2, 'apple', 'cherry'} and 0 considerd as false

#Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#Add Set Items------
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#update
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset = {"apple", "banana", "cherry"} #The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#Remove Set Items---

#remove() method
thisset = {"apple", "banana", "cherry"} #If the item to remove does not exist, remove() will raise an error.
thisset.remove("banana")
print(thisset)

#discard() method
thisset = {"apple", "banana", "cherry"} #Remove "banana" by using the discard() method:
thisset.discard("banana")
print(thisset)

#pop() method
thisset = {"apple", "banana", "cherry"} #this method will remove a random item, so you cannot be sure what item that gets removed.
x = thisset.pop()
print(x)
print(thisset)

#clear() method 
thisset = {"apple", "banana", "cherry"} #The clear() method empties the set
thisset.clear()
print(thisset)

#del() method
thisset = {"apple", "banana", "cherry"} # The del keyword will delete the set comple
del thisset
# print(thisset)

#Loop Sets -------
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# Join Sets----------

#Union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#or

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

#Join Multiple Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)

#The union() method allows you to join a set with other data types, like lists or tuples.
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)  #he  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.
print(z)

#update method
set1 = {"a", "b" , "c"}  #The update() method inserts all items from one set into another.The update() changes the original set, and does not return a new set.
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#Intersection---------------
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}  #The intersection() method will return a new set, that only contains the items that are present in both sets.
set3 = set1.intersection(set2)
print(set3)

#or

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

#Difference------
set1 = {"apple", "banana", "cherry"} #The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

#or 

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)