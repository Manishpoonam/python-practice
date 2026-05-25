# ---------------------------Creating Variables------------------------

x=5            # x is of type int
y="Manish"     # y is of type str
print(x, y)


# Casting ---

a = str(3)
b = int(3)
c = float(3)

print(a,b,c)
print(type(a), type(b), type(c))  # get the data type of a variable


# Many Values to Multiple Variables ---

d, e, f = 'Mango', 'Apple', 'Banana'
print(d, e, f)


# One Value to Multiple Variables ---

g = h = i = 'Secret'
print(g, h,i)


# Unpack a Collection ---

frutis = ['Apple', 'Mangoe', 'Gauava', 'Banana'] # If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
j,k,l,m = frutis
print(j,k,l,m)


# Output Variables ---

n="Python is awsome"
print(n)

o="Python"
p="is"
q="awsome"
print(o, p, q)
print(o+p+q)

# Global Variables ---

r = 'awsome'
def myFun():
    print("Python is " +r)

myFun()

#-----

s = 'awsome'
def Myfun1():
    s = 'fantastic'
    print('Python is '+s)

Myfun1()
print('Python is '+s)

#-----

def Myfun1():
    global t
    t = 'fantastic'
    print('Python is '+t)

Myfun1()
print('Python is '+t)