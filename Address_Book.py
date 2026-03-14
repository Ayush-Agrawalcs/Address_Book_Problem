print("Welcome to the Address Book!")
from Contact import contact

class address_book:
    def __init__(self):
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

    def create_contact(self):
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
        self.add_contact(c1)
        print("Contact added successfully!")
    

    def edit(self, name):
        for con in self.contact:

            if con.first_name == name:
                flag=True
                while(flag):
                    print("1. Edit First Name")
                    print("2. Edit Last Name")
                    print("3. Edit address")
                    print("4. Edit city")
                    print("5. Edit state")
                    print("6. Edit zip")
                    print("7. Edit phone_Number")
                    print("8. Edit Email")
                    print("0. quit")

                    status = int(input( "Enter your choice: "))

                    match status:

                        case 1:
                            new_first = input("Enter new first name: ")
                            con.first_name = new_first

                        case 2:
                            new_last = input("Enter new last name: ")
                            con.last_name = new_last
                        case 3:
                            new_add=input("Enter your address: ")
                            con.address=new_add
                        case 4:
                            new_city=input("Enter your city: ")
                            con.city=new_city
                        case 5:
                            new_state=input("Enter your new State: ")
                            con.state=new_state
                        case 6:
                            new_zip=input("Enter your new zip code: ")
                            con.zip=new_zip
                        case 7:
                            new_phone_number=input("Enter your phone no.:")
                            con.phone_number=new_phone_number
                        case 8:
                            new_email=input("Enter your email :")
                            con.email=new_email
                        case 0:
                            flag=False

    def delete(self,name):
        flag=False
        for i in self.contact:
            if i.first_name==name:
                self.contact.remove(i)
                flag=True
                break   
        if(flag==True):
            print("User deleted")
        else:
            print("user not found")

    def sort_alphabetically(self):
        self.contact.sort(key=lambda x: x.first_name)
    
    def sort_city_state_zip(self,k):
        match k:
            case 1:
                self.contact.sort(key=lambda x: x.city)
            case 2:
                self.contact.sort(key=lambda x: x.state)
            case 3:
                self.contact.sort(key=lambda x: x.zip)

        # Save contacts to file
    def save_to_file(self, filename):
        with open(f"Data//{filename}", "w") as file:
            for contact in self.contact:
                data = f"{contact.first_name}|{contact.last_name}|{contact.address}|{contact.city}|{contact.state}|{contact.zip}|{contact.phone_number}|{contact.email}\n"
                file.write(data)

        print("Contacts saved to file successfully!")


    # Load contacts from file
    def load_from_file(self, filename):
        try:
            with open(f"Data//{filename}", "r") as file:
                for line in file:
                    data = line.strip().split("|")

                    if len(data) == 8:
                        new_contact = contact(
                            data[0], data[1], data[2],
                            data[3], data[4], data[5],
                            data[6], data[7]
                        )
                        self.add_contact(new_contact)
                file.seek(0)
                print(file.read())

            print("Contacts loaded from file successfully!")

        except FileNotFoundError:
            print("File not found!")




