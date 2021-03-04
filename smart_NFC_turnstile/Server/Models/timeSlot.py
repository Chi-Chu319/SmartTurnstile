import datetime
from .SqlConnector import (
	NextThreeAvailableDates, 
	TimeslotsOfaDate, 
	TimeById, 
	DateById
	)


class TimeslotDate():
	"""docstring for ClassName"""
	def __init__(self, Id, Date):
		# the Id can be initilzed as None if not set
		self.Id = Id
		self.Date = Date


class TimeslotTime():
	"""docstring for ClassName"""
	def __init__(self, Id, StartTime, Duration, DateId):
		# the Id can be initilzed as None if not set
		self.Id = Id
		self.StartTime = StartTime
		self.Duration = Duration
		self.DateId = DateId


def TimeAdd(time, durationInHours):
	delta = datetime.timedelta(hours=durationInHours)
	time_ = (datetime.datetime.combine(datetime.date(1,1,1),time) + delta).time()
	return time_		

# A static class serves as API

def NextThreeDates():
	# pull next three date from the database in a list
	return [(Id, str(date)) for (Id, date) in NextThreeAvailableDates()]

def AvailableTime(dateId):
	# get all available time using the dateId.
	return [(Id, str(time)+"-"+ str(TimeAdd(time, duration)))
	for (Id, time, duration, dateId) 
	in TimeslotsOfaDate(dateId)]

def getById(timeId):
	# return the date and time in a string format
	_, time, duration, dateId = TimeById(timeId)
	time_str = str(time)+"-"+str(TimeAdd(time, duration))
	_, date = DateById(dateId)
	return str(date)+", "+time_str
