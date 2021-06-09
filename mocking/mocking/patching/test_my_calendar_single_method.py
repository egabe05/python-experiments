import unittest
from my_calendar import requests, get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch


class TestCalendarContextManager(unittest.TestCase):
    # this can also be used as a context manager
    @patch.object(requests, "get", side_effect=Timeout)
    def test_get_holidays_timeout_on_second_attempt(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
            assert mock_requests.get.call_count == 3


if __name__ == '__main__':
    unittest.main()
