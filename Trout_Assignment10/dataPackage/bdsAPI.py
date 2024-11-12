# Document here

import requests
import csv
import json

class apiCall:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url
