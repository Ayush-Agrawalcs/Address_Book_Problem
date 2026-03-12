from Address_Book import address_book
from Contact import contact
from Helper.Edit import edit

from Helper.Delete import delete


book = address_book()

while(True):
    First_Name=input("Enter your first name:")
    Last_Name=input("Enter your Last name:")
    Address=input("Enter your address:")
    City=input("Enter your city:")
    State=input("Enter your state:")
    Zip=input("Enter your zip code:")
    Phone_Number=input("Enter your phone number:")
    Email=input("Enter your email:")


    c1 = contact(
        First_Name,
        Last_Name,
        Address,
        City,
        State,
        Zip,
        Phone_Number,
        Email
    )
    book.add_contact(c1)
    print("Contact added successfully!")
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
            edit(book,name) 
            book.display_contacts()
            print("------------------------")
        case 3:            
            name=input("Enter the name of the contact you want to delete:")
            delete(book,name)
        case 0:
            break

    k=input("Enter N to Exit ")
    if k.lower()=='n':
        break