from better.types.tutorial import Person, PersonPhoneNumber, PersonPhoneType

eric = Person()
eric.id = 1
eric.name = "Eric Gaberik"
eric.email = "egaberik@gmail.com"
eric_phone = PersonPhoneNumber()
eric_phone.number = "555-5555"
eric_phone.type = PersonPhoneType.MOBILE
eric.phones.append(eric_phone)

print(eric)
