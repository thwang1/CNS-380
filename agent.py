import hashlib
import time
import os
import requests

def virustotal(fname):
    apikey = '125e679cfa0626662ef1231dbca4b8e37226591efbd8c4884e2328085620fd0d'

    # post scan
    scanUrl = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': apikey}
    files = {'file': (fname, open(fname, 'rb').read())}
    response = requests.post(scanUrl, files=files, params=params)
    response = response.json()

    # get resource
    resource = response["resource"]
    
    # get report
    reportUrl = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': apikey, 'resource': resource}
    response = requests.get(reportUrl, params=params)

    response = response.json()

    total = response["total"]
    detected = response["positives"]    

    percent = (detected/total)*100
    
    return percent

BASE_FILES = dict()
SERVER = "http://localhost:8080/api/add"

for fname in os.listdir("."):
    if os.path.isfile(fname):
        try:
            md5_checksum = hashlib.md5((open(fname,"rb").read())).hexdigest()
            BASE_FILES.update({fname:md5_checksum})
        except Exception as e:
            print(e)

while True:
    time.sleep(5)
    for fname in os.listdir("."):
        if os.path.isfile(fname):
            try:
                md5_checksum = hashlib.md5((open(fname,"rb").read())).hexdigest()
                if md5_checksum not in BASE_FILES.values():
                    print(fname)
                    calc_percent = virustotal(fname)
                    if calc_percent >= 50:
                        print("Delete the file!")
                        os.remove(fname)
                        data = {"data":"Deleted \"{}\" with MD5 checksum {}".format(fname,md5_checksum)}
                    else:
                        BASE_FILES.update({fname:md5_checksum})
                        data = {"data":"Allowed \"{}\" with MD5 checksum {}".format(fname,md5_checksum)}
                    requests.post(SERVER,data=data)		
            except Exception as e:
                print(e)










