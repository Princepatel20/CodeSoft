contacts = []

def show_menu():
    print("Contact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    matching_contacts = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    if not matching_contacts:
        print("No contacts found.")
    else:
        print("Matching Contacts:")
        for contact in matching_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def edit_contact():
    search_term = input("Enter name or phone number to search: ")
    matching_contacts = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    if not matching_contacts:
        print("No contacts found.")
    else:
        if len(matching_contacts) > 1:
            print("Multiple contacts found:")
            for i, contact in enumerate(matching_contacts, start=1):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            index = int(input("Enter the index of the contact to edit: "))
            if index < 1 or index > len(matching_contacts):
                print("Invalid index.")
                return
            contact = matching_contacts[index - 1]
        else:
            contact = matching_contacts[0]
        name = input(f"Enter new name (current: {contact['name']}): ") or contact['name']
        phone = input(f"Enter new phone number (current: {contact['phone']}): ") or contact['phone']
        email = input(f"Enter new email address (current: {contact['email']}): ") or contact['email']
        contact['name'] = name
        contact['phone'] = phone
        contact['email'] = email
        print("Contact updated successfully!")

def delete_contact():
    search_term = input("Enter name or phone number to search: ")
    matching_contacts = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    if not matching_contacts:
        print("No contacts found.")
    else:
        if len(matching_contacts) > 1:
            print("Multiple contacts found:")
            for i, contact in enumerate(matching_contacts, start=1):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            index = int(input("Enter the index of the contact to delete: "))
            if index < 1 or index > len(matching_contacts):
                print("Invalid index.")
                return
            contact = matching_contacts.pop(index - 1)
        else:
            contact = matching_contacts.pop()
        contacts.remove(contact)
        print("Contact deleted successfully!")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            edit_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()