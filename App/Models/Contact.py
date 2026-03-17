class contact:
    '''
    - contact class
      -  first_name
      -  last_name
      -  address
      -  city
      -  state
      -  zip
      -  phone_number
      -  email
    '''
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip_code
        self.phone_number = phone_number
        self.email = email

    def display(self):
        '''
        Display User details
        '''
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Address:", self.address)
        print("City:", self.city)
        print("State:", self.state)
        print("Zip:", self.zip)
        print("Phone:", self.phone_number)
        print("Email:", self.email)

