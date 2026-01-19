from contact import Contact

class Contact_list:
    def __init__(self):
        self.contact_list = []

    def add_new_contact(self,contact):
        self.contact_list.append(contact)
    
    def display_contact_list(self):
        for contact in self.contact_list:
            print(contact)