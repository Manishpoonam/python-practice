import random

r = random.randint(1,20)

print("Enter the vlaue from 1 to 20")

while(True):
    inp = int(input())
    if(r > inp):
        print("Try a greater number")
    elif(r < inp):
        print("Try a samller number")
    else:
        print("Conguratate, This is right guess")
        break