def area_rectangle():
    l = int(input("Enter length:"))
    w = int(input("Enter width:"))
    print(l*w)

def volume_cube():
    l=int(input("Enter side length:"))
    print(l*l*l)

def area_circle():
    r = int(input("Enter radius:"))
    print(3.14*r*r)

def volume_circle():
    r = int(input("Enter radius:"))
    print(2*3.14*r)

def volume_sphere():
    r = int(input("Enter radius:"))
    print((4/3)*3.14*r*r*r)

while True:
    print("1: Area of a Rectangle")
    print("2: Volume of a Cube")
    print("3: Area of a Circle")
    print("4: Volume of a Circle")
    print("5: Volume of a Sphere")
    print("6: Quit")

    option = input("Choose an option:")

    if option == "1":
        area_rectangle()

    elif option == "2":
        volume_cube()

    elif option == "3":
        area_circle()

    elif option == "4":
        volume_circle()

    elif option == "5":
        volume_sphere()

    elif option == "6":
        break