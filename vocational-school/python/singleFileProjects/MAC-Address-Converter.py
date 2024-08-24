import requests
import argparse

MAKE_LOWER = False

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

def check_mac_address(mac_address):
    if 11 < len(mac_address) < 18:
        return True
    else:
        print("Please enter a Mac Address with a length between 12 and 17\nSupported formats are like the following:\n")
        print("D83ADDEE5522\nd83addee5522\nD8-3A-DD-EE-55-22\nD8:3A:DD:EE:55:22\nd8$3A$DD$eE$55!22")
        return False


def mac_address_vendor(mac_address_vendor_api_mac_address, debug_enabled):  # uses the mac_vendor_api to get the vendor of the mac
    mac_address_vendor_api_url = "https://api.macvendors.com/" + str(mac_address_vendor_api_mac_address)
    mac_address_vendor_api_call = requests.get(mac_address_vendor_api_url)
    if debug_enabled:
        print("Entering debug mode.\nMore stats will be shown.")
        print(f"\n\n\n{mac_address_vendor_api_call.status_code=}")
        print(f"{mac_address_vendor_api_call.elapsed=}")
        print(f"{mac_address_vendor_api_call.raw=}")
        print(f"{mac_address_vendor_api_call.reason=}")
        print(f"{mac_address_vendor_api_call.__hash__()=}\n\n\n")
    return mac_address_vendor_api_call.text , mac_address_vendor_api_call.status_code

def main():
    parser = argparse.ArgumentParser("This is a Converter which converts MAC Address Notation to a other one [e.g. 'E8-9C-25-DC-A5-EA' -> 'E8:9C:25:DC:A5:EA']\nIt will also lookup the vendor of the MAC Address\n\n\t©timmatheis-de")
    parser.add_argument("-m", "--Mac-Address", required=True, action="store", dest="mac_address", help="Provide MAC Address in supported format", type=str)
    parser.add_argument("-r", "--replace", required=False, default="-", action="store", dest="replace_symbol", help="Enter symbol for replacing [Default: '-']", type=str)
    parser.add_argument("-l", "--lower", required=False, default=False, action="store_true", dest="lower_boolean", help="Specify to change the MAC Address to only lowercase. [Default: False]")
    parser.add_argument("-d", "--debug", required=False, default=False, action="store_true", dest="lower_boolean", help="Specify to enable the debug mode. [Default: False]")
    args = parser.parse_args()
    user_specified_symbol: str = args.replace_symbol
    if args.lower_boolean:
        global MAKE_LOWER
        MAKE_LOWER = True

    mac_address: str = args.mac_address

    if check_mac_address(mac_address):
        mac_address_output: str = symbol_check_mac_address(mac_address, user_specified_symbol)  #calls replace and add function
        print(mac_address_output)
        vendor, status_code = mac_address_vendor(mac_address, args.lower_boolean)
        print(vendor)

if __name__ == "__main__":
    main()