contacts = {}

# 1. Add Contact
def add_contact():                              
    name = input("Enter your Name: ")
    number = input("Enter Contact Number: ")
    if name in contacts:
        print("Contact already exist")
    else:
        contacts[name] = number
        print("Contact has been added successfully")
    if not number.isdigit():
        print("Enter valid phone number")
        return
    
# 3. Search Contact number
def search_contact():
    search_name = input("Enter name that you wanna search: ")
    if search_name in contacts:
        print(f"{search_name} : {contacts[search_name]}")
    else:
        print("Not Found")

# 4. Print contact list
def print_list():
    if not contacts:
            print("No contacts saved.")
    else:
        for name,number in contacts.items():
            print(f"{name}:{number}")

 # 5. Delete contact
def delete_contact():
    delete_contact = input("Enter Contact name that you wanna Delete: ")
    if delete_contact in contacts:
        del contacts[delete_contact]
        print("Number has been deleted sucessfully!")
    else:
        print("Contact Not Found")
       


while True:
    print("\nContact Book")
    print("Choose an Option:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Print All Contact List")
    print("5. Delete Contact")
    print("6. Exit")
    
    try:
        choice = int(input("Enter your Choice: "))
    except ValueError:
        print("Enter valid Option")
        continue
    
    if choice == 1:       # 1. Add Contact
        add_contact()
        
    elif choice == 2:       # 2. View Contact
        if not contacts:
            print("No contacts saved")
        else:
            for name, number in contacts.items():
                print(f"{name}: {number}")         
    
    elif choice == 3:       # 3. Search Contact number
        search_contact()

    elif choice == 4:       # 4. Print contact list
        print_list()
    
    elif choice == 5:       # 5. Delete contact
        delete_contact()        

    elif choice == 6:      # 6. Exit
        print("Exit")
        break

    else:
        print("Invalid option")