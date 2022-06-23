contact = {}

def display_contact():
    print("Name\t\tContact number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

while True:
    choice = int(input("1.Add new contact\n2.Search conatct\n3.Display contact\n4.Edit contact\n5.Delete contact\n6.Exit\nPlease select any option of your choice:\n  "))
    if choice == 1:
        name = input("Please enter any name of your choice:\n").upper()
        phone = input("Please enter any number of your choice:\n").upper()
        contact[name] = phone

    elif choice == 2:
        search_name = input("Please enter name to search for:\n").upper()
        if search_name in contact:
            print(search_name,"'s contact number is ",contact[search_name])
        else:
            print("Name is not found in the contact book")

    elif choice == 3:
        if not contact:
            print("Empty contact book")
        else:
            display_contact() 

    elif choice == 4:
        edit_contact =input("Please enter name to be edited:\n").upper()
        if edit_contact in contact:
            phone = input("Please enter mobile number:\n").upper() 
            contact[edit_contact] = phone
            print("contact updated")
            display_contact()
        else:
            print("Name is not found in the contact book")

    elif choice == 5:
        del_contact = input("Please the name to be deleted:\n").upper()
        if del_contact in contact:
            confirm = input("Do you want to delete this contact:[y/n]\n").upper()
            if  confirm == "y" or confirm == "Y":
                contact.pop(del_contact)
            display_contact()
        else:
            print("Name is not found in the contact book")
    else:
        break        
