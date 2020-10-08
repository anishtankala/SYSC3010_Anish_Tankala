#key = AT68QYQ94MQEWXL3
#field 1 : group, field 2: cmail, field3: identifier 

#Code taken from website 'https://iotdesignpro.com/projects/how-to-send-data-to-thingspeak-cloud-using-raspberry-pi'
import http.client
import urllib.parse
import time
key = "AT68QYQ94MQEWXL3"  # Put your API Key here

def lab4():
    while True:    
        f1 = "L3-T-1" #field 1
        f2 = "anishtankala@cmail.carleton.ca" #field 2
        f3 = "c" #field 3
        params = urllib.parse.urlencode({'field1': f1, 'field 2': f2,'field 3': f3, 'key': key })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(f1)
            print(f2)
            print(f3)
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        break
        
if __name__ == "__main__":
    lab4()
