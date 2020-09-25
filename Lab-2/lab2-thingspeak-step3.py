#Code refactored from github account 'soumilshah1995'

import urllib.request
import requests
import threading
import json

import random


def read_data_thingspeak():
    URL='https://api.thingspeak.com/channels/1155617/feeds.json?api_key='
    KEY='FJ3SE4AUKO261QRD'
    HEADER='&results=2'
    NEW_URL=URL+KEY+HEADER
    print(NEW_URL)

    get_data=requests.get(NEW_URL).json()
    #print(get_data)
    channel_id=get_data['channel']['id']

    feild_1=get_data['feeds']
    #print(feild_1)

    t=[]
    for x in feild_1:
        #print(x['field1'])
        t.append(x['field1'])
    
    print(t)

if __name__ == '__main__':
    #thingspeak_post()
    read_data_thingspeak()