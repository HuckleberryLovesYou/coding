###########################################################################################################
#        This code is inspired by ebola man                                                               #
#        https://www.youtube.com/@ebolaman_                                                               #
#        He made a similar program like this                                                              #
#        in C# and I thought it míght be a                                                                #
#        good idea to interpret it into phyton.                                                           #
#        The idea came from this video:                                                                   #
#        https://www.youtube.com/watch?v=oQxAVIZdktU                                                      #
#        It's also the first time for me                                                                  #
#        working with functions and f-Strings.                                                            #
#        So far I can say that I LOVE f-Strings.                                                          #
#        This code can be found at:                                                                       #
#        https://github.com/HuckleberryLovesYou/coding/blob/main/vocational-school/phyton/geolocator.py   #
#                                                                                                         #
###########################################################################################################


import requests
import json
import os



def ipinfo_request(ipinfo_request_requested_ip):
    ipinfo_api_requested_url = f"https://ipinfo.io/{ipinfo_request_requested_ip}/json"
    ipinfo_api_call = requests.get(ipinfo_api_requested_url)
    ipinfo_api_response_statuscode = ipinfo_api_call.status_code
    ipinfo_api_response_text = ipinfo_api_call.text
    ipinfo_api_response_json = json.loads(ipinfo_api_response_text)
    ipinfo_api_response_coords = f"{ipinfo_api_response_json["loc"]}"
    coord = ipinfo_api_response_coords.split(',')
    ipinfo_api_response_coord_latitude = coord[0]
    ipinfo_api_response_coord_longitude = coord[1]
    google_maps_link = f"https://www.google.com/maps/search/?api=1&query={ipinfo_api_response_coord_latitude},{ipinfo_api_response_coord_longitude}"
    print(f"The IP '{ipinfo_request_requested_ip}' is located in {ipinfo_api_response_json["postal"]} {ipinfo_api_response_json["city"]} in {ipinfo_api_response_json["region"]} in {ipinfo_api_response_json["country"]}")
    print(f"The coordinats are: {ipinfo_api_response_json["loc"]}")
    print(f"Generated Google Maps Link: {google_maps_link}")
    # print(f"The call uri was {requested_url}")
    if not ipinfo_api_response_statuscode == 200:
        print(f"API-Call failed\nYour api_call returned {ipinfo_api_response_statuscode} status code")
        return ipinfo_api_response_statuscode
    else:
        return ipinfo_api_response_statuscode

def main():
    while True:
        requested_ip = input("Bitte gib hier deine IP-Adresse ein\n\n")
        print("\n"*25)
        if requested_ip == "":
            print("\n" * 25)
            exit("Process finished with exit code: UserMadeNoEntry")
        else:
            ipinfo_api_response_statuscode = ipinfo_request(requested_ip)
            print(f"\n\n{ipinfo_api_response_statuscode=}\n")



if __name__ == "__main__":
    main()
