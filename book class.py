# the Book class holds data about a book
class Book:
    #the __init__method initializes the attributes
    def __init__(self, book_title, author_name, publisher_name):
        self.__book_title = book_title
        self.__author_name = author_name
        self.__publisher_name = publisher_name

    def set_book_title(self, book_title):
        self.__book_title = book_title

    def set_author_name(self, author_name):
        self.__author_name = author_name

    def set_publishe_name(self, publisher_name):
        self.__publisher_name = publisher_name

#mutator method
    def get_book_title(self):
        return self.__book_title

    def get_author_name(self):
        return self.__author_name

    def get_publisher_name(self):
        return self.__publisher_name
def main():
    title = input("enter the book title:")
    a_name = input("enter the author name:")
    p_name = input("enter the publisher name:")

#create an instance of book class
    note = Book(title, a_name, p_name)
#display data that was entered
    print("here is the data that was entered:")
    print("Book Title:", note.get_book_title())
    print("Author Name:", note.get_author_name())
    print("Publisher Name:",(note.get_publisher_name()))
