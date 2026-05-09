# Contact Book using File Handling

FILE_NAME = "contacts.txt"

def load_contacts():
    contacts = {}
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, mobile = line.strip().split(",")
                contacts[name] = mobile
    except FileNotFoundError:
        pass
    return contacts

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for name, mobile in contacts.items():
        
            file.write(f"{name},{mobile}\n")

def new_contact():
    contacts = load_contacts()
    name = input("Enter name: ")
    if name in contacts:
        print("Contact already exists")
    else:
        mobile = input("Enter mobile number: ")
        contacts[name] = mobile
        save_contacts(contacts)
        print("Contact added successfully")

def update_contact():
    contacts = load_contacts()
    name = input("Enter name to update: ")
    if name in contacts:
        mobile = input("Enter new mobile number: ")
        contacts[name] = mobile
        save_contacts(contacts)
        print("Mobile number updated")
    else:
        print("Contact not found")

def delete_contact():
    contacts = load_contacts()
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted")
    else:
        print("Contact not found")

def get_contact():
    contacts = load_contacts()
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else:
        print("Contact not found")

def print_all_contacts():
    contacts = load_contacts()
    if not contacts:
        print("Contact book is empty")
    else:
        print("All Contacts:")
        for name, mobile in contacts.items():
            print(name, ":", mobile)

# Menu
while True:
    print("\nCONTACT BOOK")
    print("1. New Contact")
    print("2. Update Mobile Number")
    print("3. Delete Contact")
    print("4. Get Contact Number")
    print("5. Print All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_contact()
    elif choice == "2":
        update_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        get_contact()
    elif choice == "5":
        print_all_contacts()
    elif choice == "6":
        print("Exiting Contact Book")
        break
    else:
        print("Invalid choice")