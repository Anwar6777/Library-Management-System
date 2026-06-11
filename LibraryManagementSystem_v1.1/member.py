from book import Book
from datetime import datetime, timedelta
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
        if isinstance(book, Book) and len(self.issued_books) <  self.MAX_BOOKS:
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

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "issued_books": [
                book.book_id
                for book in self.issued_books
            ],
        }
            # "issue_date": datetime.now().strftime("%Y-%m-%d"),
            # "due_date": (datetime.now()+ timedelta(days=14)).strftime("%Y-%m-%d")