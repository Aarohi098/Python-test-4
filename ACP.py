class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(self.title, " is already borrowed")
        else:
            self.is_borrowed = True
            print(self.title, " has been borrowed")

    def return_book(self):
        if not self.is_borrowed:
            print(self.title, " has not been checked out")
        else:
            self.is_borrowed = False
            print(self.title , " has been returned ")

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} ({status})"


book1 = Book("Harry Potter 1", "J.K. Rowling")
book2 = Book("Harry Potter 2", "J.K. Rowling")

print(book1) 

book1.borrow()
print(book1)

book1.borrow()

book1.return_book()
print(book1)
