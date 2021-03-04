import requests
import json


with open('./config.json', 'r') as f:
    config = json.load(f)

endpoint = config["endpoint"]
port = config["port"]
url = endpoint+":"+str(port)


def nonActivatedAuths():
    # TODO implement with a request class 
	r = requests.get(url+'/Admin/NonActivatedAuths').json()
	Ids = r['Ids']
	result = []
	for i in Ids:
		result.append("Id: {}".format(i["Id"]))
	return result



def registerCardId(username, password, authId, keyUID):
	# keyUID in binary form
	# send request to the API, return status message if there is any
	auth = (username, password)
	data = {"keyUID": keyUID}	
	params = {"authId": authId}
	r = requests.post(url+'/Admin/Register', auth=auth, params=params, data=data)
	if r.status_code == 401:
		return ("error", "Wrong username or password")
	responds = r.json()
	if "error" in responds:
		return ("error", responds["error"])
	elif "message" in responds:
		return ("message", responds["message"])



if __name__ == '__main__':
	auth = ('admin', 'admin')
	data = {"keyUID": b'123'}	
	params = {"authId": 3}
	r = requests.post('http://192.168.31.43:5000/Admin/Register',auth =auth, params=params,data=data)
	print(r.text)