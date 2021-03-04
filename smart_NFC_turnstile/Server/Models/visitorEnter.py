import json
import datetime
from .SqlConnector import (
	CreateVisitorEnter,
	UpdateVisitorEnterAuthenId,
	UpdateVisitorEnterTemp,
	UpdateVisitorEnterPermission,
	UpdateVisitorEnterPhotoPath
)

with open('./config.json', 'r') as f:
    config = json.load(f)

class VisitorEnter():
	"""docstring for ClassName"""
	def __init__(self, Time, Temperature, PhotoPath, Id=None, Permission=False):
		# the Id can be initilzed as None if not set
		self.Id = Id
		self.Time = Time
		self.Temperature = Temperature
		self.PhotoPath = PhotoPath
		self.Permission = Permission

def NewEnter():
	# create a new visitor entry in the database with the time
	# return Id
	row = CreateVisitorEnter(datetime.datetime.now())
	return int(row[0])

def UpdateTemp(Id, Temp):
	UpdateVisitorEnterTemp(Id, Temp)

def UpdatAuthenId(Id, AuthenId):
	UpdateVisitorEnterAuthenId(Id, AuthenId)

def __UpdatePhotoPath(Id, PhotoPath):
	UpdateVisitorEnterPhotoPath(Id, PhotoPath)

def SavePhoto(Id, photo):
	# TODO save the photo 
	path = config["photoPath"]
	photoPath = photo.save(path+"\\"+"{}.jpg".format(Id))
	__UpdatePhotoPath(Id, photoPath)


def UpdatePermission(Id):
	# set the permission to True
	UpdateVisitorEnterPermission(Id)



		

