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

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "is_issued": self.is_issued
        }

    @classmethod
    def from_dict(cls, data):
        book = cls(
            data["book_id"],
            data["title"],
            data["author"]
        )
        if data["is_issued"]:
            book.issue_book()
        return book 