from better.tutorial import AddressBook, Person, PersonPhoneNumber, PersonPhoneType

def PromptForAddress(address_book: AddressBook):
    person = Person()
    person.id = int(input("Enter person ID number: "))
    person.name = input("Enter name: ")

    email = input("Enter email address (blank for none): ")
    if email:
        person.email = email
    
    while True:
        number = input("Enter a phone number (or leave blank to finish): ")
        if not number:
            break

        phone = PersonPhoneNumber()
        phone.number = number

        phone_type_input = input("Is this a mobile, home, or work phone? ")
        if phone_type_input == "mobile":
            phone.type = PersonPhoneType.MOBILE
        elif phone_type_input == "home":
            phone.type = PersonPhoneType.HOME
        elif phone_type_input == "work":
            phone.type = PersonPhoneType.WORK
        else:
            print("Unknown phone type; leaving as default value.")
        person.phones.append(phone)

    address_book.people.append(person)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} "ADDRESS_BOOK_FILE"')
        sys.exit(-1)

    address_book = AddressBook()

    try:
        with open(sys.argv[1], "rb") as f:
            address_book.parse(f.read())
    except IOError:
        print(f"{sys.argv[1]}: Could not open file. Creating a new one")

    PromptForAddress(address_book)

    with open(sys.argv[1], "wb") as f:
        f.write(bytes(address_book))
