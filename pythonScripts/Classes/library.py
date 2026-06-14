from dataclasses import dataclass

@dataclass
class Book :
    title : str
    author : str
    pages : int


class BookNotFoundError(Exception):
    pass

class Library: 
    def __init__(self , books=None):
        self.books = books if books is not None else []
    
    def add_book(self, book:Book) -> None :
        self.books.append(book)
    

    def find_by_author(self , author:str) -> list[Book]:
        return [book for book in self.books if book.author == author]
    
    def get_longest(self) -> Book:
        if not self.books:
            raise BookNotFoundError("Book NOt found")
        return max(self.books, key=lambda book: book.pages)

if __name__ == "__main__":
    lib = Library()
    try:
        print(lib.get_longest())
    except BookNotFoundError:
        print("Book Not available")

    lib.add_book(Book("title", "GD" , 123))
    lib.add_book(Book("title 2", "Author 2 ",159))
    lib.add_book(Book("title 3", "Author 3", 753))

    print(lib.find_by_author("GD"))
    print(lib.get_longest())

    
    


    
        