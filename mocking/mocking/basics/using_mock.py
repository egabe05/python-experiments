from unittest.mock import Mock

mock = Mock()
print(mock)

# create attributes/functions when you access them
print(mock.some_attribute)
print(mock.some_function())


# recursively defines other mocks
json = Mock()
print(json.loads('{"k": "v"}').get('k'))




