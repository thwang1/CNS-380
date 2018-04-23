##### Web Brute Force #####
##### CNS-380/597 Advanced Cybersecurity Automation - Ryan Haley####


'''
During your pentest you find a website that you believe to be of high value.
You decide to probe it to find any webpages it might be hiding and hopefullly
return a page with that you can use to gather contact information.

Write a script that will take in a list of file paths (you can use the txt
file provided WebPath.txt) and check them against the given website.
The script will then notify the user which link(s) were successful.

You then must scrape the webpage of any directories/files that were found and
return any phone numbers and email addresses you find on the page.

NOTE: This problem is only to be done against the given URL.
'''

from requests import request
import re

url = 'https://www.secdaemons.org/'
f = open("WebPath.txt","r")
filePaths = f.read().split("\n")
f.close()
    
for filePath in filePaths:
        response = request("GET",url+"/"+filePath,verify=False)
        if response.status_code == 200:
            print(filePath)
            con = response.content.decode("utf-8")
            phNum = re.findall('\(?\d{3}\)?.?\d{3}.?\d{4}',con)
            email = re.findall('[\w.-]+@[\w.-]+',con)
            print(phNum)
            print(email)




