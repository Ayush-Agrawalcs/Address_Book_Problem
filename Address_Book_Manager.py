from Address_Book import address_book
from Contact import contact
class address_book_manager:
    def __init__(self):
        self.address_book={}
        
    def add_addressbook(self,name):
        if name not in self.address_book:
            self.address_book[name]=address_book()
        else:
            print("Address book with this name already exists.")  


    def display(self):
        for k,v in self.address_book.items():
            print("Address Book Name:",k)
            v.display_contacts()
            print("--------------------------")
    
    def search_person(self,city,state):
        for k,v in self.address_book.items():
            for i in v.contact:
                if(i.city==city or i.state==state):
                    print(k,' : ',i.first_name)



        