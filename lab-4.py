import pickle
class Customer:
    def __init__(self):
        self.cid = ""
        self.acc_no = ""
        self.cname = ""
        self.phone = ""
        self.email_id = ""
        self.balance = 0.0
        self.cards = []

    def create_customer(self):
        self.cid = input("Enter Customer ID: ")
        self.acc_no = input("Enter Account Number: ")
        self.cname = input("Enter Customer Name: ")
        self.phone = input("Enter Phone Number: ")
        self.email_id = input("Enter Email: ")
        self.balance = float(input("Enter initial balance: "))
        self.cards = []

    def debit_from(self, amount):
        self.balance = self.balance - amount

    def credit_to(self, amount):
         self.balance = self.balance + amount

    def display_all(self):
        print(self.cid)
        print(self.acc_no)
        print(self.cname)
        print(self.phone)
        print(self.email_id)
        print(self.balance)

    def assign_card(self, card):
        self.cards.append(card)

class Card:
    def __init__(self):
        self.type = ""
        self.card_no = ""
        self.cvv = ""
        self.expiry_date = ""
        self.c_balance = 0.0

    def add_card(self):
        self.type = input("Enter Card Type: ")
        self.card_no = input("Enter Card Number: ")
        self.cvv = input("Enter CVV: ")
        self.expiry_date = input("Enter Expiration Date: ")
        self.c_balance = float(input("Enter Balance: "))

    def display_card(self):
        print(self.type)
        print(self.card_no)
        print(self.cvv)
        print(self.expiry_date)
        print(self.c_balance)



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

while True:
    print("1. Create Customer ")
    print("2. Create Card ")
    print("3. Transfer funds ")
    print("4. Assign Card to customer ")
    print("5. Display Customer Info ")
    print("6. Display Card Info ")
    print("7. Commit ")
    print("8. Exit ")

    option = input("Select Option: ")

    if option == "7":
        f1 = open("customer_info.dat", "ab")
        pickle.dump(customer, f1)
        f1.close()