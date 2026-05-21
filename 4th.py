# Strings in Python | Slicing | Count, Find & Replace 


a="Hello i m Manish"

print(a[2])   #it give the index value of that place

print(len(a))  # it gives the lenght of String


b="ManishKumar"
c = b[1:5]   # String slicing
print(c)

d  = "Hi Hi Hi Hi Manish"
e = "Hi"   # count Function
cout = d.count(e)
print(cout)


f= "Manish"
src=d.find(f) # Search function
print(src)

new = d.replace("Manish", "Butku") #replace function
print(new)


for n in new:
    print(n) # take each single character and print

j = f.upper() # function for uppercase and use lower() for lowercase
print(j)

