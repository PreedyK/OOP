class Person:
    def __init__(self, nn, dd, gg):
        self._pname = nn
        self._dob = dd
        self._gender = gg

    def display(self):
        print("Person name: ", self._pname)
        print("Person_DOB: ", self._dob)
        print("Person_Gender: ", self._gender)
        return ""

class Student(Person):
    def __init__(self, x, y, z, a, b):
        Person.__init__(self, x, y, z)
        self.dept = a
        self.id = b

    def display(self):
        print(Person.display(self))
        print("Stu_Dept: ", self.dept)
        print("Stu_ID: ", self.id)

class Faculty:
    def __init__(self, x, y, z, a, b):
        Person.__init__(self, x, y, z)
        self.dept = a
        self.design = b

    def display(self):
        print(Person.display(self))
        print("Fac_Dept: ", self.dept)
        print("Fec_Design: ", self.design)


s1 =Student("Pam", "1989", "Female", "Receptionist", "3424")
s1.display()

s2=Student("Millie", "2005", "Female", "Graphic Design", "2389")
s2.display()

f1=Faculty("Rebekah", "1980", "Male", "Bible", "Dr")
f1.display()