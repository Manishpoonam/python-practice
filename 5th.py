# List in Python | Append, Insert, Count, Sum, Pop



l =[1,5,7,20,99,90]
print(l)

print(l[0])

x=l[1:4]   # slicing list
print(x)  

l.append(10)  # add the elemnt in last
print(l)

m = [11,90,30]
l.extend(m)  # add the other list to first one
print(l)

m.insert(2,100)
print(m) # add emenet wher you want in list

l.sort
print(l) # arrange list's element in ascending order

l.pop(2) # delete or remove elemt using index
print(l)

c = l.count(90) # it count number of elements
print(c)

d = len(l) # lenght of list
print(d)

no=[20,10,90]
s = sum(no) # it add the value of element
print(s)

x = l*3
print(x) # it duplicate the element of list 3 time

for i in range(len(l)):  # print all ements using loop
    print(l[i])

x=[]
print("how many elament you want") # taking input by user
n = int(input())
print("Enter the elemnet in the list")
for i in range (n):
    a = int(input())
    x.append(a)
print(x)