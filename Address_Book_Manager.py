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
    
    def view_person(self,city,state):
        dict={}
        for k,v in self.address_book.items():
            dict_city={}
            dict_state={}
            for i in v.contact:
                if(i.city==city):
                    dict_city[i.city]=dict_city.get(i.city, []) + [i.first_name]
                if(i.state==state):
                    dict_state[i.state]=dict_state.get(i.state, []) + [i.first_name]
            dict[k]=[dict_city,dict_state]
            return dict
    
    def count_contact(self,city,state):
        count_city=0
        count_state=0
        for k,v in self.address_book.items():
            for i in v.contact:
                if(i.city==city):
                    count_city+=1
                if(i.state==state):
                    count_state+=1
        print("Number of contacts in city",city,":",count_city)
        print("Number of contacts in state",state,":",count_state)
    
    
   


        