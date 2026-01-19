from contact_list import Contact_list
from contact import Contact

contact_list = Contact_list()

contact_list.add_new_contact(Contact("John Brown", "brown@onet.pl", "555234000"))
contact_list.add_new_contact(Contact("Anna May", "am@o2.pl", "232000199"))
contact_list.add_new_contact(Contact("George Small", "smallg@google.pl", "222999100"))
contact_list.add_new_contact(Contact("Paola Big", "bigpaola@poczta.pl", "100200300"))

print("Contact list on the smartphone:")
contact_list.display_contact_list()