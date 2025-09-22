Projects = {}
while True:
    print("1. Project Initiation")
    print("2. Project Closure")
    print("3. Project Progress Update")
    print("4. Print a Project")
    print("5. Print All Projects")
    print("6. Quit")

    option = input("Please Select an Option:")

    if option == "1":
        managers = []
        tech = []
        team = []

        pID = input("Enter Project ID::")
        title = input("Enter project Title:")
        n = int(input("How Many Project Managers would you like to enter:"))
        for m in range (0,n):
            managers.append(input("Enter a Project Manager:"))
        start = input("Enter a Start Date:")
        end = input("Enter and End Date:")
        sponsor = input("Enter a Project Sponsor")
        budg = input("Enter a Budget for your Project:")
        t = int(input("Enter how many Technologies for your Project:"))
        for e in range(0,t):
            tech.append(input("Enter the Technology:"))
        s = int(input("Enter number of Team Members:"))
        for i in range(0,s):
            team.append(input("Enter Team Member Name:"))

        Projects.update({"pID": {
                            "Project title":title,
                            "Managers":managers,
                            "Start_date":start,
                            "End_Date":end,
                            "Sponsor":sponsor,
                            "budget": budg,
                            "technologies":tech,
                            "Team_Members":team


}})

    if option == "2":
        pID = input("Enter Project ID you wish to Close:")
        del Projects[pID]


    if option == "3":
        managers = []
        tech = []
        team = []

        pID = input("Enter Project ID you wish to Update:")
        title = input("Enter project Title:")
        n = int(input("How Many Project Managers would you like to enter:"))
        for m in range(0, n):
            managers.append(input("Enter a Project Manager:"))
        start = input("Enter a Start Date:")
        end = input("Enter and End Date:")
        sponsor = input("Enter a Project Sponsor")
        budg = input("Enter a Budget for your Project:")
        t = int(input("Enter how many Technologies for your Project:"))
        for e in range(0, t):
            tech.append(input("Enter the Technology:"))
        s = int(input("Enter number of Team Members:"))
        for i in range(0, s):
            team.append(input("Enter Team Member Name:"))

        Projects.update({"pID": {
                            "Project title": title,
                            "Managers": managers,
                            "Start_date": start,
                            "End_Date": end,
                            "Sponsor": sponsor,
                            "budget": budg,
                            "technologies": tech,
                            "Team_Members": team
        }})