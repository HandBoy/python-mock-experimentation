import requests
from requests import Timeout, ConnectionError

def call_the_api(url):
    try:
        req = requests.get(url, timeout=5)

        if not req.ok:
            response = req.json()
            if "detail" in response:
                return {"error": response["detail"]}
                
            return {"request_error": "api_error_response"}

        return req.json()[0]

    except ConnectionError:
        return {"request_error": "ConnectionTimeout"}
    except Timeout:
        return {"request_error": "Timeout"}
    except Exception as ex:
        return {"request_error": ex}


if __name__ == "__main__":
    call_the_api("http://jsonplaceholder.typicode.com/todos")
