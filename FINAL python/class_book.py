import random

class Book:
    def __init__(self, title, place, availability):       
        self.title = title
        self.place = place
        self.availability = availability
    
    def find_book(self):                                        #find where the book is stored. If its availible, show where; if not, tell that not
        if self.availability == 'available':
            self.place = random.randint(1, 10)
            print(f'The book "{self.title}" is stored in the bookplace {self.place}.')
        else:
            print(f'The book "{self.title}" is {self.availability} because it is out with reader')


    def borrow_self(self):                                       #nested function doing the borrowing from the book's side                                                                
        if self.availability == 'available':                     #needed for the Member's borrowing function,
            self.availability = 'not available'                  #better if not called
            return True
        else:
            return False

    def return_self(self):                                        #nested function doing returinig from the book's side 
        if self.availability == 'not available':                  #needed for the Member's returning function
            self.availability = 'available'                       #better if not called


class Member:
    def __init__(self, name):
        self.name = name
        self.has_book = []

    def take_book(self, book):                                  #function that checks the book is available and if it is, adds the book to the self.has_book array
        if book.borrow_self():
            self.has_book.append(book)
            print(f'The book "{book.title}" is added to {self.name}\'s reading list.')
        else:
            print(f'The book "{book.title}" is not available for borrowing.')

    def return_book(self, book):                                #function that removes books from the Member's has_book array                     
        if book in self.has_book:
            book.return_self()
            self.has_book.remove(book)
            print(f'The book "{book.title}" is removed from {self.name}\'s reading list.')
        else:
            print(f'The book "{book.title}" is not in {self.name}\'s reading list.')

    def show_books(self):                                       #function that shows books in the has_book aray
        if self.has_book:
            print(f"Books owned by {self.name}:")
            for book in self.has_book:
                print(f"- {book.title}")
        else:
            print(f"{self.name} does not have any books.")






