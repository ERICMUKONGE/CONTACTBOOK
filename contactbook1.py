names = []
phone_numbers = []
num = 3

for i in range(num):
    name = input("Please enter any name of your choice:\n").upper()
    phone_number = input("Please enter any phone number of your choice:\n")
    names.append(name)
    phone_numbers.append(phone_number)
print("\nName\t\t\tPhone Number\n")

for i in range(num):
    print("{}\t\t\t{}".format(names[i], phone_numbers[i]))

search_term = input("\n Please enter name to search for:\n").upper()
print("search Result")
if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    print("Name {}, Phone Number: {}".format(search_term, phone_number))
else:
    print("Contact not found")       