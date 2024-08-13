import datetime
import argparse

def main():
    parser = argparse.ArgumentParser(description="This is a Generator for a reasonable Backup-Name for Homeassistant")
    parser.add_argument("-v", "--version", required=True, action="store", dest="version", help="Enter current bugfix-version-number [e.g. 2024.8.2 -> 2]")
    args = parser.parse_args()

    print(generate_name(args.version))

def generate_name(version=None):
    today: str = f"{datetime.date.today()}"
    string: str = today + "_Update-" + today[:4] + today[6:7] + version
    return string
    
if __name__ == '__main__':
    main()