class Sorting:
    def sort_alphabetically(self):
        '''
        Sorting alphabetically '''
        self.contact.sort(key=lambda x: x.first_name)
    
    def sort_city_state_zip(self,k):
        '''
        sort by a ciry,zipcode or state'''
        match k:
            case 1:
                self.contact.sort(key=lambda x: x.city)
            case 2:
                self.contact.sort(key=lambda x: x.state)
            case 3:
                self.contact.sort(key=lambda x: x.zip)