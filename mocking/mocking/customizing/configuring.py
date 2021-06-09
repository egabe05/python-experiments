from unittest.mock import Mock

# mocks can be configured at time of initialization
mock = Mock(side_effect=lambda: "something")
print(mock())

mock = Mock(name="My Mock")
print(mock)

mock = Mock(return_value=True)
print(mock())


# existing mocks can be configured with .configure_mock
mock = Mock()
print(mock)
mock.configure_mock(side_effect=lambda: "existing something")
print(mock())

# configure a mock by unpacking a dictionary with .configure_mock
dog = Mock()
dog.configure_mock(**{"bark.return_value": "woof", "fetch.side_effect": lambda: "fetching ...", "my_name": "Rover"})
print(dog.bark())
print(dog.fetch())
print(dog.my_name)
