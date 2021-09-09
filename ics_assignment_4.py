# If you want to run this code enter "yes" else enter anything it will end this code. This program will take input +ve,-ve and 0 and will print the total of inputs i.e. sum of all inputs.
# Note that while giving input +ve no if you enter 0 or -ve no so it will break the loop and will print total count of +ve inputs and will move on to the next step.
# Same goes for -ve and 0.

a=1
n=0
t=0
p=0
while True:
    text=input("Do you want to run this code or want to end it?\n")
    if ("yes"  in text):
        while (a>0):
            a = float(input("enter +ve no : "))
            if(a>0):
                t=t+a
        print("total of +ve no is " , t)
        while (a<0):
            a = float(input("enter -ve no : "))
            if(a<0):
                n=n+1
        print("count of -ve no is " , n)
        while (a==0):
            a = float(input("enter zero (O) : "))
            if(a==0):
                p=p+1
        print("count of 0 is " , p)
    else:
        print("program ended")
        break




