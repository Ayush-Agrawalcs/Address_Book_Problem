# Address Book Management System

## Introduction

Refactored Python application for managing multiple address books and contacts. Code divided into modular packages: Models (data classes), Service (business logic), utils (I/O), with clean imports and bug fixes.

Supports persistent storage in TXT, CSV, JSON formats.

## Features

* Multiple address books
* Add/Edit/Delete contacts (dedup by first name)
* Display/sort contacts (alpha, city/state/zip)
* Search/view/count by city/state
* Save/Load to/from TXT/CSV/JSON
* Robust CLI with book selection

## Project Structure

```
AddressBook/
├── Address_book_main.py          # CLI entrypoint
├── App/
│   ├── Models/                   # Data classes
│   │   ├── __init__.py
│   │   ├── Contact.py
│   │   └── Address_Book.py
│   ├── Service/                  # Business logic
│   │   ├── __init__.py
│   │   └── Address_Book_Manager.py
│   └── utils/                    # File I/O handlers
│       ├── __init__.py
│       └── file_handler.py
├── Data/                         # Storage (address_book.txt/csv/json)
├── TODO.md                       # Refactor progress
├── Readme.md
└── .gitignore
```

## How to Run

```bash
python Address_book_main.py
```

Follow interactive menu. Select book before contact ops/I/O.

## Technologies

* Python 3 (stdlib: json, os, pathlib)

## Design Principles

* **Modularity/SRP**: Separate concerns (data, logic, I/O)
* **Relative imports** & packages
* **Error handling** (try/except, checks)
* **Tested** refactors preserve functionality

