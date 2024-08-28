import requests
import argparse
from tkinter.filedialog import askopenfilename
from time import sleep

MAKE_LOWER = False
filename = ""
only_mac = False
no_api = False

mac_address_array_all: list[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "A", "B", "C",
                         "D", "E", "F"]

def add(mac_address: str, user_specified_symbol: str) -> str:
    count: int = 0
    amount_of_times_true: int = 0
    for i in range(len(mac_address)):
        if count == 2:
            mac_address = mac_address[:i + amount_of_times_true] + user_specified_symbol + mac_address[i + amount_of_times_true:]
            count = 0
            amount_of_times_true += 1
        count += 1
    return mac_address


def replace(mac_address: str, user_specified_symbol: str) -> str:
    mac_address_output: str = ""
    for i in range(len(mac_address)):
        if not mac_address[i] in mac_address_array_all:
            mac_address_output = mac_address_output + user_specified_symbol
        else:
            if MAKE_LOWER:
                mac_address_lower = mac_address[i].lower()
                mac_address_output = mac_address_output + str(mac_address_lower)
            else:
                mac_address_upper = mac_address[i].upper()
                mac_address_output = mac_address_output + str(mac_address_upper)
    return mac_address_output


def mac_address_vendor(mac_address: str, debug_enabled: bool) -> tuple[str, int]:  # uses https://api.macvendors.com/ api to get the vendor of the mac
    """Get the vendor of the MAC address by using the macvendors.com API.
    It takes a MAC address as a string input and a boolean to determine, if debug is enabled.
    It returns a tuple containing the vendor name (of type str) and the status code (of type int) of the API call."""
    mac_address_vendor_api_url = "https://api.macvendors.com/" + mac_address
    mac_address_vendor_api_call = requests.get(mac_address_vendor_api_url)
    if debug_enabled:
        print("Entering debug mode.\nMore stats will be shown.")
        print(f"\n\n\n{mac_address_vendor_api_call.status_code=}")
        print(f"{mac_address_vendor_api_call.elapsed=}")
        print(f"{mac_address_vendor_api_call.raw=}")
        print(f"{mac_address_vendor_api_call.reason=}")
        print(f"{mac_address_vendor_api_call.__hash__()=}\n\n\n")
    return mac_address_vendor_api_call.text , mac_address_vendor_api_call.status_code


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
            mac_address = decide_convertion_algorithm(mac_address, user_specified_symbol)
            mac_addresses_in_csv_file.append(mac_address)
            if not no_api:
                vendor, _ = mac_address_vendor(mac_address, debug_enabled=False)
                vendors_in_csv_file.append(vendor)
                sleep(1.2) #max. 2 api-requests per second

        mac_addresses_done += 1
        print(f"{csv_file_length - mac_addresses_done} done. (00-00-00-00-00-00 will be skipped)", end="\r")

    generate_output_file(hostnames_in_csv_file, ip_in_csv_file, mac_addresses_in_csv_file, vendors_in_csv_file)


def decide_convertion_algorithm(mac_address: str, user_specified_symbol: str) -> str:
    if mac_address[2] in mac_address_array_all:  # checks if there is already spacing between every 16bit
        mac_address = add(mac_address, user_specified_symbol)
    else:
        mac_address = replace(mac_address, user_specified_symbol)
    return mac_address

def is_valid_mac_address(mac_address:  str) -> bool:
    """It checks if the given MAC Address is valid by checking if the length is between 12 and 17 and if the mac address
    isn't 000000000000 or 00-00-00-00-00-00.
    It also prints a message if the MAC Address is
    invalid including supported mac address formats. It returns True if the MAC Address is valid, otherwise False."""

    if 11 < len(mac_address) < 18 and mac_address != "000000000000" != "00-00-00-00-00-00":
        if mac_address != "000000000000" or mac_address != "00-00-00-00-00-00" or mac_address != "00:00:00:00:00:00":
            return True
    else:
        print("Please enter a Mac Address with a length between 12 and 17\nSupported formats are like the following:\n")
        print("D83ADDEE5522\nd83addee5522\nD8-3A-DD-EE-55-22\nD8:3A:DD:EE:55:22\nd8$3A$DD$eE$55!22")
        return False


def main() -> None:
    parser = argparse.ArgumentParser("This is a Converter which converts MAC Address Notation to a other one [e.g. 'E8-9C-25-DC-A5-EA' -> 'E8:9C:25:DC:A5:EA']\nIt will lookup the vendor of the MAC Address by default.\n\n\t©timmatheis-de")
    parser.add_argument("-m", "--mac-address", required=True, action="store", dest="mac_address", help="Provide MAC Address in supported format.", type=str)
    parser.add_argument("-r", "--replace", required=False, default="-", action="store", dest="replace_symbol", help="Enter symbol for replacing. [Default: '-']", type=str)
    parser.add_argument("-l", "--lower", required=False, default=False, action="store_true", dest="lower_boolean", help="Specify to change the MAC Address to only lowercase. [Default: False]")
    parser.add_argument("-d", "--debug", required=False, default=False, action="store_true", dest="lower_boolean", help="Specify to enable the debug mode. [Default: False]")
    parser.add_argument("-f", "--file", required=False, default=False, action="store_true", dest="file_boolean", help="Specify to specify a file afterwards. Support file formats are: .csv [Default: False]")
    parser.add_argument("-om", "--only-mac", required=False, default=False, action="store_true", dest="only_mac_boolean", help="Specify to change the output file to only include the Mac Addresses. [Default: False]")
    parser.add_argument("-na", "--no-api", required=False, default=False, action="store_true", dest="no_api_boolean", help="Specify to skip the api lookup. [Default: False]")
    args = parser.parse_args()

    mac_address: str = args.mac_address
    user_specified_symbol: str = args.replace_symbol
    if args.lower_boolean:
        global MAKE_LOWER
        MAKE_LOWER = True
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
        if is_valid_mac_address(mac_address):
            mac_address_output: str = decide_convertion_algorithm(mac_address, user_specified_symbol)  #calls replace() and add()
            print(mac_address_output)
            if not no_api:
                vendor, status_code = mac_address_vendor(mac_address, args.lower_boolean)
                print(vendor)

if __name__ == "__main__":
    main()