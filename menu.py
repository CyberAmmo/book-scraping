from app import books


USER_CHOICE = '''Enter one of the following:
 - 'b' to look best books
 - 'c' to look at the cheapest books
 - 'n' to get the next book on the page
 - 'q' to exit

Enter your choice: '''


def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating * -1)[:5]
    for book in best_books:
        print(book)


def cheapest_book():
    cheap_book = sorted(books, key=lambda x: x.price)[:5]
    for book in cheap_book:
        print(book)


books_generator = (x for x in books)

def get_next_book():
    print(next(books_generator))


def menu():
    user_imput = input(USER_CHOICE)
    while user_imput != 'q':
        if user_imput == 'b':
            print_best_books()
        elif user_imput == 'c':
            cheapest_book()
        elif user_imput == 'n':
            get_next_book()
        else:
            print('Please enter a valid command!')
        user_imput = input(USER_CHOICE)

menu()



