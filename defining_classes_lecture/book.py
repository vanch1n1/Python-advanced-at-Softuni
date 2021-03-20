class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

book = Book('Game of thrones', 'Martin', 500)
print(book.name)