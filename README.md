# Library Management System

A simple Object-Oriented Python project that simulates a Library Management System.

## Features

### Book Management

* Add books
* Remove books
* Search books by ID
* Search books by title
* Search books by author
* View all books

### Member Management

* Add members
* Remove members
* View all members

### Book Issue & Return

* Issue books to members
* Return books
* Prevent issuing already issued books
* Prevent returning books that were not borrowed

### Borrowing Rules

* Maximum 3 books per member
* Cannot remove a member with borrowed books
* Cannot remove a book that is currently issued

### Data Persistence

* Automatic JSON save
* Automatic JSON load on startup

### Due Date System

* Stores issue date
* Stores due date
* Detects late returns

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* JSON File Handling
* Datetime Module

## Project Structure

```text
Library-Management-System/
│
├── main.py
├── library.json
└── README.md
```

## Classes

### Book

Represents a library book.

Attributes:

* book_id
* title
* author
* is_issued

Methods:

* issue_book()
* return_book()

### Member

Represents a library member.

Attributes:

* member_id
* name
* issued_books

Methods:

* borrow_book()
* return_book()
* view_books()

### Library

Manages books and members.

Methods:

* add_book()
* remove_book()
* add_member()
* remove_member()
* issue_book()
* return_book()
* search_book()
* search_book_by_title()
* search_book_by_author()
* save_data()
* load_data()

## Sample Usage

```python
lib = Library()

lib.add_book(
    Book(5614, "Harry Potter", "J.K. Rowling")
)

lib.add_member(
    Member(101, "Anwar")
)

lib.issue_book(101, 5614)
```

## Learning Outcomes

This project helped me practice:

* Classes and Objects
* Encapsulation
* Properties
* Composition
* Dictionaries
* File Handling
* JSON Serialization
* Date & Time Handling
* Basic Software Design

## Future Improvements

* Fine Calculation for Late Returns
* GUI using Tkinter
* SQLite Database Integration
* User Authentication
* Admin Dashboard

## Author

Anwar

BCA Graduate | MCA Final Year Student

Learning Python, Data Analysis, Machine Learning, and AI Development.
