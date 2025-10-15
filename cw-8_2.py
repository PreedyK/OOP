import pickle
class Product:
    def __init__(self):
        self.pid = ""
        self.pname = ""
        self.price = 0.0
        self.description = ""

    def get_product_details(self):
        self.pid = input("Enter Product ID:")
        self.pname = input("Enter Product Name:")
        self.price = input("Enter Product Price")
        self.description = input("Enter Product Description")

    def display_product_info(self):
        print(self.pid)
        print(self.pname)
        print(self.price)
        print(self.description)

#Main

while True:
    print("1. Create Product Object ")
    print("2. Get Product Info ")
    print("3. Display Product ")
    print("4. Write the Product into a File ")
    print("5. Read from the File and Display the Product Info ")
    print("6. Exit")

    option = input("Enter your choice:")

    if option == "1":
        product_obj = Product()

    if option == "2":
        product_obj.get_product_details()

    if option == "3":
        product_obj.display_product_info()

    if option == "4":
        f1 = open("product_inventory.dat", "ab")
        pickle.dump(product_obj, f1)
        f1.close()

    if option == "5":
        f2 = open("product_inventory.dat", "rb")
        while True:
            try:
                data = pickle.load(f2)
                data.display_product_info()
            except EOFError:
                break

    if option == "6":
        break