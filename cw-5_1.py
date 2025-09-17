myStudents={"s1":{
                "name":"Judah",
                "Major":"Chemistry",
                "Year":"Freshman",
                "credits":"15",
                "gpa":"3.8"}}
while True:
    print("1.: Add a Student:")
    print("2: Delete a Student:")
    print("3: Edit a Student:")
    print("4: Print a Student:")
    print("5: Quit")

    option = input("Enter option:")

    if option == "1":
        student = input("Enter Student name:")
        major = input("Enter major:")
        year = input("Enter Year:")
        credits = input("Enter credits:")
        gpa = input("Enter GPA:")
        sID = input("Enter Student ID")
        myStudents.update({"sID":{
                                "Name":student,
                                "major":major,
                                "year":year,
                                "credits":credits,
                                "GPA":gpa}})
        print(myStudents)

    elif option == "2":
        sID = input("Enter Student ID you wish to remove:")
        del myStudents[sID]

    elif option == "3":
        student = input("Enter Student name:")
        major = input("Enter major:")
        year = input("Enter Year:")
        credits = input("Enter credits:")
        gpa = input("Enter GPA:")
        sID = input("Enter Student ID")
        myStudents.update({"sID":{
                                "Name":student,
                                "major":major,
                                "year":year,
                                "credits":credits,
                                "GPA":gpa}})




