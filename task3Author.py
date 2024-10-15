class Author():
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book():
    def __init__(self,title, author):
        self.title = title
        self.author = author
    def get_info_book(self):
        print(f"{self.title} - {self.author.name}")
a = Author("Толстой", "Русский")
b = Book("Война и мир", a)
b.get_info_book()