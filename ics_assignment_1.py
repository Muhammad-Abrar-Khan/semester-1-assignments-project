# It takes input numbers (until user entered "0") i.e. receipt amount & prints the total amount & total count of receipts i.e. total inputs except 0.
a=1
t=0
n=0
while (a>0):
    a = float(input("enter receipt amount : "))
    if (a>0):
        t=t+a
        n=n+1
print("total amount = " , t)
print("count of receipts is" , n)






