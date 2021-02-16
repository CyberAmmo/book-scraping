import re
from bs4 import BeautifulSoup

from locators.all_books_page import AllBooks
from parsers.book_parser import BookParser


class BooksPage:
    def __init__(self, books):
        self.soup = BeautifulSoup(books, 'html.parser')

    @property
    def books(self):
        locator = AllBooks.BOOKS
        all_books = self.soup.select(locator)
        return [BookParser(e) for e in all_books]
        
    @property
    def page_count(self):
        content = self.soup.select_one(AllBooks.PAGE).string
        pattern = 'Page [0-9] of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        return pages