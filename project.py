class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    is_borrowed = False
    
b1 = Book("Harry Potter 1", "J.K Rowling")
b2 = Book("Harry Potter 2", "J.K Rowling")
b2 = Book("Harry Potter 3", "J.K Rowling")

def borrow():
    borrowed = input("Press 1, 2 or 3 to borrow either Harry Potter 1, 2 or 3 ")
    if borrowed == 1:
        is_borrowed = True
        print("Harry Potter 1 has been borrowed")
    elif borrowed == 2:
        is_borrowed = True
        print("Harry Potter 2 has been borrowed")
    if borrowed == 3:
        is_borrowed = True
        print("Harry Potter 3 has been borrowed")
    
def returns():
    returned = input("Press 1, 2 or 3 to return either Harry Potter 1, 2 or 3 ")
    if returned == 1:
        if is_borrowed is False:
            print("This book has not been borrowed")     
        else: 
            is_borrowed = False
            print("Harry Potter 1 has been returned")
    elif returned == 2:
        if is_borrowed is False:
          print("This book has not been borrowed")     
        else: 
            is_borrowed = False
            print("Harry Potter 2 has been returned")
    elif returned == 3:
        if is_borrowed is False:
            print("This book has not been borrowed")     
        else: 
            is_borrowed = False
            print("Harry Potter 3 has been returned")
            
borrow()
returns()


        