from .timeSlot import TimeAdd
import datetime
from .SqlConnector import (
	SaveAuthen, 
	GetNonActivatedAuths,
	ActivateAuthWithUID,
	KeyUIDExists,
	AuthById,
	BookingById,
	TimeById,
	DateById
	)


class Authen:
	def __init__(self, Id, keyUID, Booking):
		# the Id can be initilzed as None if not set
		self.Id = Id
		self.keyUID = keyUID
		self.Booking = Booking

def Verify(AuthenKey):
	return KeyUIDExists(AuthenKey)

def NewAuthen(bookingId):
	# save a not activated auth
	SaveAuthen(bookingId)

def NonActivatedAuths():
	rows = GetNonActivatedAuths()
	result = []
	for i in rows:
		result.append(i[0])
	return result


def ActivateAuth(authId, UID):
	# update the authen KeyUID and Activated status in Database
	UID = "0x"+str(UID)
	# print(UID)
	ActivateAuthWithUID(authId, UID)

def KeyUsed(KeyUID):
	return KeyUIDExists(KeyUID)

def BookedTime(authId):
	# return the start and end time
	bookingId = AuthById(authId)[2]
	timeslotId = BookingById(bookingId)[3]
	_, time_start, duration, dateId = TimeById(timeslotId)
	time_end = TimeAdd(time_start, duration)
	date = DateById(dateId)[1]
	datetime_start = datetime.datetime.combine(date, time_start)
	datetime_end = datetime.datetime.combine(date, time_end)
	return datetime_start, datetime_end






