stu_name=input("Enter the Student Name")

course1=int(input("Enter the grade points for Course1"))
course2=int(input("Enter the grade points for Course2"))
course3=int(input("Enter the grade points for Course3"))
course4=int(input("Enter the grade points for Course4"))
course5=int(input("Enter the grade points for Course5"))

total=course1+course2+course3+course4+course5
print("the total score is",total,"/500")

ave=(course1+course2+course3+course4+course5)/5
print("The average score is", ave)
