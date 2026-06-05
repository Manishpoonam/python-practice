def rec_iterative (number):   # Factorail using iterative
    fact = 1
    for i in range(number):
        fact = fact * (i+1)
    return fact

def rec_recursive(number): # Factorial using recursive
    if number==1:
        return 1
    else:
        return number * rec_recursive(number-1)
    
def Fibonacci_iter(number):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(number):
        c=a+b
        print(c)
        a=b
        b=c
    



number = int(input("Enter the value "))
print("The Factorial value using iterative: ",rec_iterative(number))
print("The Factorial value using recursive: ",rec_recursive(number))
print("The Fibonacci sequence using iterative: ", Fibonacci_iter(number))


