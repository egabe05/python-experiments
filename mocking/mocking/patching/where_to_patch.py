import my_calendar
from unittest.mock import patch

"""
always think local scope, here we imported my_calendar which is bound to our local
scope so it works as expected when called.
"""
with patch('my_calendar.is_weekday'):
    print(my_calendar.is_weekday())


# -------------------------------------------------

# comment out all of the above for the next example

# from my_calendar import is_weekday
# from unittest.mock import patch
#
# """
# in this case is_weekday is imported into our local scope directly, however we patch
# "my_calendar.is_weekday".  when is_weekday is then called we get the actual function
# and not the mock.
# """
# with patch("my_calendar.is_weekday"):
#     print(is_weekday())


# -------------------------------------------------

# comment out all of the above for the next example

# from my_calendar import is_weekday
# from unittest.mock import patch
#
# """
# in this case is_weekday is imported into our local scope directly, therefore to mock the
# function we want to mock the local function
# """
# with patch("__main__.is_weekday"):
#     print(is_weekday())
