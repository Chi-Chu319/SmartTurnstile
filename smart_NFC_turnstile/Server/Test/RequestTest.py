import requests
import datetime

URL = "http://192.168.31.43:5000"

r = requests.get(url = URL+'/Visitors/Enter/Create', params = {'dateTime':datetime.datetime.now().replace(microsecond=0)}).json()



print(r)