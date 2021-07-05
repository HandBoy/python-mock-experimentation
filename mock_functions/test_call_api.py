import unittest
from unittest.mock import Mock, patch

from requests.exceptions import Timeout, ConnectionError

from mock_functions.call_api import call_the_api


def api_response(endpoint, *args, **kwargs):
    # Create a new Mock to imitate a Response
    response_mock = Mock(ok=True, status_code=200)

    data = []

    if "user" in endpoint:
        data = [
            {"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False},
            {"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False}
        ]
    elif "profile" in endpoint:
        data = [
            {"profileId": 1, "id": 1, "title": "delectus aut autem", "completed": False},
            {"profileId": 1, "id": 1, "title": "delectus aut autem", "completed": False}
        ]

    response_mock.json.return_value = data

    return response_mock


def api_response_not_found(endpoint, *args, **kwargs):
    # Create a new Mock to imitate a Response
    response_mock = Mock(ok=False, status_code=404)

    data = {"detail": "Resource Not Found", "code": 404}

    response_mock.json.return_value = data

    return response_mock


def response_api():
    return [
        {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False},
        {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
    ]


class TestCallApi(unittest.TestCase):
    BASE_URL = "http://jsonplaceholder.typicode.com/todos"
    NOT_FOUND = "http://httpbin.org/status/404"
    TMOUT = "http://temuser.develop.tembici.com.br/api/v1/users/addresses?user_id=1"

    def test_request_response(self):
        response = call_the_api(self.BASE_URL)
        self.assertTrue(response)
        self.assertEqual(1, response["userId"])

    def test_request_not_found(self):
        response = call_the_api(self.NOT_FOUND)
        print(response)
        self.assertTrue(response)
        self.assertIn("request_error", response)

    def test_request_timout(self):
        response = call_the_api(self.TMOUT)
        print(response)
        self.assertTrue(response)
        self.assertIn("request_error", response)
        self.assertIn("Timeout", response["request_error"])

    @patch("mock_functions.call_api.requests.get")
    def test_request_mock_response(self, mock_get):

        mock_get.json.return_value = response_api()

        response = call_the_api(self.BASE_URL)
        self.assertTrue(response)

    @patch("mock_functions.call_api.requests.get")
    def test_request_user_url_mock_response(self, mock_get):
        mock_get.side_effect = api_response

        response = call_the_api(f"{self.BASE_URL}/user")

        self.assertTrue(response)
        self.assertEqual(1, response["userId"])

    @patch("mock_functions.call_api.requests.get")
    def test_request_profile_url_mock_response(self, mock_get):
        mock_get.side_effect = api_response

        response = call_the_api(f"{self.BASE_URL}/profile")

        self.assertTrue(response)
        self.assertEqual(1, response["profileId"])

    @patch("mock_functions.call_api.requests.get")
    def test_request_mock_timeout_response(self, mock_get):
        mock_get.side_effect = Timeout

        response = call_the_api(f"{self.BASE_URL}/profile")

        self.assertTrue(response)
        self.assertIn("request_error", response)
        self.assertIn("Timeout", response["request_error"])

    @patch("mock_functions.call_api.requests.get")
    def test_request_mock_connection_error(self, mock_get):
        mock_get.side_effect = ConnectionError

        response = call_the_api(f"{self.BASE_URL}/user/1")

        self.assertTrue(response)
        self.assertIn("request_error", response)
        self.assertIn("ConnectionTimeout", response["request_error"])

    @patch("mock_functions.call_api.requests.get")
    def test_request_mock_without_user(self, mock_get):
        mock_get.side_effect = api_response_not_found

        response = call_the_api(f"{self.BASE_URL}/user/1")

        self.assertTrue(response)
        self.assertIn("detail", response)
        self.assertIn("Resource Not Found", response["detail"])

    @patch("mock_functions.call_api.requests.get")
    def test_request_mock_without_profile(self, mock_get):
        mock_get.side_effect = api_response_not_found

        response = call_the_api(f"{self.BASE_URL}/profile/1")

        self.assertTrue(response)
        self.assertIn("detail", response)
        self.assertIn("Resource Not Found", response["detail"])


if __name__ == "__main__":
    unittest.main()
