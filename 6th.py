# Dictionaries in Python | A to Z of Dictionaries 

d={'Manish':90, 'Aman':99, 'Vaishali':100}  #Name is key and 90 is value

print(d) #Print all Dictionary

l= d.keys() #print all keys
print(l)

b=d.values() #prints all values
print(b)

del d['Aman'] # delet values and keys
print(d) 

d['Vaishali']=105 #update the data
print(d) #Print all Dictionary

d['Vinod'] = 500 # update key 
print(d)

marks = d['Vaishali'] #if you want to know specific value of  key i.e., if you want to know the marks of vaishali
print(marks)

if('Manish' in d):  # If you want to konw the the key is available in dictionary or not 
    print("Yes")
else:
    print("No")


for i in d:
    print(i, d[i])