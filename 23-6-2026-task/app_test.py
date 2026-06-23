# mocking an external api call and testing the dependant function

from unittest.mock import patch
from app import get_user

@patch("app.requests.get")
def test_get_user(mock_get):
    mock_get.return_value.json.return_value = {
        "id":1,
        "name":"Harsadha"
    }
    result = get_user()
    assert result["name"] == "Harsadha"