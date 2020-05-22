import requests
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError


'''
ConnectionError 502
HTTPError 

'''

def call_the_api(url):
    #url = 'http://httpbin.org/get'

    try:
        req = requests.get(url, timeout=5)

        if 'errors' in req.json():
            return {'request_error': 'api_error_response'}

        return req.json()[0]

    except ConnectionError:
        return {'request_error': 'ConnectionTimeout'}
    except Timeout:
        return {'request_error': 'Timeout'}
    except Exception as ex:
        return {'request_error': ex}


if __name__ == "__main__":
    call_the_api()
