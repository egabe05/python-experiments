from unittest.mock import create_autospec, Mock

# you can provide a specification to a mock which defines the interface
calendar = Mock(spec=["is_weekday", "get_holidays"])

# within the specification and will return another mock object
print(calendar.is_weekday())

# not defined within the specification so will raise an attribute error
try:
    calendar.create_event()
except AttributeError as e:
    print(type(e), str(e))


# you can set the specification with an object directly
import my_calendar

calendar_direct = Mock(spec=my_calendar)

print(calendar_direct.is_weekday())

try:
    calendar_direct.create_event()
except AttributeError as e:
    print(type(e), str(e))


# you can automatically implement a spec with create_autospec
calendar_auto = create_autospec(my_calendar)

print(calendar_auto.is_weekday())

try:
    calendar_auto.create_event()
except AttributeError as e:
    print(type(e), str(e))
