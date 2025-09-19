myStudents = {}
while True:
    print("1.: Add a Student")
    print("2: Delete a Student")
    print("3: Edit a Student")
    print("4: Display a Student")
    print("5: Quit")

    option = input("Enter option:")

    if option == "1":
        student = input("Enter Student name:")
        Lab1 = int(input("Enter Points for Lab 1:"))
        Lab2 = int(input("Enter Points for Lab 2:"))
        Lab3 = int(input("Enter Points for Lab 3:"))
        Lab4 = int(input("Enter Points for Lab 4:"))
        Lab5 = int(input("Enter Points for Lab 5:"))
        sID = input("Enter Student ID:")
        total= Lab1+Lab2+Lab3+Lab4+Lab5
        avg= total/5
        percent = avg*10

        myStudents.update({sID:{
                                "Name":student,
                                "Points for Lab 1":Lab1,
                                "Points for Lab 2":Lab2,
                                "Points for Lab 3":Lab3,
                                "Points for Lab 4":Lab4,
                                "Points for Lab 5":Lab5,
                                "Total": total,
                                "Percent": percent,
                                "Average": avg
                                }})

        print(myStudents)
        print("Total:",total)
        print("Percent:", percent)
        print("Average:", avg)


    elif option == "2":
        sID = input("Enter Student ID you wish to remove:")
        del myStudents[sID]

    elif option == "3":
        sID = input("Enter Student ID you wish to edit:")
        student = input("Enter Student name:")
        Lab1 = int(input("Enter Points for Lab 1:"))
        Lab2 = int(input("Enter Points for Lab 2:"))
        Lab3 = int(input("Enter Points for Lab 3:"))
        Lab4 = int(input("Enter Points for Lab 4:"))
        Lab5 = int(input("Enter Points for Lab 5:"))
        total = Lab1+Lab2+Lab3+Lab4+Lab5
        avg = total/5
        percent = avg * 10
        myStudents.update({sID: {
                            "Name": student,
                            "Points for Lab 1": Lab1,
                            "Points for Lab 2": Lab2,
                            "Points for Lab 3": Lab3,
                            "Points for Lab 4": Lab4,
                            "Points for Lab 5": Lab5,
                            "Total": total,
                            "Percent": percent,
                            "Average": avg
        }})


    elif option == "4":
        sID = input("Enter Student ID you wish to display:")
        for n in myStudents.items():
            print(n)


    elif option == "5":
        break
