import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    # The GetRequester class should have a get_response_body method that sends a GET request to the URL passed in on initialization. This method should return the body of the response.
    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    # The GetRequester class should have a load_json method should use get_response_body to send a request, then return a Python list or dictionary made up of data converted from the response of that request.
    def load_json(self):
        return json.loads(self.get_response_body())


###############################################################################
    
get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
print(get_requester.load_json())