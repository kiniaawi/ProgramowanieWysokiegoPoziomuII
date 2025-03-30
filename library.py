class Library:
    def __init__(self, books):
        self.books = books

    def find_book(self, isbn):
        for book in self.books:
            if book["ISBN"] == isbn:
                return print(f"\nZnaleziona ksiazka: {book["title"]}")
            else:
                return print("No book found")

