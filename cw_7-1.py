class Student:
    def init_(self):
        self.stu_id = ""
        self.stu_name = ""
        self.major = ""
        self.gpa = 0.0
        self.dob = ""
        self.courses = []

    def add_student(self):
        self.stu_id = input("Enter student ID:")
        self.stu_name = input("Enter Student Name:")
        self.major = input("Enter Student Major:")
        self.gpa = input("Enter GPA:")
        self.dob = input("Enter Date of Birth:")

    def edit_student(self):
        self.stu_name = input("Enter the updated name for student:")
        self.stu_name = input("Enter the updated Student Name:")
        self.major = input("Enter the updated Student Major:")
        self.gpa = input("Enter the updated GPA for the Student:")
        self.dob = input("Enter the updated Date of Birth:")

    def register_course(self, cc1):
        self.courses.append(cc1)

    def display_student(self):
        print ("Student ID:", self.stu_id)
        print("Student Name:", self.stu_name)
        print("Student Major:", self.major)
        print("Student GPA:", self.gpa)
        print("Date of Birth:", self.dob)
        for x in self.courses:
            print("Courses Registered:", x.courseName)

class Course:
    def init_(self):
        self.courseID = ""
        self.courseName = ""
    def add_course(self):
        self.courseID = input("Add course ID:")
        self.courseName = input("Add course name:")


#Main Code
s1 = Student()
s1.add_student()
c1 = Course()
c1.add_course()
s1.register_course(c1)
s1.display_student()