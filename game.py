import random
print("Let's start the game..enter an input")
list=["rock","paper","scissors"]
c=0
d=0
for i in range(0,5):
    a=input()
    b=random.choice(list)
    while(a!="rock" and a!="paper" and a!="scissors"):
        print("enter either rock,paper or scissors")
        a=input()
    if(a=="rock" and a!=b):
        if(b=="scissors"):
            print("you won")
            c=c+1
        else:
            print("you lost")
            d=d+1
    elif(a=="paper" and a!=b):
        if(b=="rock"):
            print("you won")
            c=c+1
        else:
            print("you lost")
            d=d+1
    elif(a=="scissors"and a!=b):
        if(b=="paper"):
            print("you won")
            c=c+1
        else:
            print("you lost")
            d=d+1
    elif(a==b):
        print("tie")
if(c>d):
    print("you r the winner")
elif(c<d):
    print("you r the looser")
else:
    print("both r equal")
