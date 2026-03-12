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
