import json
from App.Models.Contact import contact


class File_handler:
        # Save contacts to file
    def save_to_file(self, books,filename):
        '''
        save a contact to csv or a text file
        '''
        c=input("enter 1 to add text and 2 to add csv: ")
        if(c=='1'):
            s='|'
            ex=".txt"
        if(c=='2'):
            s=","
            ex=".csv"
        with open(f"Data//{filename}{ex}", "w") as file:
            for name,book in books.address_book.items():
                for contact in book.contact:
                    data = f"{name}{s}{contact.first_name}{s}{contact.last_name}{s}{contact.address}{s}{contact.city}{s}{contact.state}{s}{contact.zip}{s}{contact.phone_number}{s}{contact.email}\n"
                    file.write(data)

        print("Contacts saved to file successfully!")


    # Load contacts from file
    def load_from_file(self, books,filename):
        '''
        Load the contact from csv or text to the contact
        '''
        print(filename)
        c=input("enter 1 to add text and 2 to add csv: ")
        if(c=='1'):
            s='|'
            ex=".txt"
        if(c=='2'):
            s=","
            ex=".csv"
        try:
            with open(f"Data//{filename}{ex}", "r") as file:
                for line in file:
                    data = line.strip().split(s)

                    if len(data) == 9:
                        books.add_addressbook(data[0])
                        book=books.address_book[data[0]]
                        new_contact = contact(
                             data[1], data[2],
                            data[3], data[4], data[5],
                            data[6], data[7],data[8]
                        )
                        book.add_contact(new_contact)
                file.seek(0)
                print(file.read())

            print("Contacts loaded from file successfully!")

        except FileNotFoundError:
            print("File not found!")
    
    
    def save_to_json(self,books,filename):
        '''
        save a contact to the json file
        '''
        address_books_dict = {}
        for ab_name, book in books.address_book.items():
            address_books_dict[ab_name] = []
            for contact in book.contact:
                data = {
                    "first_name": contact.first_name,
                    "last_name": contact.last_name,
                    "address": contact.address,
                    "city": contact.city,
                    "state": contact.state,
                    "zip": contact.zip,
                    "phone_number": contact.phone_number,
                    "email": contact.email
                }
                address_books_dict[ab_name].append(data)
        with open(f"Data/{filename}", "w") as file:
            json.dump(address_books_dict,file,indent=4)
        

        print("Contacts saved to file successfully!")
    
 

    def load_to_json(self, books, filename):
        '''
         Load the contact from json to the contact'''
        try:
            with open(f"Data//{filename}", "r") as file:
                datas = json.load(file)

            for ab_name, b in datas.items():
                books.add_addressbook(ab_name)
                book = books.address_book[ab_name]

                for data in b:
                    new_contact = contact(
                        data["first_name"],
                        data["last_name"],
                        data["address"],
                        data["city"],
                        data["state"],
                        data["zip"],
                        data["phone_number"],
                        data["email"]
                    )

                    book.add_contact(new_contact)

            print("Contacts loaded from JSON successfully!")

        except FileNotFoundError:
            print("File not found!")




