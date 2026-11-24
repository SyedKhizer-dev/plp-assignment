class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, author, year, pages, genre):
        super().__init__(title, author, year)
        self.pages = pages
        self.genre = genre

    def describe(self):
        print("Book")
        print(self.title)


class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue_number, is_monthly):
        super().__init__(title, author, year)
        self.issue_number = issue_number
        self.is_monthly = is_monthly

    def describe(self):
        print("Magazine")


book1 = Book("abc", "xyz", 2020, 200, "qwe")
mag1 = Magazine("xyz", "abc", 2022, 300, False)

list1 = [book1, mag1]

print(type(list1))

for i in list1:
    i.describe()
