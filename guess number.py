import random

top_of_number=input("type a number : ")

if top_of_number.isdigit():
    top_of_number=int(top_of_number)
    
    
    if top_of_number<=0:
        print("enter a number larger than 0 ")
        quit()
else:
    print("enter a number next time ")
    
random_number=random.randint(0, top_of_number)

guess=0

while True:
    guess+=1
    user=input("make a number : ")
    if user.isdigit():
        user=int(user)
    else:
        print("enter a number next time ")
        continue

    if user==random_number:
        print("yes you got it ")
        break
    elif user>random_number:
        print("you number is  greater than random number")
        continue
    else:
        print("you  number is less than random number ")
        continue
print("you got",guess,"time")
    
    