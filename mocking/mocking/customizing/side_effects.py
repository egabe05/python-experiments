import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock

requests = Mock()


def get_holidays():
    try:
        r = requests.get("http://localhost/api/holidays")
    except Timeout:
        print("Request timed out, retrying")
        r = requests.get("http://localhost/api/holidays")
    if r.status_code == 200:
        return r.json()
    return None


class TestCalendar(unittest.TestCase):
    def fake_request(self, url):
        print(f"Making a request to {url}")
        print("Request received")

        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            "12/25": "Christmas",
            "7/4": "Independence Day",
        }
        return response_mock

    def test_get_holidays(self):
        # accepts and calls a function provided it has the same arguments as the mock
        requests.get.side_effect = self.fake_request
        assert get_holidays()["12/25"] == "Christmas"

    def test_get_holidays_timeout_on_second_attempt(self):
        # accepts exceptions to simulate failure conditions
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()

    def test_retries_on_timeout(self):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {"12/25": "Christmas", "7/4": "Independence Day", }

        # accepts an iterable which must yield a value on every call
        requests.get.side_effect = [Timeout, response_mock]

        assert get_holidays()["7/4"] == "Independence Day"


if __name__ == '__main__':
    unittest.main()
