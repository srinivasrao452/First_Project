
import requests
BASE_URL = "http://127.0.0.1:6655/"
ENDPOINT = "jsondata/"
# ENDPOINT = "empdata/"

FINAL_URL = BASE_URL + ENDPOINT

resp = requests.get(FINAL_URL)

print(resp.json())
# print(resp.text)
print("status code is :" ,resp.status_code )













# import requests
# BASE_URL = 'http://127.0.0.1:7788/'
# ENDPOINT = 'empdata/'
#
# FINAL_URL = BASE_URL + ENDPOINT
# #http://127.0.0.1:8877/empdata/
#
# resp = requests.post(FINAL_URL)
# # print(resp.json())
# print(resp.text)
# print("Status code is :",resp.status_code)