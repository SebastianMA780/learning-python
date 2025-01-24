class Publication:
		def __init__(self, title, author):
			self.title = title
			self.author = author
			self.available = True
			self._protected = "protected variable" # this is protected and can be accessed outside the class. But it's a convention to not access it outside the class
			self.__private = "private variable" # this is private and can't be accessed outside the class

		def borrow(self, itemName = ""):
			if self.available:
				print(f"{itemName} {self.title} by {self.author} is borrowed")
				self.available = False
			else:
				print(f"Sorry, the {itemName} is not available")

		def return_book(self, itemName = ""):
			if not self.available:
				print(f"{itemName} {self.title} by {self.author} is returned")
				self.available = True
			else:
				print(f"The {itemName} is already available")

class Book(Publication):
		def borrow(self):
			super().borrow("Book")

		def return_book(self):
			super().return_book("Book")

class Magazine(Publication):
		def borrow(self):
			if self.available:
				print(f"Magazine {self.title} by {self.author} is borrowed")
				self.available = False
			else:
				print("Sorry, the Magazine is not available")

class User:
		def __init__(self, name, user_id):
			self.name = name
			self.user_id = user_id
			self.borrowed_books = []

		def borrow_book(self, book):
			if book.available:
				self.borrowed_books.append(book)
				book.borrow()
			else:
				print(f"Sorry, the book {book.title} is not available")
			
		def return_book(self, book):
			if book in self.borrowed_books:
				self.borrowed_books.remove(book)
				book.return_book()
			else:
				print(f"Sorry, the book {book.title} is not borrowed by you")

class Library :
		def __init__(self):
			self.books = []
			self.users = []
		
		def add_book(self, book):
			self.books.append(book)
			print(f"Book {book.title} by {book.author} is added to the library")

		def register_user(self, user):
			self.users.append(user)
			print(f"User {user.name} is registered")

		def show_available_books(self):
			print("Available books in the library")
			for book in self.books:
				if book.available:
					print(f"{book.title} by {book.author}")


book1 = Book("The Alchemist", "Paulo Coelho")
book2 = Book("The Da Vinci Code", "Dan Brown")
book3 = Book("The Kite Runner", "Khaled Hosseini")

magazine1 = Magazine("National Geographic", "National Geographic Society")

user1 = User("Alice", 1)
user2 = User("Bob", 2)
user3 = User("Charlie", 3)

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.register_user(user1)
library.register_user(user2)
library.register_user(user3)

#show available books
library.show_available_books()

#borrow book
user1.borrow_book(book1)
user2.borrow_book(book2)
user3.borrow_book(book3)

#show available books
library.show_available_books()

### Static and class methods ###
class Order:

	global_tax_rate = 100

	#static methods allow to access the method without creating an object of the class
	@staticmethod
	def calculate_tax(amount, tax_rate):
		return amount * ( tax_rate / 100 )
	
	#class methods allow to access the class variables without creating an object of the class
	@classmethod
	def change_global_tax_rate(cls, new_tax_rate):
		cls.global_tax_rate = new_tax_rate

print(Order.calculate_tax(100, 5))
Order.change_global_tax_rate(10)
print(Order.global_tax_rate)
