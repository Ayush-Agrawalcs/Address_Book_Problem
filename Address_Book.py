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
