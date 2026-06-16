# MINI PROJECT- WEEK 1- DAY 5
'''
✓ Contact class (name, phone, email) with __str__
✓ ContactBook class: add, search, delete, list all contacts
✓ Use defaultdict to group contacts by first letter (A-Z)
✓ Menu-driven console interface (loop until exit)
✓ Use filter + lambda for search functionality
✓ Handle all edge cases (duplicate, not found, empty book)'''

import re
from collections import defaultdict

class Contact:
    serial_no = 1000
    def __init__(self,name,phone,email):
        self.id = Contact.serial_no
        Contact.serial_no+=1
        self.name = name
        self.phone = phone
        self.email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,input_name):
        name_pattern = r"^[A-Za-z]+(\s[A-Za-z]+)*$"
        if not re.fullmatch(name_pattern,input_name):
            raise ValueError("Input a valid name.")
        else:
            self._name = input_name

    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self,input_phone):
        phone_pattern = r"^\d{10}$"
        if not re.fullmatch(phone_pattern,input_phone):
            raise ValueError("Input a valid 10 digit phone number.")
        else:
            self._phone = input_phone

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,input_email):
        email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        if not re.fullmatch(email_pattern,input_email):
            raise ValueError("Input a proper email.")
        else:
            self._email = input_email

    def __str__(self):
        return f"Contact ID:{self.id}\t\tName:{self.name}\t\tPhone:{self.phone}\tEmail:{self.email}"
    
class ContactBook():
    def __init__(self):
        self.contacts=[]

    def add_contact(self,name,phone,email):
        for contact in self.contacts:
            if contact.phone==phone:
                raise ValueError("Contact already exists. Cannot create duplicate contacts.")
        contact=Contact(name,phone,email)
        self.contacts.append(contact)

    def view_all_contact(self):
        if not self.contacts:
            raise ValueError("No contacts found.")
        for contact in self.contacts:
            print(contact)
    
    def delete_contact(self,phone):
        for contact in self.contacts:
            if contact.phone==phone:
                self.contacts.remove(contact)
                return "Contact deleted successfully!"
        raise ValueError("Contact not found for deleting.")
    
    def search_contact(self, keyword):
        result = list(filter(lambda c: (keyword.lower() in c.name.lower()) 
                             or (keyword.lower() in c.email.lower()) 
                             or (keyword.lower() in c.phone),self.contacts))

        if not result:
            raise ValueError("Contact not found.")

        for contact in result:
            print(contact)

    def group_contacts(self):
        groups = defaultdict(list)
        for contact in self.contacts:
            groups[contact.name[0].upper()].append(contact)
        return groups
    
print("WELCOME TO THE CONTACT PORTAL :)")
print("MENU:")
print("1.Add Contact")
print("2.View Contacts")
print("3.Delete Contact")
print("4.Group Contacts alphabetically")
print("5.Search for a contact")
print("0.Exit")

book = ContactBook()

while(1):
    print()
    choice = int(input("Enter your choice:"))
    match choice:
        case 0:
            print("Exiting..")
            break

        case 1:
            # try:
            #     print("Adding a contact..")
            #     name = input("Enter the name of the contact:")
            #     phone = input("Enter the phone number:")
            #     email=input("Enter the email address:")
            #     book.add_contact(name,phone,email)
            #     print(name,"'s Contact has been added successfully!")
            # except Exception as e:
            #     print("Error:",e)
            book.add_contact("Harsadha","9840572839","harshu@gmail.com")
            book.add_contact("Sruthi R","9344726389","sruthi@yahoo.com")
            book.add_contact("Visalakshi","7356723491","visa@gmail.com")
            book.add_contact("Ranjeeth","9923567189","ranjeenm@gmail.com")
            book.add_contact("Shamitha","9840702348","shami23@hotmail.com")

        case 2:
            try:
                print("Viewing all contacts..")
                book.view_all_contact()
            except Exception as e:
                print("Error:",e)

        case 3:
            try:
                print("Deleting contacts..")
                phone = input("Enter the contact number to be deleted:")
                print(book.delete_contact(phone))
            except Exception as e:
                print("Error:",e)

        case 4:
            try:
                print("Displaying contact list alphabetically..")
                groups = book.group_contacts()
                if not groups:
                    print("No contacts found.")
                for letter in sorted(groups):
                    print(letter,":")
                    for contact in groups[letter]:
                        print(contact)
            except Exception as e:
                print("Error:",e)

        case 5:
            try:
                print("Searching for a contact..")
                keyword = input("Enter keyword to be searched in the contact book:")
                book.search_contact(keyword)
            except Exception as e:
                print("Error:",e)

        case _:
            print("Enter a valid choice from 0-4.")
            continue