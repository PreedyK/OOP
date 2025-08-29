number1=int(input("Enter Number 1:"))
number2=int(input("Enter Number 2:"))

operator=input("Enter an operator:")

if operator=="+":
    print("the result is:", number1+number2)

elif operator=="-":
    print("the result is:", number1-number2)

elif operator=="*":
    print("the result is:", number1*number2)

elif operator=="/":
    print("the result is:", number1/number2)