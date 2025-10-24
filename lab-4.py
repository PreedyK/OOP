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

    def display_customer(self):
        print(self.cid)
        print(self.acc_no)
        print(self.cname)
        print(self.phone)
        print(self.email_id)
        print(self.balance)
        if self.cards:
            print("Assigned Cards:")
            for card in self.cards:
                print(card.card_no, card.type)
        else:
            print("No cards assigned.")

    def assign_card(self, card):
        self.cards.append(card)
        print("Card", card.card_no, "assigned to", self.cname)

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
customers = []
cards = []

def find_customer(customers, cid):
    for c in customers:
        if c.cid == cid:
            return c
    return None


def find_card(cards, card_no):
    for card in cards:
        if card.card_no == card_no:
            return card
    return None

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

    if option == "1":
        c = Customer()
        c.create_customer()
        customers.append(c)
        print("Customer ", c.cname, "added.")

    if option == "2":
        card = Card()
        card.add_card()
        cards.append(card)
        print("Card ", card.card_no, "added")

    if option == "3":
        sender_id = input("Enter Sender Customer ID: ")
        receiver_id = input("Enter Receiver ID: ")
        sender = find_customer(customers, sender_id)
        receiver = find_customer(customers, receiver_id)
        if sender and receiver:
            amount = float(input("Enter amount to Transfer: "))
            if sender.balance  >= amount:
                sender.debit_from(amount)
                receiver.credit_to(amount)
                print("Transferred", amount, "from", sender.cname, "to", receiver.cname)


    if option == "4":
        cid = input("Enter Customer ID: ")
        card_no = input("Enter Card Number to assign: ")
        customer = find_customer(customers, cid)
        card = find_card(cards, card_no)
        if customer and card:
            customer.assign_card(card)
        else:
            print("Invalid Customer ID or Card Number!")

    if option == "5":
        cid = input("Enter Customer ID: ")
        customer = find_customer(customers, cid)
        if customer:
            customer.display_customer()
        else:
            print("Customer not Found!")

    if option == "6":
        card_no = input("Enter Card Number: ")
        card = find_card(cards, card_no)
        if card:
            card.display_card()
        else:
            print("Card not Found!")

    if option == "7":
        with open("customer_data.dat", "wb") as f:
            pickle.dump(customers, f)
        with open("card_data.dat", "wb") as f:
            pickle.dump(cards, f)
        print("All data saved successfully")

    if option == "8":
        break
