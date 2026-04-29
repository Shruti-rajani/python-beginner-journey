
contacts = {}

while True:
    print("Contact Book")
    print("Choose an Option:")
    print("1. Add Contact  ")
    print("2. View Contact")
    print("3. Search Contact ")
    print("4. Print All Contact List")
    print("5. Delete Contact")
    print("6. Exit")
    try:
        choice = int(input("Enter your Choice: "))
    except ValueError:
        print("Enter valid Option")
        continue

    if choice == 1:       #1. Add Contact
        name= input("Enter Contact Name: ")
        number = input("Enter Contact Number: ")
        if name in contacts:
            print("Contact already exist")
        else:
            contacts[name] = number                 #variable[key] = value
        
    elif choice == 2:       #2. View Contact
        if not contacts:
            print("No contacts saved")
        else:
            for name, number in contacts.items():
                print(f"{name}: {number}")         
    
    elif choice == 3:       #3.Search Contact number
        search_contact = input("Enter Contact Name to Search: : ")
        if search_contact in contacts:
            print(contacts[search_contact])
        else:
            print("Not Found")

    elif choice == 4:       #4.print contact list
        if not contacts:
            print("No contacts saved.")
        else:
            print(contacts)
    
    elif choice == 5:       #delete contact
        delete_name = input("Enter contact to delete: ")

        if delete_name in contacts:
            del contacts[delete_name]
            print("Deleted successfully")
        else:
            print("Contact not found")


    elif choice == 6:      #exit
        print("Exit")
        break

    else:
        print("Invalid option")
            
           
