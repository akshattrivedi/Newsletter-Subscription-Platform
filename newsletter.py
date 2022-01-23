from user import User
from category import Category

class NewsLetter:
    def __init__(self, newsId, categoryList, title, userId, price):
        self.newsId = newsId
        self.categoryList = categoryList
        self.title = title
        self.userId = userId
        self.price = price