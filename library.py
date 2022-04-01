from book import Book
from author import Author


class Library:
    def __init__(self):
        self.books = []
        self.isbn_lst = []
        self.authors = []
        self.ids = []
        self.prices = []

    def add_book(self):
        book = Book()
        author = Author()
        print('Please enter library contents.')
        book.get_info_from_user()
        if book.ISBN in self.isbn_lst:
            print('A book already exits with this ISBN.'
                  'Please try adding a different book.')
        elif author.Id in book.authors:
            print('This author has a different Id.'
                  'Please enter the correct Id')
        else:
            self.isbn_lst.append(book.ISBN)
            self.books.append(book)
            self.authors.append(book.authors)
            self.prices.append(book.price)
            self.ids.append(author.Id)

    def remove_book(self):
        isbn = input('Enter book ISBN: ')
        if isbn in self.isbn_lst:
            isbn_index = self.isbn_lst.index(isbn)
            self.books.remove(self.books[isbn_index])
        else:
            print('There is no book with that ISBN.\n')

    def display_library(self):
        return f'All Books: \n' \
               f'{self.books}'

    def isbn_search(self):
        isbn = input('Enter book ISBN: ')
        if isbn in self.isbn_lst:
            isbn_index = self.isbn_lst.index(isbn)
            print(self.books[isbn_index])
        else:
            print('Book could not be found.')

    def author_search(self):
        author = Author()
        book_author = author.get_info_from_user()
        print(f'Every book written by {author.name}: \n')
        for book in self.books:
            if book_author in book.authors:
                print(book)

    def price_search(self):
        price_range = int(input('I am looking for all books less than: $'))
        for book in self.books:
            price_index = self.prices.index(book.price)
            if price_range > self.prices[price_index]:
                print(self.books[price_index])

    def __str__(self):
        linebreak = '----------' * 5
        books_info = ''
        for book in self.books:
            books_info += str(book) + '\n'
        return f'Entire Library: \n' \
               f'{linebreak} \n' \
               f'{books_info} \n'
