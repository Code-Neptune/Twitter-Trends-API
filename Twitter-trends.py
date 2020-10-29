import requests
import json

bearer_token = ''      # Put your bearer token between ''


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def get_trends(headers, locationid=1):      # 1 is woeid for worldwide
    response = requests.get(
        f"https://api.twitter.com/1.1/trends/place.json?id={locationid}", headers=headers
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(
                response.status_code, response.text)
        )

    print(json.dumps(response.json()))


def main():
    headers = create_headers(bearer_token)
    get_trends(headers)


if __name__ == "__main__":
    main()
