import requests
import fittings

proxyIPs = {"http" : "http://127.0.0.1:8080", "https" : "https://127.0.0.1:8080"} #useful if you want to review the requests with Burp

def makeSubmission(strawUser:fittings.appliances.Strawman):
    url = "TARGET URL HERE"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "54",
        "Origin": "null",
        "Connection": "close"
    }
    data = {"email": strawUser.email, "password": strawUser.password}  #season to taste when you see the actual request
    response = requests.post(url, data, headers = headers, proxies = None, verify = True, allow_redirects=False) #set verify to false and proxies to proxyIPs for inspecting requests in transit
    return response


if __name__ == "__main__":
    import fittings
    submitter = makeSubmission
    fittings.hoses.multiAlarm(submitter)