import requests
import argparse
from tkinter.filedialog import askopenfilename
from time import sleep

make_lower = False
filename = ""
only_mac = False
no_api = False

mac_address_letters: list[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "A", "B", "C",
                         "D", "E", "F"]


class MacAddressInvalid(Exception):
    def __init__(self, message: str):
        print(message)

def generate_output_file(hostnames: list[str], ips: list[str], mac_addresses: list[str], vendors: list[str]) -> None:
    print("Generating output file...")
    with open("output_mac_address_converter.txt", "a") as output_file:
        if only_mac:
            for i in range(len(mac_addresses)):
                output_file.write(str(mac_addresses[i]) + "\n")
        else:
            if no_api:
                for i in range(len(mac_addresses)):
                    output_file.write(f"Hostname: {hostnames[i]}, IP: {ips[i]}, MAC: {mac_addresses[i]}\n")
            else:
                for i in range(len(mac_addresses)):
                    output_file.write(f"Hostname: {hostnames[i]}, IP: {ips[i]}, MAC: {mac_addresses[i]}, Vendor: {vendors[i]}\n")


def handle_csv_file(user_specified_symbol: str) -> None:
    with open(filename, "r") as csv_file:
        lines = csv_file.readlines()

    hostnames_in_csv_file = []
    ip_in_csv_file = []
    mac_addresses_in_csv_file = []
    vendors_in_csv_file = []
    csv_file_length = len(lines)
    mac_addresses_done: int = 0
    for line in lines:
        columns = line.split(",")
        hostnames_in_csv_file.append(columns[1])
        ip_in_csv_file.append(columns[2])
        mac_address = columns[3]
        if is_valid_mac_address(mac_address):
            mac_address = convert_mac_address(mac_address, user_specified_symbol)
            mac_addresses_in_csv_file.append(mac_address)
            if not no_api:
                vendor, _ = mac_address_vendor(mac_address)
                vendors_in_csv_file.append(vendor)
                sleep(1.2) #max. 2 api-requests per second

        mac_addresses_done += 1
        print(f"{csv_file_length - mac_addresses_done} done. (00-00-00-00-00-00 will be skipped)", end="\r")

    generate_output_file(hostnames_in_csv_file, ip_in_csv_file, mac_addresses_in_csv_file, vendors_in_csv_file)


def mac_address_vendor(mac_address) -> str | None:  # uses https://api.macvendors.com/ api to get the vendor of the mac
    """Get the vendor of the MAC address by using the macvendors.com API.
    It takes a MAC address as a string input and a boolean to determine, if debug is enabled.
    It returns a tuple containing the vendor name (of type str) and the status code (of type int) of the API call."""
    if not no_api:
        mac_address_vendor_api_url = "https://api.macvendors.com/" + mac_address
        mac_address_vendor_api_call = requests.get(mac_address_vendor_api_url)
        mac_address_vendor_api_call_text = mac_address_vendor_api_call.text
        if mac_address_vendor_api_call_text == '{"errors":{"detail":"Not Found"}}' or mac_address_vendor_api_call.status_code != 200:
            print("API Lookup failed")
            return "API Lookup failed. Not found."
        return mac_address_vendor_api_call.text
    else:
        print("No API lookup, since --no-api switch.")


def is_valid_mac_address(mac_address: str) -> bool:
    """It checks if the given MAC Address is valid by checking if the raw length is 12 and if the mac address
    isn't 000000000000 or 00-00-00-00-00-00 or 00:00:00:00:00:00.
    It also prints a message if the MAC Address is
    invalid including supported mac address formats. It returns True if the MAC Address is valid, otherwise False."""
    count: int = 0
    for letter in mac_address:
        if letter in mac_address_letters:
            count += 1

    if count == 12:
        if not mac_address in ["000000000000", "00-00-00-00-00-00", "00:00:00:00:00:00"]:
            return True

    print("Please enter a valid Mac Address \nSupported formats are like the following:\n")
    print("D83ADDEE5522\nd83addee5522\nD8-3A-DD-EE-55-22\nD8:3A:DD:EE:55:22\nd8$3A$DD$eE$55!22")
    if len(filename) == 0:
        raise MacAddressInvalid("Invalid MAC Address submitted.")
    else:
        return False

def get_raw_mac_address(mac_address: str) -> str:
    raw_mac_address: str = ""
    for index, letter in enumerate(mac_address):
        if letter in mac_address_letters:
            raw_mac_address += mac_address[index]

    return raw_mac_address


def convert_mac_address(mac_address: str, user_specified_symbol: str) -> tuple[str, str] | None:
    raw_mac_address: str = get_raw_mac_address(mac_address)
    if is_valid_mac_address(raw_mac_address):
        count: int = 0
        amount_of_times_true: int = 0
        for i in range(len(raw_mac_address)):
            if count == 2:
                raw_mac_address = raw_mac_address[:i + amount_of_times_true] + user_specified_symbol + raw_mac_address[i + amount_of_times_true:]
                count = 0
                amount_of_times_true += 1

            count += 1

        if make_lower:
            raw_mac_address = raw_mac_address.lower()

        return raw_mac_address,  mac_address_vendor(raw_mac_address)


def main() -> None:
    parser = argparse.ArgumentParser("This is a Converter which converts MAC Address Notation to a other one [e.g. 'E8-9C-25-DC-A5-EA' -> 'E8:9C:25:DC:A5:EA']\nIt will lookup the vendor of the MAC Address by default.\n\n\t©timmatheis-de")
    parser.add_argument("-m", "--mac-address", required=True, action="store", dest="mac_address", help="Provide MAC Address in supported format.", type=str)
    parser.add_argument("-r", "--replace", required=False, default="-", action="store", dest="replace_symbol", help="Enter symbol for replacing. [Default: '-']", type=str)
    parser.add_argument("-l", "--lower", required=False, default=False, action="store_true", dest="lower_boolean", help="Specify to change the MAC Address to only lowercase. [Default: False]")
    parser.add_argument("-f", "--file", required=False, default=False, action="store_true", dest="file_boolean", help="Specify to specify a file afterwards. Support file formats are: .csv [Default: False]")
    parser.add_argument("-om", "--only-mac", required=False, default=False, action="store_true", dest="only_mac_boolean", help="Specify to change the output file to only include the Mac Addresses. [Default: False]")
    parser.add_argument("-na", "--no-api", required=False, default=False, action="store_true", dest="no_api_boolean", help="Specify to skip the api lookup. [Default: False]")
    args = parser.parse_args()

    mac_address: str = args.mac_address
    user_specified_symbol: str = args.replace_symbol
    if args.lower_boolean:
        global make_lower
        make_lower = True
    if args.only_mac_boolean:
        global only_mac
        only_mac = True
    if args.no_api_boolean:
        global no_api
        no_api = True


    if args.file_boolean:
        global filename
        filename = askopenfilename(title="Select csv-file to iterate through:", filetypes=[("CSV-Files" , "*.csv"), ("XML-Files", "*.xml"), ("JSON-Files", "*.json")])
        filetype = filename.split(".")
        filetype = f".{filetype[-1]}"
        match filetype:
            case ".csv":
                handle_csv_file(user_specified_symbol)
            case ".xml":
                print("This filetype is still wip")
            case ".json":
                print("This filetype is still wip")
    else:
        mac_address, vendor = convert_mac_address(mac_address, user_specified_symbol)
        if no_api:
            print(f"MAC Address: {mac_address}")
        else:
            print(f"MAC Address: {mac_address}\nVendor: {vendor}")

if __name__ == "__main__":
    main()