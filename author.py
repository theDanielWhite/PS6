class Author:
    def __init__(self):
        self.Id = None
        self.name = None
        self.email = None

    def get_info_from_user(self):
        print('Please enter author details.')
        self.Id = input('Enter Id: ')
        self.name = input('Enter name: ')
        self.email = input('Enter email: ')

    def __str__(self):
        return f'Id: {self.Id} \n' \
               f'Name: {self.name} \n' \
               f'Email: {self.email} \n'
