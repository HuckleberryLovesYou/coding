import requests

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
        print(f"\n\n\n{mac_address_vendor_api_call.status_code=}")
        print(f"{mac_address_vendor_api_call.elapsed=}")
        print(f"{mac_address_vendor_api_call.raw=}")
        print(f"{mac_address_vendor_api_call.reason=}")
        print(f"{mac_address_vendor_api_call.__hash__()=}\n\n\n")
    return mac_address_vendor_api_call.text , mac_address_vendor_api_call.status_code



def main():
    debug_mode_char: str = "§"
    user_specified_symbol: str = input("Please enter your Symbol you want to add in or replace with. Leave clear if the mac should be without any spacing:\n")
    if user_specified_symbol[len(user_specified_symbol)-1] == debug_mode_char:
        user_specified_symbol = user_specified_symbol[:len(user_specified_symbol)-1]
        debug_enabled = True
        print("Entering debug mode because you have entered " + debug_mode_char + " stats will be shown")
        print(f"Entering debug mode because you have entered {debug_mode_char=}\nMore stats will be shown")
    else:
        debug_enabled = False
    while True:
        mac_address_input: str = input(f"\nPlease enter your valid MAC to add or replace with the following before defined symbol '{user_specified_symbol}' :\n")
        print("\n" * 15)
        if check_mac_address(mac_address_input):
            mac_address_output: str = symbol_check_mac_address(mac_address_input, user_specified_symbol)  # also calls replace and add function
            print(mac_address_output)
            vendor, status_code = mac_address_vendor(mac_address_input, debug_enabled)
            print(vendor)

if __name__ == "__main__":
    main()