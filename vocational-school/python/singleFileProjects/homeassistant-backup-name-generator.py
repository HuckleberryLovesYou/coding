import datetime
import requests

def get_version(major_version: str) -> str:
    if major_version[-2] == "0":
        last_digit: str = major_version[-1]
        major_version = major_version[:-2] + last_digit
    url: str = "https://www.home-assistant.io/blog/categories/release-notes/"
    response: requests.Response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Error while fetching the url")
    response_text: str = str(response.text)
    index = response_text.index(major_version)

    return response_text[index:(index + (len(major_version) + 2))]


def generate_name():
    today: str = str(datetime.date.today())
    major_version: str = today[:7].replace("-", ".")
    latest_version = get_version(major_version)
    return today + "_Update-" + latest_version.replace(".", "")


def main():
    print(generate_name())


if __name__ == '__main__':
    main()