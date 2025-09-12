nameList = []
ageList = []

while True:
    print("1. Add an Element to the List")
    print("2. Remove from the List")
    print("3. Replace an element from the List")
    print("4. Reverse the Elements of the List")
    print("5. Print the List")
    print("6. Exit")

    option = input("Enter your choice:")

    if option == "1":
        append_name = input("Enter the name of the student to be added:")
        append_age = input("Enter the age of the student to be added:")
        nameList.append(append_name)
        ageList.append(append_age)

    elif option == "2":
         remove_name = input("Enter the name of the student to be removed from the List:")
         remove_age = input("Enter the age of the student to be removed:")
         nameList.remove(remove_name)
         ageList.remove(remove_age)


    elif option == "3":
        replace_name = int(input("Enter the index of the Student name to be replaced:"))
        new_name = input("Enter new student name:")
        replace_age = int(input("Enter the index of the age to be replaced:"))
        new_age = input("Enter new age:")
        nameList[replace_name] = new_name
        ageList[replace_age] = new_age

    elif option == "4":
        nameList.reverse()
        ageList.reverse()

    elif option == "5":
        print(nameList)
        print(ageList)

    elif option == "6":
        break