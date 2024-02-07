from class_book import Book
from class_book import Member


The_Catcher = Book('The Catcher in the Rye', 1, 'available')
The_Hobbit = Book('The Hobbit', 2, 'available')

Alice = Member("Alice")
Billie = Member("Billie")



The_Catcher.find_book()
The_Hobbit.find_book()

Alice.take_book(The_Catcher)
Billie.take_book(The_Hobbit)

Alice.show_books()                #show all books that Alice borrowed

Alice.return_book(The_Catcher)
Alice.return_book(The_Hobbit)     #attempt to return book that reader doesn't have

Alice.show_books()                #show the empty reading list
Alice.take_book(The_Hobbit)       #attempt to borrow a book that is not available


The_Catcher.find_book()           #check availability after return