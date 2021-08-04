#!/usr/bin/python
# -*- coding: utf-8 -*-
# import required modules

import time;
import requests;
import os.path;
from datetime import datetime;

# Define function to make API call

def call_api():
        
# Define POST request variables

        url = "https://api.meraki.com/api/v1/devices/your_sn_here/camera/generateSnapshot"

# Set Payload to enable Full Frame resolution firmware 4.2 required

        #payload = '''{ "fullframe": true }'''
        payload = '''{}'''

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Cisco-Meraki-API-Key": "your_api_key_here"
        }

# Make API Call

        response = requests.request('POST', url, headers=headers, data=payload)

        return response

def check_for_200(response):
    if response.ok:
        print('URL Server: Sure here is a link!')
        
# Wait for URL to become avalable

        time.sleep(10)
        return response
    else:
        print('URL Server: We got a problem here!')
        start_auto_snapshot()

def download_img(response):
        
# Extract download URL and store it in img_url

    img_url  = response.json()['url']

# Request image data

    get_response = requests.request('GET',img_url)
    print('Image Server: Sure thing!')
    
# Generate filename from timestamp

    now = datetime.now()
    file_name = now.strftime("%m%d%Y%H%M%S").replace(" ", "") + '.jpeg'

    complete_name = os.path.join('I:\Timelapse\Run_1', file_name)
    
# Save image to JPEG at root of project file

    file = open(complete_name,"wb")
    file.write(get_response.content)
    file.close()
    print('Image Saved!')

def start_auto_snapshot():
        
# Create loop

    while True:
        try:
                
# Store request from api_call()

                print('Ring Ring Calling!')
                url_request = call_api()
                print('Host: Hey can I get a snapshot link?')
                check_for_200(response=url_request)
                print('Host: Hey, Image Server? Can I have this file?')
        
# Download the image to the hard drive

                download_img(response=url_request)
        
# adjust time between pictures

                print('')
                time.sleep(5)

        except (Exception):
                time.sleep(30)
                start_auto_snapshot()
                print (Exception)
                        
    

start_auto_snapshot()
    
