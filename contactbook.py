contact_book={}
while True:
    choice = input("Make a choice of what our menu have to offer\nX-Exit\nA-All numbers\nS-save\nP-select the number\n").upper()
    if choice == "S":
        name = input("Please enter your name:\n")
        number = input("Please enter your contact number:\n")
        contact_book[name]=number
    elif choice == "P":
        search_name = input("Please enter name you want to search for:\n") 
        print("So the number of",search_name,"is",contact_book[search_name])
    elif choice == "A":
        print(contact_book) 
    elif choice == "X":
        break       