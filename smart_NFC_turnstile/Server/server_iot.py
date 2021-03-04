import Models.authen as authen
import Models.booking as booking
import Models.timeSlot as timeSlot
import Models.visitorEnter as visitorEnter
import datetime
import json
from flask import (
	Blueprint,
	request, 
	jsonify
	)


with open('./config.json', 'r') as f:
    config = json.load(f)

iotAPI = Blueprint("iotAPI", __name__)

""" for iot devices """

# @app.route("/", methods=["GET"])
# def Hello():
# 	if request.method == "GET":
# 		return 'Hello! this is yours web server.'


# https://www.google.com/search?q=hello
# get request only handle parameters while POST/PUT/DELETE deal with data
# request.args
# request.data
# authenticate the incomming Id
@iotAPI.route("/IOT/VerifyAuth", methods=["POST"])
def verifyAuth():
	# verify the KeyUID
	# check the time
	# initialize a visitor enter entry
	# return the verification(time, UID), message, the visitor Enter Id
	enterId = visitorEnter.NewEnter()
	message = ""
	valid = False
	keyUID = request.form["keyUID"]
	exists, authId = authen.KeyUIDExists(keyUID)
	if exists:
		now = datetime.datetime.now()
		strart, end = authen.BookedTime(authId)
		if strart < now < end:
			visitorEnter.UpdatAuthenId(enterId, authId)
			message = "Identity verified"
			valid =True
		else:
			message = "Not within booked time."
	else:
		message = "Invalid card."
	return jsonify(exists=exists, valid=valid, message=message, enterId=enterId)




@iotAPI.route("/IOT/Visitors/Enter/UpdateInfo", methods=["POST"])
def updateInfo():
	# update all the info (temperature, photopath, permission)
	permission = False
	message = ""
	visitorEnterId = request.form["visitorId"]
	temperature = float(request.form['temperature'])
	photo = request.files['photo']
	# TODO fix the photo saving method
	photopath = visitorEnter.SavePhoto(visitorEnterId, photo)
	visitorEnter.UpdateTemp(visitorEnterId, temperature)
	if temperature < config["temperatureThreshold"]:
		# enter permitted
		visitorEnter.UpdatePermission(visitorEnterId)
		permission = True
		message = "Access permitted."
	else:
		# enter denied
		message = "Access denied"
	return jsonify(permission=permission, message=message)



# @iotAPI.route("IOT/Visitors/Enter/Create", methods=["GET"])
# def Create():
# 	# return the id
# 	return visitor.NewEnter(request.args['dateTime'])

# @iotAPI.route("/IOT/Visitors/Enter/<int:id>/Temp", methods=["POST"])
# def UpdateTemp(id):
# 	# update the temp
# 	visitor.UpdateTemp(Id, request.data['Temp'])

# @iotAPI.route("/IOT/Visitors/Enter/<int:id>/AuthenId", methods=["POST"])
# def UpdateAuthenId(id):
# 	# update the AuthenId
# 	visitor.UpdatAuthenId(Id, request.data['AuthenId'])

# @iotAPI.route("/IOT/Visitors/Enter/<int:id>/Image", methods=["POST"])
# def UpdateImage(id):
# 	photo = request.data['Photo']
# 	# todo save the photo
# 	photo.save()
# 	photoPath = photo.path
# 	visitor.UpdatePhotoPath(Id, photoPath)


if __name__ == "__main__":
	iotAPI.run(debug=True, host= '0.0.0.0')