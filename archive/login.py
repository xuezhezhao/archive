import requests
import json
url_ar='http://123.57.39.4:2222/api/admin/login/login'
payload={"accountName":"admin","password":"11111111"}
headers = {'Content-Type': "application/json", }
result=requests.post(url_ar,headers=headers,data=json.dumps(payload))
print(result.json())
print(result.cookies)
cookies=result.cookies
print(requests.utils.dict_from_cookiejar(cookies))