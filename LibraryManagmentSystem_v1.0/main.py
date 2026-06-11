class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.__is_issued = False
    
    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"""Book ID: {self.book_id}
Title: {self.title}
Author: {self.author}
Status: {status}"""

    @property
    def is_issued(self):
        return self.__is_issued

    def issue_book(self):
        if self.is_issued:
            return False
        self.__is_issued = True
        return True
        
    
    def return_book(self):
        if not self.is_issued:
            return False
        self.__is_issued = False
        return True
    

# b1 = Book(5614, "Harry Potter", "Abrahim Lincon", False)
# b2 = Book(8668, "Iron Man", "Tony Stark", False)

# print("Book Issued!" if b1.issue_book() else "The Book is not Available")
# print("Book Issued!" if b1.issue_book() else "The Book is not Available")
# print("Book Returned!" if b2.return_book() else "The Book was never issued!")

    
class Member:
    MAX_BOOKS = 3
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.issued_books = []
        
    def __str__(self):
        return f"""Member ID: {self.member_id}
Name: {self.name}
Book Issued: {"No Record" if not self.issued_books else [book.title for book in self.issued_books]}"""

    def borrow_book(self, book):
        if isinstance(book, Book) and len(self.issued_books) >=  self.MAX_BOOKS:
            if book.issue_book():
                self.issued_books.append(book)
                return True
        return False
    
    def return_book(self, book):
        if isinstance(book, Book) and book in self.issued_books:
            self.issued_books.remove(book)
            book.return_book()
            return True
        return False
    
    def view_books(self):
        if not self.issued_books:
            print("No books borrowed")
            return

        for book in self.issued_books:
            print(book.title)
    
# m1 = Member(123, "Anwar")
# print(m1.borrow_book(b2))
# print(m1.return_book(b2))

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
    def add_book(self, book):
        if isinstance(book, Book) and book.book_id not in self.books:
            self.books[book.book_id] = book
            return True
        return False
    
    def remove_book(self, book_id):
        if book_id in self.books:
            if self.books[book_id].is_issued:
                print("Book is currently issued.")
                return False
            del self.books[book_id]
            return True
        return False
    
    def add_member(self, member):
        if isinstance(member, Member) and member.member_id not in self.members:
            self.members[member.member_id] = member
            return True
        return False
    
    def remove_member(self, member_id):
        if member_id in self.members:
            if self.members[member_id].issued_books:
                print("Member has borrowed books.")
                return False
            del self.members[member_id]
            return True
        return False
    
    def search_book(self, book_id):
        if book_id in self.books:
            return self.books.get(book_id)

    def search_book_by_author(self, author):
        return [book for book in self.books.values() if author.lower() == book.author.lower()]
        
    def search_book_by_title(self, title):
        return [book for book in self.books.values() if title.lower() == book.title.lower()]
    
    def issue_book(self, member_id, book_id):
        if member_id in self.members and book_id in self.books:
            if self.members[member_id].borrow_book(self.books[book_id]):
                return True
        return False
    
    def return_book(self, member_id, book_id):
        if member_id in self.members and book_id in self.books:
            if self.members[member_id].return_book(self.books[book_id]):
                return True
        return False
    
    def view_all_books(self):
        if not self.books:
            print("No Book Record!")
        for book in self.books.values():
            print(book)
    
    def view_all_members(self):
        if not self.members:
            print("No member Record!")
        for member in self.members.values():
            print(member)
    
if __name__ == "__main__":
    lib = Library()
    lib.add_book(Book(5614, "Harry Potter", "Abrahim Lincon"))
    lib.add_book(Book(8668, "Iron Man", "Tony Stark"))

    lib.add_member(Member(113, "Prakhar"))
    lib.add_member(Member(123, "Anwar"))

    # lib.search_book(5614)
    # lib.issue_book(113, 5614)
    # lib.issue_book(123, 8668)
    # lib.return_book(113, 5614)
    # lib.view_all_books()
    # lib.view_all_members()
    
    book = lib.search_book_by_author("Tony Stark")
    if book: print(book)
    book = lib.search_book_by_title("Harry Potter")
    if book: print(book)