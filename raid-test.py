#! /usr/bin/env python3
#
# example RAiD integration
#
#
# Andrew Janke - a.janke@gmail.com


import sys
import os.path
import os
import json
import requests
import urllib

Username = 'QCIFredbox'
ApiKey = 'f82ac16bec53a4418ffe8663fada204d1ba571c4'
Url = 'http://api.raid.org.au:8000/'

# main upload routine
if __name__ == "__main__":

    raid_headers = {
        "Authorization": "Token %s" % (ApiKey)}
    url = Url + 'raids/?format=json'

    # check RAiD's
    print("Checking a RAiD")
    response = requests.get(
        headers=raid_headers,
        url=url)

    print ("Status code: " + str(response.status_code) + "\n")
    if response.status_code < 200 or response.status_code >= 300:
        raise Exception("Failed to get RAiD.")
    else:
        print(url)
        print(json.dumps(response.json()))
        print("response.status_code = " + str(response.status_code))


    # create a RAiD
    print("\nCreating a RAiD")
    response = requests.post(
        headers = raid_headers,
        url = url)
    if response.status_code != 201:
        print("   + E FAIL Code: " + str(response.status_code))
    else:
        print(url)
        print(json.dumps(response.json()))
        print("response.status_code = " + str(response.status_code))
