contact_book = ()

def new_contact(name:str,number:int):
    # check name is exsists in ph_book or not
    # get file contacts
    try:
        with open('contacts.txt', 'r') as f:
            contact_lines = f.readlines()
    except:
        print("Error in add_contact")
    for contact in contact_lines:















        
    name = input("Enter name:")
    if name in contact:
        print("contact already exsists")
    else:
        mobile = input("Enter mobile number:")
        contact[name] = mobile
        print("contact added sussfully")

def update_contact():
    name = input("enter name to update:")
    if name in contact:
        mobile = input("Enter a new mobile number:")
        print("mobile number updated")
    else:
        print("contact not found")

def delete_contact():
    name = input("enter name to delete:")
    if name in contacts:
        delete = contact[name]
        print("contact delete")
    else:
        print("contact not found")

def get_contact():
    name = input("enter name to get contact:")
    if name in contacts:
        print(f"[name], mobile number")
    else:
        print("contact not found")

def print_all_contact():
    if not contacts:
        print("contact book is empty")
    else:
        print("enter all correct")

while True:
    print("contact book")
    print("1. new contact")
    print("2. update mobile number")
    print("3. delete contact")
    print("4. get contact number")
    print("5. print all contacts")
    choice = input("enter your choice:")
    if choice == 1:
        new_contact()
    elif choice == 2:
        update_mobile()
    elif choice == 3:
        delete_contact()
    elif choice == 4:
        get_contact()
    elif choice == 5:
        print_all_contact()
        print("exiting the contact book")
        break
    else:
        print("contact book not exiting")