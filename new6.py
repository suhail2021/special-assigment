class Book:
  def __init__(self, title, author, price):
      self.title = title
      self.author = author
      self.price=price

book1 = Book("Harry Potter", "JK Rowling", 180);
print(book1.title)
print(book1.author)
print(book1.price)