import requests
import pytest
import json
from jsonschema import validate, ValidationError

with open('cases.json', 'r') as file:
    cases_data = json.load(file)

req_method = None
req_url = None
json_data = None
schema = None
params = None

class MyTestCase:

    def __init__(self, url):
        self.url = url

    def test_get_cats(self):

        for test_case in cases_data:
            if test_case['test_case'] == 'get_cats':
                req_url = test_case['req_url']
                json_data = test_case.get('json')
                schema = test_case['schema']
                params = test_case['params']
                items = test_case['test_items']

        for item in items:
            target = item['target']
            params.update(target)

            response = requests.get(self.url + req_url, params=params)

            try:
                assert response.status_code == item['code_status'], print(f"Scanario: {item['scenario']} expacted status code is {item['code_status']}, but response code is {response.status_code}")
            except AssertionError as e:
                continue

            if response.status_code == 200:
                data = response.json()
                try:
                    validate(instance=data, schema=schema)
                except ValidationError as e:
                    print(f"JSON Schema Validation Error for scenario {item['scenario']}: {e.message}")
                    continue

                try:
                    assert item['keyword'] in response.text, (
                        f"Keyword '{item['keyword']}' not found in response for scenario {item['scenario']}"
                    )
                except AssertionError as e:
                    print(f"Keyword Assertion Error: {e}")
                    continue

    def test_get_count(self):

        for test_case in cases_data:
            if test_case['test_case'] == 'get_count':
                req_url = test_case['req_url']
                json_data = test_case.get('json')
                schema = test_case['schema']
                params = test_case['params']
                items = test_case['test_items']

        for item in items:
            target = item['target']
            params.update(target)

            response = requests.get(self.url + req_url, params=params)

            try:
                assert response.status_code == item['code_status'], print(f"Scanario: {item['scenario']} expacted status code is {item['code_status']}, but response code is {response.status_code}")
            except AssertionError as e:
                continue

            if response.status_code == 200:
                data = response.json()
                try:
                    validate(instance=data, schema=schema)
                except ValidationError as e:
                    print(f"JSON Schema Validation Error for scenario {item['scenario']}: {e.message}")
                    continue

                try:
                    assert item['keyword'] in response.text, (
                        f"Keyword '{item['keyword']}' not found in response for scenario {item['scenario']}"
                    )
                except AssertionError as e:
                    print(f"Keyword Assertion Error: {e}")
                    continue






