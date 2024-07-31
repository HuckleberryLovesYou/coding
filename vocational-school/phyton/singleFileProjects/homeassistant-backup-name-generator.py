import datetime


def main():
    bugfix_version_number: str = input("Enter current bugfix-version-number: ")
    print(createstring(bugfix_version_number))

def createstring(bugfix_version_number):
    today: str = f"{datetime.date.today()}"
    string: str = today + "_Update-" + today[:4] + today[5:7] + bugfix_version_number
    return string
    
if __name__ == '__main__':
    main()