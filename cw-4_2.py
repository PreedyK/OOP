myList = ["x"]

while True:
    print("1. Append to the List")
    print("2. Remove from the List")
    print("3. Pop an element from the List")
    print("4. Display the List")
    print("5. Quit")

    option = input("Enter your choice:")

    if option == "1":
        n = input("Enter the element to be added to the List:")
        myList.append(n)

    elif option == "2":
        m = input("Enter the element to be removed from the List:")
        myList.remove(m)


    elif option == "3":
        myList.pop()


    elif option == "4":
        print(myList)


    elif option == "5":
        break