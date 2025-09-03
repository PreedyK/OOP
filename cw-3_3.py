p=int(input("Enter principal loan amount:"))
R=float(input("Enter rate of interest:"))
n=int(input("Enter duration of loan:"))

r=R/(12*100)

emi= p*r*((1+r)**n)/((1+r)++n-1)

print("EMI:", emi)

for i in range (1, n):
    balance=p-emi
    print(balance)
    p = balance