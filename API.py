import urllib3
def getMonsters():
    resp = urllib3.request("GET", "https://mhw-db.com/monsters")
    print(resp.status)
    print(resp.data)
    return resp.data

def getSets():
    resp = urllib3.request("GET", "https://mhw-db.com/armor/sets")
    print(resp.status)
    print(resp.data)
    return resp.data

def getWeapons():
    resp = urllib3.request("GET", "https://mhw-db.com/weapons")
    print(resp.status)
    print(resp.data)
    return resp.data