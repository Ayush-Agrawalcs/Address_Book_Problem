from Address_Book import address_book
from Contact import contact
from Helper.Edit import edit

from Helper.Delete import delete

book = address_book("b1")
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
print("--------------")

book.add_contact(c1)
book.display_contacts()

s=input("you want to edit y/n")
if(s.lower()=='y'):
    name=input("Enter the name of the contact you want to edit:")
    edit(book,name)
book.display_contacts()


print("---------")
s=input("you want to Delete y/n")
if(s.lower()=='y'):
    name=input("Enter the name of the contact you want to edit:")
    delete(book,name)
