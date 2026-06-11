import json
from member import Book, Member
from datetime import datetime, timedelta
class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.issue_records = {}
        self.load_data()
    def add_book(self, book):
        if isinstance(book, Book) and book.book_id not in self.books:
            self.books[book.book_id] = book
            self.save_data()
            return True
        return False
    
    def remove_book(self, book_id):
        if book_id in self.books:
            if self.books[book_id].is_issued:
                print("Book is currently issued.")
                return False
            del self.books[book_id]
            self.save_data()
            return True
        return False
    
    def add_member(self, member):
        if isinstance(member, Member) and member.member_id not in self.members:
            self.members[member.member_id] = member
            self.save_data()
            return True
        return False
    
    def remove_member(self, member_id):
        if member_id in self.members:
            if self.members[member_id].issued_books:
                print("Member has borrowed books.")
                self.save_data()
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
                self.issue_records[book_id] = {
                    "member_id": member_id,
                    "issue_date":
                        datetime.now().strftime("%Y-%m-%d"),
                    "due_date":
                        (
                            datetime.now()
                            + timedelta(days=14)
                        ).strftime("%Y-%m-%d")
                }
                self.save_data()
                return True
        return False
    
    def return_book(self, member_id, book_id):
        if member_id in self.members and book_id in self.books:
            if self.members[member_id].return_book(self.books[book_id]):
                record = self.issue_records[book_id]
                due_date = datetime.strptime(record["due_date"], "%Y-%m-%d")
                if datetime.now() > due_date:
                    days_late = (datetime.now() - due_date).days
                    fine = days_late * 10
                    print("You have to pay the fine: ", fine)
                self.save_data()
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

    def save_data(self):
        data = {
            "books": {
                bid: book.to_dict() for bid, book in self.books.items()
            },
            "members": {
                mid: member.to_dict() for mid, member in self.members.items()
            },
            "issue_records": self.issue_records
        }
        with open("library.json", "w") as f:
            json.dump(data, f, indent=4)
       
    def load_data(self):
        try:
            with open("library.json", "r") as f:
                data = json.load(f)
            # Load Books
            for book_data in data["books"].values():
                book = Book.from_dict(book_data)
                self.books[book.book_id] = book
            # Load Members
            for member_data in data["members"].values():
                member = Member(member_data["member_id"],member_data["name"])
                # Restore borrowed books
                for book_id in member_data["issued_books"]:
                    if book_id in self.books:
                        member.issued_books.append(
                            self.books[book_id]
                        )
                self.members[member.member_id] = member
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print("Error loading library data. Data may be corrupted.")
        