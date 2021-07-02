from protobuf2 import addressbook_pb2

def ListPeople(address_book):
    for person in address_book.people:
        print("Person ID: ", person.id)
        print("Name: ", person.name)
        if person.HasField("email"):
            print("Email address: ", person.email)

        for phone_number in person.phones:
            if phone_number.type == addressbook_pb2.Person.PhoneType.MOBILE:
                print("  Mobile phone #:", end=" ")
            elif phone_number.type == addressbook_pb2.Person.PhoneType.HOME:
                print("  Home phone #:", end=" ")
            elif phone_number.type == addressbook_pb2.Person.PhoneType.WORK:
                print("  Work phone #:", end=" ")
            print(phone_number.number)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} "ADDRESS_BOOK_FILE"')
        sys.exit(-1)
    
    address_book = addressbook_pb2.AddressBook()

    with open(sys.argv[1], "rb") as f:
        address_book.ParseFromString(f.read())

    ListPeople(address_book)