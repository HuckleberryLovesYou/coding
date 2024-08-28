import requests
import argparse

MAKE_LOWER = False
filename = ""
only_mac = False
no_api = False

mac_address_array_all: list[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "A", "B", "C",
                         "D", "E", "F"]

def add(mac_address, user_specified_symbol):
    count: int = 0
    amount_of_times_true: int = 0
    for i in range(len(mac_address)):
        if count == 2:
            mac_address = mac_address[:i + amount_of_times_true] + user_specified_symbol + mac_address[i + amount_of_times_true:]
            count = 0
            amount_of_times_true += 1
        count += 1
    return mac_address


def replace(mac_address, user_specified_symbol):
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

def symbol_check_mac_address(mac_address, user_specified_symbol):
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


if __name__ == "__main__":
    main()