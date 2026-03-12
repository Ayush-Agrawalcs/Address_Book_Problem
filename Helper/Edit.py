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



