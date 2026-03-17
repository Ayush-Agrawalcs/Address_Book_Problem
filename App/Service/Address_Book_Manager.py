from App.Models.Address_Book import address_book
from App.Models.Contact import contact
from App.utils.Serching import Searching
class address_book_manager(Searching):
    def __init__(self):
        self.address_book={}
    def add_addressbook(self,name):
        '''
        Add a new address book
        '''
        if name not in self.address_book:
            self.address_book[name]=address_book()
        else:
            print("Address book with this name already exists.")  


    def display(self):
        '''
        display a new address book'''
       
        for k,v in self.address_book.items():
            print("Address Book Name:",k)
            v.display_contacts()
            print("--------------------------")
    
    
    
   


        