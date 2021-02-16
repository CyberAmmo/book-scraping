import requests

from pages.books_page import BooksPage

page_url = requests.get('https://books.toscrape.com/').content
page = BooksPage(page_url)

books = page.books

for book in books:
    print(book)

# Scraping every pagination page and give us a best rating books
# for page_num in range(1, 50):
#     url = f'https://books.toscrape.com/catalogue/page-{page_num+1}.html'
#     page_url = requests.get(url).content
#     page = BooksPage(page_url)
#     books.extend(page.books)