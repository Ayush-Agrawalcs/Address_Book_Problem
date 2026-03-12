print("Welcome to the Address Book!")
from Contact import contact

class address_book:
    def __init__(self,name):
        self.name=name
        self.contact=[]
        
    def add_contact(self,contact):
        self.contact.append(contact)


    def display_contacts(self):
        for contact in self.contact:
            contact.display()
            print("-------------")


