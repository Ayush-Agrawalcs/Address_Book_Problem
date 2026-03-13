from Address_Book import address_book
from Address_Book_Manager import address_book_manager
from Contact import contact

books=address_book_manager()

while(True):
    name=input("Enter the name of the address book you want to create:")
    if name not in books.address_book:
           
            books.add_addressbook(name)

    book = books.address_book[name]
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
display_address_book=input("Do you want to display all address books? (Y/N): ")
if display_address_book.lower()=='y':
    books.display()

display_search=input("Do you want to view a person on the basis of city and state (Y/N): ")
if display_search.lower()=='y':
    city=input("Enter city: ")
    state=input("Enter state: ")
    books.search_person(city,state)

view_person=input("Do you want to view a person on the basis of city and state (Y/N): ")
if view_person.lower()=='y':
    city=input("Enter city: ")
    state=input("Enter state: ")
    view_dict=books.view_person(city,state)
    print(view_dict)


view_person=input("Do you want to view a person on the basis of city and state (Y/N): ")
if view_person.lower()=='y':
    city=input("Enter city: ")
    state=input("Enter state: ")
    view_dict=books.view_person(city,state)
    print(view_dict)


count_contact=input("Do you want to count contacts in a city and state (Y/N): ")
if count_contact.lower()=='y':
    city=input("Enter city: ")
    state=input("Enter state: ")
    books.count_contact(city,state)