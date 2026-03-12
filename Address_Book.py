print("Welcome to the Address Book!")
from Contact import contact

class address_book:
    def __init__(self,name):
        self.name=name
        self.contact=[]
        
    def add_contact(self,contact):
        for con in self.contact:
            if con.first_name==contact.first_name:
                print("Contact with this name already exists.")
                return
        self.contact.append(contact)


    def display_contacts(self):
        for contact in self.contact:
            contact.display()
            print("-------------")


