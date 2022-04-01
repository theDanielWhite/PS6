# Classes

from library import Library

library = Library()
cont = True
while cont:
    print('          Library          \n' 
          '----------------------------\n' 
          'What would you like to do?   \n' 
          ' 1. Add a book               \n' 
          ' 2. Remove a book            \n' 
          ' 3. Display All Books        \n' 
          ' 4. Search for book by ISBN  \n' 
          ' 5. Search for book by Author \n'
          ' 6. Search for book by price  \n'
          ' 7. Exit Library              \n')
    option = int(input('Enter an option with the corresponding number: '))
    if option == 1:
        library.add_book()
    elif option == 2:
        library.remove_book()
    elif option == 3:
        print(f'\n{library}')
    elif option == 4:
        library.isbn_search()
    elif option == 5:
        library.author_search()
    elif option == 6:
        library.price_search()
    elif option == 7:
        print('Have a good day! \n')
        cont = False
    else:
        raise ValueError('Your input was invalid.')
