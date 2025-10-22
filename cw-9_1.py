class Customer:
    def __init__(self):
        self.cid = ""
        self.acc_no = ""
        self.cname = ""
        self.phone = ""
        self.emailid = ""
        self.balance = 0.0

    def create_customer(self):
        self.cid = input("Enter Customer ID: ")
        self.acc_no = input("Enter Account Number: ")
        self.cname = input("Enter Customer Name: ")
        self.phone = input("Enter Phone Number: ")
        self.emailid = input("Enter Email: ")
        self.balance = float(input("Enter initial balance: "))

    def debit_from(self, amount):
        self.balance = self.balance - amount

    def credit_to(self, amount):
         self.balance = self.balance + amount

    def display_all(self):
        print(self.cid)
        print(self.acc_no)
        print(self.cname)
        print(self.phone)
        print(self.emailid)
        print(self.balance)

#Main Code
c1 = Customer()
c2 = Customer()

c1.create_customer()
c2.create_customer()

c1.display_all()
c2.display_all()

c1.debit_from(100)
c1.display_all()

c2.credit_to(100)
c2.display_all()