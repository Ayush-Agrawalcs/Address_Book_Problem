from Address_Book import address_book
from Address_Book_Manager import address_book_manager
from Contact import contact

books=address_book_manager()

while(True):
    b=input("Enter the name of the address book you want to create:")
    if b not in books.address_book:
            books.add_addressbook(b)

    book = books.address_book[b]
    book.create_contact()
    print("1. Display Contacts")
    print("2. Edit Contact")
    print("3. Delete Contact")
    print("0. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            book.display_contacts()
            print("------------------------")
        case 2:
            name=input("Enter the name of the contact you want to edit:")
            book.edit(name) 
            book.display_contacts()
            print("------------------------")
        case 3:            
            name=input("Enter the name of the contact you want to delete:")
            book.delete(name)
        case 0:
            break

    k=input("Enter N to Exit ")
    if k.lower()=='n':
        break
y=input("Do you want to display all address books? (Y/N): ")
if y.lower()=='y':
    books.display()


