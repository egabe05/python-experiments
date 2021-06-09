from datetime import datetime
from unittest.mock import Mock

# test days
tuesday = datetime(year=2019, month=1, day=1)
saturday = datetime(year=2019, month=1, day=5)

datetime = Mock()


def is_weekday() -> bool:
    today = datetime.today()
    return 0 <= today.weekday() < 5


# .today should return Tuesday
datetime.today.return_value = tuesday
assert is_weekday()

# .today should return Saturday
datetime.today.return_value = saturday
assert not is_weekday()
