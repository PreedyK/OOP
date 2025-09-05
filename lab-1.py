while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    option=input("Select an option:")

    if option =="1":
        n = int(input("Enter first number:"))
        m = int(input("Enter second number:"))
        print("The Answer is:", n+m)
        print("----------------------------------")

    elif option =="2":
        n = int(input("Enter first number:"))
        m = int(input("Enter second number:"))
        print("The Answer is:", n-m)
        print("----------------------------------")

    elif option =="3":
        n = int(input("Enter first number:"))
        m = int(input("Enter second number:"))
        print("The Answer is:", n*m)
        print("----------------------------------")

    elif option =="4":
        n = int(input("Enter first number:"))
        m = int(input("Enter second number:"))
        print("The Answer is:", n/m)
        print("----------------------------------")

    elif option =="5":
        break