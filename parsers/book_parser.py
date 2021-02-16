import re

from locators.book_locators import BookLocators


class BookParser:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name}, £{self.price} got {self.rating} stars rating>'

    @property
    def name(self):
        locator = BookLocators.NAME
        item_link =  self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = BookLocators.LINK
        item_link =  self.parent.select_one(locator)
        item_name = item_link.attrs['href']
        return item_name

    @property
    def price(self):
        locator = BookLocators.PRICE
        item_price =  self.parent.select_one(locator).string
        
        pattern = '£([0-9]+\.[0-9+])'
        matcher = re.search(pattern, item_price)
        return float(matcher.group(1))

    @property
    def rating(self):
        locator = BookLocators.RATING
        star_rating_tag =  self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        rating_num = BookParser.RATINGS.get(rating_classes[0])
        return rating_num