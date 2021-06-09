import requests
from datetime import datetime
from requests.exceptions import Timeout

# see test examples in mocking/tests


def is_weekday() -> bool:
    today = datetime.today()
    return 0 <= today.weekday() < 5


def get_holidays():
    try:
        r = requests.get("http://localhost/api/holidays")
    except Timeout:
        print("Request timed out, retrying")
        r = requests.get("http://localhost/api/holidays")
    if r.status_code == 200:
        return r.json()
    return None
