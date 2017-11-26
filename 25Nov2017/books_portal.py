"""
Portal to add and view book and price details
"""


class Book(object):
    """
    A simple representation of book

    :param name: title, title of the book
    :param name: pages, number of pages in the book
    :param name: price, price of the book
    """

    def __init__(self, title, pages, price):
        self.title, self.pages, self.price = title, pages, price

    def __str__(self):
        return "\tTitle: %s\n\tPages: %d\n\tPrice: %.2f\n" %\
            (self.title, self.pages, self.price)

    __repr__ = __str__


class Books(object):
    """
    A simple representation of book collection
    """

    collection = []

    def __str__(self):
        return show_books(self.collection)

    __repr__ = __str__


def show_books(book_collection):
    """
    return printable string for books in collection
    """
    all_books = ""

    if book_collection:  # using implicit booleanness of empty list
        for index, book in enumerate(book_collection):
            all_books += "Book " + str(index + 1) + "\n"
            all_books += str(book)
    else:
        all_books = "No books in collection\n"

    return all_books

ALL_BOOKS = Books()


def main():
    """
    running the book portal
    """
    print "\n" + "\n".join([
        "1. Enter book",
        "2. List all books",
        "3. Search book for price range",
        "4. List unique prices",
        "5. Exit\n"
    ])
    choice = int(raw_input("Please enter choice: "))

    if choice == 1:
        title = raw_input("Title: ")
        pages = int(raw_input("Pages: "))
        price = float(raw_input("Price: "))
        ALL_BOOKS.collection.append(Book(title, pages, price))
        main()
    elif choice == 2:
        print ALL_BOOKS
        main()
    elif choice == 3:
        price_range = float(raw_input("Price Range: "))
        print show_books(
            [book for book in ALL_BOOKS.collection
             if book.price <= price_range]
            )
        main()
    elif choice == 4:
        print "\n".join(
            {str(book.price) for book in ALL_BOOKS.collection}
            )
        main()
    elif choice == 5:
        print "Thank you for using Book Portal"
    else:
        print "Invalid choice. Please select from the given choices."
        main()

if __name__ == "__main__":
    main()
