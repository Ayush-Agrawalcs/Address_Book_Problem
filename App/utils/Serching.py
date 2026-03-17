class Searching:
    def search_person(self,city,state):
        '''
        Search a person by city or state'''
        for k,v in self.address_book.items():
            for i in v.contact:
                if(i.city==city or i.state==state):
                    print(k,' : ',i.first_name)
    
    def view_person(self,city,state):
        '''
        Maintain a dictionary to view a person by a city or state'''
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
    