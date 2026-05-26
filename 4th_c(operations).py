#Python Operators ---

print(10+50)

sum1 = 100 + 50
sum2 = sum1 + 250
sum3 = sum2 + sum2
print(sum1)
print(sum2)
print(sum3)

#Arithmetic Operators ---
x = 15
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x / y)  # Division (returns a float)
print(x % y)
print(x ** y)
print(x // y) # Division (returns a float)

#Assignment Operators ---
x = 5 
print(x)
x = 5
x += 3  #	x = x + 3
print(x) # Result 8
x = 5
x -= 3  #	x = x - 3
print(x) # Result 5
x = 5
x *= 3  #	x = x * 3
print(x) # Result 15
x = 5
x /= 3  #	x = x / 3
print(x) # Result 5.0
x = 5
x //= 3  #	x = x // 3
print(x) # Result 1.0
x = 5
x %= 3  #	x = x % 3
print(x) # Result 2
x = 5
x **= 3  #	x = x ** 3 it is power of 3
print(x) # Result 125
x = 5
x &= 3  #	x = x & 3
print(x) # Result 1
x = 5
x |= 3  #	x = x | 3
print(x) # Result 7
x = 5
x ^= 3  #	x = x ^ 3
print(x) # Result 6
x = 5
x >>= 3  #	x = x >> 3
print(x) # Result 0
x = 5
x <<= 3  #	x = x << 3
print(x) # Result 40

print(x := 3)  # x = 3 so print(x) The Walrus Operator

numbers = [1, 2, 3, 4, 5] #example
if (count := len(numbers)) > 3:
    print(f"List has {count} elements")


#Comparison Operators ---
x = 5
y = 3
print(x == y) # Equal
print(x != y) # Not equal
print(x > y)  # Greater than
print(x < y)  # Less than
print(x >= y) # Greater than or equal to
print(x <= y) # Less than or equal to

#Chaining Comparison Operators
x = 5
print(1 < x < 10)
print(1 < x and x < 10)

# Logical Operators ---
x = 5
print(x > 0 and x < 10)      #and 
print(x < 5 or x > 10)       #or
print(not(x > 3 and x < 10)) #not

# Identity Operators ---
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) #Returns True if both variables are the same object / Checks if both variables point to the same object in memory
print(x is y) 
print(x == y) # Checks if the values of both variables are equal

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is not y) #operator returns True if both variables do not point to the same object

# Membership Operators ---
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) #Returns True if a sequence with the specified value is present in the object
print("pineapple" not in fruits) #	Returns True if a sequence with the specified value is not present in the object

# Membership in Strings
text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)

#Bitwise Operators ---

# The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 2 = 0010 (Result)
print(6 & 3)

# The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 7 = 0111 (Result)
print(6 | 3) 

# The ^ operator compares each bit and set it to 1 if only one is 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 5 = 0101 (Result)
print(6 ^ 3)



