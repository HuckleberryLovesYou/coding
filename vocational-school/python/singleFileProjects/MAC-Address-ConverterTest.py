import requests
import argparse
import csv
from os.path import exists
from tkinter.filedialog import askopenfilename
from time import sleep

MAKE_LOWER: bool = False
FILENAME: str = ""


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
            mac_address_output += user_specified_symbol
        else:
            if MAKE_LOWER:
                mac_address_output = mac_address[i].lower()
            else:
                mac_address_output = mac_address[i].upper()
    return mac_address_output

def decide_convertion_algorithm(mac_address: str, user_specified_symbol: str) -> str:
    if mac_address[2] in mac_address_array_all:  # checks if there is already spacing between every 16bit
        mac_address = add(mac_address, user_specified_symbol)
    else:
        mac_address = replace(mac_address, user_specified_symbol)
    return mac_address

def is_valid_mac_address(mac_address: str) -> bool:
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

def get_file_path(): #let the user select a .csv-file and writes it into global_filename
    def is_valid_file(filepath) -> bool: #checks if file actually exists (might not be needed)
        if exists(filepath):
            print("CSV-File found")
            return True
        else:
            print("No csv selected")
            return False
    global FILENAME
    FILENAME = askopenfilename(title="Select a CSV-File:", filetypes=[("csv files" , "*.csv")])
    return FILENAME, is_valid_file(FILENAME)


def process_csv_file():
    with open(FILENAME, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=" ")
        mac_addresses = []
        for row in reader:
            split = row[0].split(",")
            if split[3] != "000000000000":
                mac_addresses.append(split[3])
        mac_address_vendors = []
        for mac_address in mac_addresses:
            vendor = run(mac_address, "-")
            mac_address_vendors.append(vendor)
            sleep(1)
    with open(FILENAME + "_lookup", "a") as txt_file:
        for i in mac_address_vendors:
            txt_file.write(f"{mac_addresses[i]}: {mac_address_vendors[i]}")



def str2bool(input: str) -> bool:
    if input.lower() == "true":
        return True
    elif input.lower() == "false":
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean expected")

def get_cli_args():
    parser = argparse.ArgumentParser("This is a Converter which converts MAC Address Notation to a other one [e.g. 'E8-9C-25-DC-A5-EA' -> 'E8:9C:25:DC:A5:EA']\nIt will also lookup the vendor of the MAC Address\n\n\t©timmatheis-de")
    parser.add_argument("-m", "--Mac-Address", required=True, action="store", dest="mac_address", help="Provide MAC Address in supported format", type=str)
    parser.add_argument("-r", "--replace", required=False, default="-", action="store", dest="replace_symbol", help="Enter symbol for replacing [Default: '-']", type=str)
    parser.add_argument("-l", "--lower", required=False, default=False, action="store_true", dest="lower_boolean", help="Specify to change the MAC Address to only lowercase. [Default: False]", type=str2bool)
    parser.add_argument("-d", "--debug", required=False, default=False, action="store_true", dest="debug_boolean", help="Specify to enable the debug mode. [Default: False]", type=str2bool)
    parser.add_argument("-f", "--file", required=False, default=False, action="store_true", dest="file_boolean", help="Specify to select file afterwards.", type=str2bool)
    return parser.parse_args()
def main() -> None:
    try:
        args = get_cli_args()
        mac_address: str = args.mac_address
        replace_symbol: str = args.replace_symbol

        if args.lower:
            global MAKE_LOWER
            MAKE_LOWER = True

        if args.file is not None:
            get_file_path()

    except:
        mac_address = input("Enter MAC Address: ")
        replace_symbol = input("Enter replace symbol [e.g. '-' or ':'] ")
        enable_debug = input("Enter 'y' to enable debug mode: ").lower
        debug_enabled = False
        if enable_debug == "y":
            debug_enabled = True

        if is_valid_mac_address(mac_address):
            mac_address_output: str = decide_convertion_algorithm(mac_address, replace_symbol)  #calls replace and add function
            print(mac_address_output)
            vendor, status_code = mac_address_vendor(mac_address, debug_enabled)
            print(vendor)

if __name__ == "__main__":
    main()