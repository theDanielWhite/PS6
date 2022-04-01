from author import Author


class Book:
    def __init__(self):
        self.ISBN = None
        self.title = None
        self.authors = None
        self.price = None
        self.publisher = None
        self.publication_date = None

    def get_info_from_user(self):
        print('Please enter book details.')
        self.ISBN = input('Enter ISBN: ')
        self.title = input('Enter title: ')
        n_authors = int(input('How many authors are there? \n'))
        self.authors = [None] * n_authors
        for i in range(n_authors):
            author = Author()
            author.get_info_from_user()
            self.authors[i] = author
        self.publisher = input('Enter publisher: ')
        self.publication_date = input('Enter publication date: ')
        self.price = float(input('Enter price: '))
        print('\n')

    def __str__(self):
        authors_info = ''
        for author in self.authors:
            authors_info += str(author) + '\n'
        return f'ISBN: {self.ISBN} \n' \
               f'Title: {self.title} \n' \
               f'Authors: \n' \
               f'{authors_info} \n' \
               f'Publisher: {self.publisher} \n' \
               f'Publication Date: {self.publication_date} \n' \
               f'Price: {self.price} \n'

    def __eq__(self, other):
        return self.title == other.title \
               and self.authors == other.authors \
               and self.ISBN == other.ISBN \
               and self.publisher == other.publisher \
               and self.publication_date == other.publication_date \
               and self.price == other.price
