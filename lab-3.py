class Book:
    def __init__(self):
        self.book_id = ""
        self.book_title = ""
        self.author_id = ""
        self.publisher = ""
        self.year_of_publication = ""
        self.available = True

    def create_book(self):
        self.book_id = input("Enter Book ID: ")
        self.book_title = input("Enter Book Title: ")
        self.author_id = input("Enter Author: ")
        self.publisher = input("Enter Publisher: ")
        self.year_of_publication = input("Enter Year of Publication: ")
        self.available = True

    def display_books(self):
        print("Book Name:", self.book_title)
        print("Author:", self.author_id)
        print("Publisher", self.publisher)
        print("Year of Publication:", self.year_of_publication)

class Author:
    def __init__(self):
        self.author_id = ""
        self.author_name = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.email = ""

    def display_author(self):
        print("Author name:", self.author_name)
        print("Affiliation:", self.affiliation)
        print("Country:", self.country)
        print("Phone Number:", self.phone)
        print("Email:", self.email)

    def add_author(self):
        self.author_id = input("Enter Author ID: ")
        self.author_name = input("Enter Author Name: ")
        self.affiliation = input("Enter Author Affiliation: ")
        self.country = input("Enter Country of Origin: ")
        self.phone = input("Enter Author Phone Number: ")
        self.email = input("Enter Author Email: ")

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
        self.user_id = input("Enter User ID: ")
        self.user_name = input("Enter User Name: ")
        self.password = input("Enter User Password: ")
        self.address = input("Enter User Address: ")
        self.phone = input("Enter User Phone Number: ")
        self.email = input("Enter User Email: ")

    def borrow_book(self, book):
        self.books_borrowed.append(book)

    def display_user(self):
        print("User ID:", self.user_id)
        print("User Name:", self.user_name)
        print("Password:", self.password)
        print("User Address:", self.address)
        print("User Phone Number:", self.phone)
        print("User Email:", self.email)
        if self.books_borrowed:
            print("Books being borrowed:")
            for b in self.books_borrowed:
                print("-", b.book_title)
        else:
            print("No books currently borrowed")

#Main Code
books = []
authors = []
users = []

while True:
    print("1. Add a Book")
    print("2. Add User")
    print("3. Add Author")
    print("4. Display Books")
    print("5. Display User")
    print("6. Display Authors")
    print("7. Borrow a Book")
    print("8. Exit")

    option = input("select option:")

    if option == "1":
        print("Enter Book details:")
        b = Book()
        b.create_book()
        books.append(b)

    if option == "2":
        u = User()
        u.add_user()
        users.append(u)

    if option == "3":
        a = Author()
        a.add_author()
        authors.append(a)

    if option == "4":
        print("Books:")
        for b in books:
            b.display_books()

    if option == "5":
        print("Users:")
        for u in users:
            u.display_user()

    if option == "6":
        print("Authors:")
        for a in authors:
            a.display_author()

    if option == "7":
        for u in users:
            print(u.user_name)
        print("Please choose the user of your choice: ")
        selected_user = input()

        real_user_info = None
        for u in users:
            if u.user_name == selected_user:
                real_user_info = u
                break

        for b in books:
            print(b.book_title)
        print("Please choose the book you would like to borrow: ")
        selected_book = input()

        real_book_info = None
        for b in books:
            if b.book_title == selected_book:
                real_book_info = b
                break

        if real_book_info:
            if real_book_info.available:
                real_user_info.borrow_book(real_book_info)
                real_book_info.available = False
            else:
                print("Sorry, that book is already being borrowed.")

    if option == "8":
        break
