import requests

from pages.books_page import BooksPage

url = requests.get('https://books.toscrape.com/').content
page = BooksPage(url)

books = page.books
# For Just getting the data
# for book in page.books:
#     print(book)