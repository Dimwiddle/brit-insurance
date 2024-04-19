import requests
from requests import Response
import json
from requests.exceptions import RequestException
from typing import Literal

class Client:

    def __init__(self) -> None:
        self.endpoint = "https://api.restful-api.dev/objects"
        self.default_headers = {"content-type": "application/json"}

    def _send_request(self, method: Literal['GET', 'PATCH', 'PUT', 'POST', 'DELETE'], url: str, data: dict, headers: dict = None) -> Response:
        try:
            return requests.request(method ,url, data=data, headers=headers or self.default_headers)
        except RequestException as e:
            raise RequestException(f"Issue found when sending request. \n Endpoint: {url} \n Data: {data} \n {e}")
    
    def patch_object(self, object_id: int, data: dict):
        """Send a PATCH request for a specfic object to update it's specific fields."""
        url = f"{self.endpoint}/{object_id}"
        return self._send_request('PATCH', url, json.dumps(data))
    
    def get_objects(self):
        """Send a GET request to retrieve existing objects from the server."""
        return self._send_request('GET', self.endpoint)
    
    def post_object(self, data: dict) -> Response:
        """Send a POST request to create a new object."""
        return self._send_request('POST', self.endpoint, json.dumps(data))
