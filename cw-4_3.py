myList = []

while True:
    print("1. Add an Element to the List")
    print("2. Remove from the List")
    print("3. Replace an element from the List")
    print("4. Sort the Elements in the List")
    print("5. Reverse the Elements of the List")
    print("6. Print the List")
    print("7. Exit")

    option = input("Enter your choice:")

    if option == "1":
        n = input("Enter the element to be added to the List:")
        myList.append(n)

    elif option == "2":
        m = input("Enter the element to be removed from the List:")
        myList.remove(m)


    elif option == "3":
        x = int(input("Enter the index of the element to be replaced:"))
        new_element = input("Enter new element:")
        myList[x] = new_element


    elif option == "4":
        myList.sort()


    elif option == "5":
        myList.reverse()

    elif option == "6":
        print(myList)

    elif option == "7":
        break