a=int(input("Enter First Side : "))
b=int(input("Enter Second Side : "))
c=int(input("Enter Third Side : "))
r=False
if a>b and a>c:
    r=(b+c)>a
elif b>a and b>c:
    r=(a+c)>b
else:
    r=(a+b)>c

if r==True:
    print("Yes")
else:
    print("No")
