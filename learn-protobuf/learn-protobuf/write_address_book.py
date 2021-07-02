import addressbook_pb2

def PromptForAddress(person):
    person.id = int(input("Enter person ID number: "))
    person.name = input("Enter name: ")

    email = input("Enter email address (blank for none): ")
    if email:
        person.email = email
    
    while True:
        number = input("Enter a phone number (or leave blank to finish): ")
        if not number:
            break

        phone = person.phones.add()
        phone.number = number

        phone_type_input = input("Is this a mobile, home, or work phone? ")
        if phone_type_input == "mobile":
            phone.type = addressbook_pb2.Person.PhoneType.MOBILE
        elif phone_type_input == "home":
            phone.type = addressbook_pb2.Person.PhoneType.HOME
        elif phone_type_input == "work":
            phone.type = addressbook_pb2.Person.PhoneType.WORK
        else:
            print("Unknown phone type; leaving as default value.")
    print(person)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} "ADDRESS_BOOK_FILE"')
        sys.exit(-1)

    address_book = addressbook_pb2.AddressBook()

    try:
        with open(sys.argv[1], "rb") as f:
            address_book.ParseFromString(f.read())
    except IOError:
        print(f"{sys.argv[1]}: Could not open file. Creating a new one")

    PromptForAddress(address_book.people.add())

    with open(sys.argv[1], "wb") as f:
        f.write(address_book.SerializeToString())
