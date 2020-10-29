import requests
import json
import sys
import os

bearer_token = ''      # Put your bearer token between ''

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def get_locationID(headers):
    response = requests.get(
        "https://api.twitter.com/1.1/trends/available.json", headers=headers
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )

    return json.dumps(response.json())


def main():
    headers = create_headers(bearer_token)
    location_ids = get_locationID(headers)
    cwd = os.getcwd()
    print(f'Check Location_ID.json in current working directory {cwd}')
    sys.stdout = open('location_ID.json', 'w')
    print(location_ids)
    sys.stdout = sys.__stdout__
    input("Press any key to exit...")

if __name__ == "__main__":
    main()
