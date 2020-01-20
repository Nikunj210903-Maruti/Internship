
'''
from requests.auth import HTTPBasicAuth
import requests

username = '407b7065-7f36-4dc4-98a9-9dd47afce24'
password = 'a366ea21-8b83-45c9-a81c-9bd9a85014fa'

if not username or not password:
    raise Exception("Please provide username and password")

karix_authentication_url = 'https://api.karix.io/account/'+ str(username)
res = requests.get(karix_authentication_url,auth=HTTPBasicAuth(username,password))
print(res.status_code)
'''

from enum import Enum


class test(Enum):
  one = "whatsapp"

print(test['one'].name)

