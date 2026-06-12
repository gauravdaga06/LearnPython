from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int

    def summary(self):
        return f"{self.title} by {self.author}, {self.pages} pages."

book = Book ("Hello World", "Gaurav" , 305)
print(book.summary())

print(book)
print (book==Book("Hello World", "Gaurav" , 305))