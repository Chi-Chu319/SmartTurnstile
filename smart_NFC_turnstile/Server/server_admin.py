import Models.authen as authen
from flask import Blueprint, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import json

with open('./config.json', 'r') as f:
    config = json.load(f)


adminAPI = Blueprint("adminAPI", __name__)
auth = HTTPBasicAuth()



users = {i["username"]:generate_password_hash(i["password"]) for i in config["users"]}

# users = {
#     "admin": generate_password_hash("admin")
# }


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return True
    else:
    	return False


@adminAPI.route("/Admin/NonActivatedAuths", methods=["GET"])
def allAuths():
	return jsonify(Ids=[{"Id": i} for i in authen.NonActivatedAuths()])


@adminAPI.route("/Admin/Register", methods=["POST"])
@auth.login_required
def Register():
	authId = int(request.args["authId"])
	Ids = authen.NonActivatedAuths()
	# make sure the auth is not activated
	if authId not in Ids:
		return jsonify(error="Auth not exists or already registered.")
	keyUID = request.form["keyUID"]
	# make sure the UID is in correct format
	if len(keyUID) != 8:
		return jsonify(error="UID not in correct format.")
	elif authen.KeyUIDExists(keyUID)[0]:
		return jsonify(error="Tag already used.")
	authen.ActivateAuth(authId, keyUID)
	return jsonify(message="Key registered.")
	    



if __name__ == "__main__":
	# adminAPI.run(debug=True, host= '0.0.0.0')
	pass