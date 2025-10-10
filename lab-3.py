class Book:
    def __init__(self):
        self.book_id = ""
        self.book_title = ""
        self.author_id = ""
        self.publisher= ""
        self.year_of_publication = ""
        self.booklist = []

    def create_book(self):
        self.book_id = input("Enter Book ID:")
        self.book_title = input("Enter Book Title:")
        self.author_id = input("Enter Author:")
        self.publisher = input("Enter Publisher:")
        self.year_of_publication = input("Enter Year of Publication:")

    def display_books(self):
        for b in self.booklist:
            print(b.book_name)

class Author:
    def __init__(self):
        self.author_id = ""
        self.author_name = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.email = ""

    def add_author(self):
        self.author_id = input("Enter Author ID:")
        self.author_name = input("Enter Author Name:")
        self.affiliation = input("Enter Author Affiliation:")
        self.country = input("Enter Country of Origin:")
        self.phone = input("Enter Author Phone Number:")
        self.email = input("Enter Author Email:")

class User:
    def __init__(self):
        self.user_id = ""
        self.user_name = ""
        self.password = ""
        self.address = ""
        self.phone = ""
        self.email = ""
        self.books_borrowed = []

    def add_user(self):
        self.user_id = input("Enter User ID:")
        self.user_name = input("Enter User Name:")
        self.password = input("Enter User Password:")
        self.address = input("Enter User Address:")
        self.phone = input("Enter User Phone Number:")
        self.email = input("Enter User Email:")

    def borrow_book(self, b1):
        self.books_borrowed.append(b1)

    def display_user(self):
        print("User ID:", self.user_id)
        print("User Name:", self.user_name)
        print("Password:", self.password)
        print("User Address:", self.address)
        print("User Phone Number:", self.phone)
        print("User Email:", self.email)
        for x in self.books_borrowed:
            print("Books Borrowed:", x.book_name)
#Main Code
while True:
    print("1. Add a Book")
    print("2. Add User")
    print("3. Add Author")
    print("4. Display Books:")
    print("5. Display User:")
    print("6. Borrow a Book")

    option = input("select option:")

    if option == "1":
        b1 = Book()
        b1.create_book()

    if option == "2":
        u1 = User()
        u1.add_user()

    if option == "3":
        a1 = Author()
        a1.add_author()

    if option == "4":
        b1 = Book()
        b1.display_books()