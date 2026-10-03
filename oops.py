# class Student:

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
        
        

#     def avg(self):
#         total  = 0
#         for i in self.marks:
#             total += i
#         print(f"{self.name} you got an average of {total/len(self.marks)}")





# s1 = Student("ben",[88,89,90])
# s1.avg()
        

# class Account:
#     def __init__(self,bal,acc_no):
#         self.bal = bal
#         self.acc_no = acc_no

#     def debit(self,amount):
#         self.bal -= amount
#         print(f"Rs {amount} was debited from your account ")
#         print(f"Total balance is {self.get_bal()}")
#     def credit(self,amount):
#         self.bal += amount
#         print(f"Rs {amount} was credited to your account ")
#         print(f"Total balance is {self.get_bal()}")
#     def get_bal(self):
#             return self.bal    
        

    

# acc1 =Account(10000,7896)
# acc1.debit(100)
# acc1.credit(300000)   

# class Smartdevice:

#     def __init__(self,name):
#         self.name=name
#         self.__is_on = False

#     def status(self):
#         return self.__is_on

#     def toggle(self):
#         if self.__is_on == False:
#             self.__is_on == True
#             print(f"{self.name} is powered on")
#         else:
#             self.__is_on == False
#             print(f"{self.name} powered off")  

# class Securitycamera(Smartdevice):
#     def record(self):
#         if self.status == True:
#             print("recording video")
#         else:
#             print("offline,cant be recorded")    
# cam1 = Securitycamera("balcony")
# cam1.toggle()
# cam1.record()

class LibraryError(Exception):
    """Custom exception for all library-related errors."""
    pass


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        # Encapsulation: The availability state is hidden from direct outside modification
        self._is_available = True  

    @property
    def is_available(self):
        """Read-only property to check availability safely."""
        return self._is_available

    def borrow(self):
        if not self._is_available:
            raise LibraryError(f"Book '{self.title}' is currently unavailable.")
        self._is_available = False

    def return_book(self):
        self._is_available = True

    def __str__(self):
        status = "Available" if self._is_available else "Borrowed"
        return f"{self.title} by {self.author} ({status})"


class Member:
    max_books = 2  # Class attribute shared by all base members

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        # Encapsulation: The member's borrowed books are kept private
        self._borrowed = [] 

    def borrow(self, book):
        if len(self._borrowed) >= self.max_books:
            raise LibraryError(f"{self.name} has reached the borrowing limit of {self.max_books}.")
        
        # This will raise a LibraryError if the book is already taken
        book.borrow()  
        self._borrowed.append(book)

    def get_fee(self):
        return 10  # Standard base fee


# Inheritance: StudentMember copies Member traits but modifies specific rules
class StudentMember(Member):
    max_books = 3

    # Polymorphism: Overriding the base method to return a different fee
    def get_fee(self):
        return 0


# Inheritance: PremiumMember copies Member traits but modifies specific rules
class PremiumMember(Member):
    max_books = 10

    # Polymorphism: Overriding the base method to return a different fee
    def get_fee(self):
        return 20


class Library:
    def __init__(self):
        self.books = []
        self.members = {}

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members[member.member_id] = member

    def checkout(self, member_id, isbn):
        if member_id not in self.members:
            raise LibraryError(f"Member ID {member_id} not found.")

        # Search for the book by ISBN
        target_book = None
        for book in self.books:
            if book.isbn == isbn:
                target_book = book
                break
                
        if not target_book:
            raise LibraryError(f"ISBN {isbn} does not belong to any library book.")

        # Delegate the actual borrowing logic to the specific member object
        member = self.members[member_id]
        member.borrow(target_book)

    def list_available(self):
        # A great place to use a list comprehension!
        return [book for book in self.books if book.is_available]


lib = Library()
lib.add_book(Book("1984", "George Orwell", "111"))
lib.add_book(Book("Dune", "Frank Herbert", "222"))
lib.add_member(StudentMember("Asha", "S1"))

lib.checkout("S1", "111")
lib.checkout("S1", "111")   # should raise LibraryError
print(lib.list_available())