import unittest
from my_calendar import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch


class TestCalendarDecorator(unittest.TestCase):
    @patch('my_calendar.requests')
    def test_get_holidays_timeout_on_second_attempt(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
            assert mock_requests.get.call_count == 3


if __name__ == '__main__':
    unittest.main()
