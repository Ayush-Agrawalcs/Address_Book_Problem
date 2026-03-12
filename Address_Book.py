print("Welcome to the Address Book!")

class contact:
    def __init__(self,first_name,last_name,address,city,state,zip,phone_number,email):
        self.first_name=first_name
        self.last_name=last_name
        self.address=address
        self.city=city
        self.state=state
        self.zip=zip
        self.phone_number=phone_number
        self.email=email
    def display(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Address:", self.address)
        print("City:", self.city)
        print("State:", self.state)
        print("Zip:", self.zip)
        print("Phone:", self.phone_number)
        print("Email:", self.email)

class address_book:
    def __init__(self):
        self.contact=[]
    def add_contact(self,contact):
        self.contact.append(contact)
    def display_contacts(self):
        for contact in self.contact:
            contact.display()
            print("-------------")


book = address_book()

c1 = contact(
    "Ayush",
    "Agrawal",
    "FF Road",
    "Firozabad",
    "Uttar Pradesh",
    "283203",
    "9045735010",
    "ayu@gmail.com"
)

book.add_contact(c1)
book.display_contacts()
