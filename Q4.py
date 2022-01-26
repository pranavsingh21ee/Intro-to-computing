n1=float(input("Enter First Number : "))
n2=float(input("Enter Second Number : "))
n3=float(input("Enter Third Number : "))
if n1>n2 and n1>n3:
    l= n1
elif n2>n1 and n2>n3:
    l= n2
else:
    l= n3
print("The greatest number is", l)
    
