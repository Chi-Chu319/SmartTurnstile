
import Models.booking as booking
import Models.timeSlot as timeSlot
import Models.authen as authen
from flask import (
	Blueprint, 
	request, 
	render_template, 
	redirect, 
	url_for, 
	session,
	)

'''
each time a request comes to the server, the script will be run again from the begining
so global variable will be initialized again
but the session will not
g is only alive in one request
session(cookie) is stored in browser
'''

visitorAPI = Blueprint("visitorAPI", __name__, static_folder="./static")
# # the secret key encrypts the session data 
# app.secret_key = "Key"

def validate(form):
	# validate imformation 
	# if any of the imformation is empty, Then, its not valid
	result = True
	message = ""
	if form["Name"] == "": 
		result = False
		message += "name, "
	if form["Email"] == "":
		result = False
		message += "email, "
	messageList = list(message)[:-2]
	messageList.append(".")
	return result, "".join(messageList)

""" visitor webpage """


# @app.route("/", methods=["GET"])
# def index():
# 	return redirect(url_for("collectInfo"))


@visitorAPI.route("/Booking/CollectInfo", methods=["GET", "POST"])
def collectInfo():
	# make sure no enter the booking page with out filling in info
	errorMessage = ""
	if "errorMessage" in session:
		errorMessage = session["errorMessage"]
		session.pop("errorMessage", None)
	if request.method == "POST":
		# flush the cookie when try to login
		session.pop("bookingName", None)
		session.pop("bookingEmail", None)
		validation, message = validate(request.form)
		if validation:
			""" the booking imformation will be complete with 
			 the time booked from booking method"""
			session["bookingName"] = request.form["Name"]
			session["bookingEmail"] = request.form["Email"]
			# the cookie(http session) is stored in the browser and needs to be cleaned from application with code
			# clear session with session.clear() or session.pop(key) 
			# !!! object can not be stored in session
			return redirect(url_for("visitorAPI.bookTime"))
		else:
			errorMessage = " The following field is misssing: " + message
	return render_template("personalInfo.html", error = errorMessage)

@visitorAPI.route("/Booking", methods=["GET", "POST"])
def bookTime():
	if "bookingName" in session:
		# handling time booking
		# session should be cleared when the booking is completed
		dates = timeSlot.NextThreeDates()
		times = None
		if request.method=="POST":
			# The date and time form data are sent in squence
			if "DateId" in request.form:
				#set the date data in cookie, bring up the corresponding timeslots
				dateId = request.form["DateId"]
				times = timeSlot.AvailableTime(dateId)
			elif "TimeId" in request.form:
			 	# complete form, clear the session, save to database, redirect to review
				timeId = request.form["TimeId"]
				bookingId = booking.Booking(session["bookingName"], session["bookingEmail"], timeId).SaveToDB()
				authen.NewAuthen(bookingId)
				session.clear()
				return redirect(url_for("visitorAPI.bookingReview", bookingId=bookingId))
		return render_template("booking.html", dates=dates, times=times)
	else:
		# When the imformation is not filled in 
		session["errorMessage"] = "Please fill in your personal information before booking a time"
		return redirect(url_for("visitorAPI.collectInfo"))

@visitorAPI.route("/Booking/Review", methods=["GET", "POST"])
def bookingReview():
	# review the booking
	# booking = Booking.getById(Id)
	bookingId = request.args["bookingId"]
	b = booking.getById(bookingId)
	t = timeSlot.getById(b.timeslotId)
	return render_template("bookingReview.html", booking=b, time=t)




if __name__ == "__main__":
	visitorAPI.run(debug=True, host= '0.0.0.0')