import sys
import json
import datetime
import pyodbc

'''
Handles the connection to the database
return raw data from the DB
'''

with open('./config.json', 'r') as f:
    config = json.load(f)


DBusername = config["DBusername"]
DBpassword = config["DBpassword"]



conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                  'Server='+config["SQL"]+';'
                  'Database='+config["Database"]+';'
                  'Trusted_Connection=yes;'
                  )



cursor = conn.cursor()


# cursor = InitializeConnection(Resources.LocalSql, Resources.Database)

''' Authen '''

def KeyUIDExists(UID):
	# return the True or False as the verdit
	# if the key exists, return the AuthId, else None
	# takes in key without "0x"
	# print(UID)
	cursor.execute("{CALL KeyUIDExists (?)}", ("0x"+UID))
	row = cursor.fetchone()
	return (row!=None, row[0] if row != None else None)

def SaveAuthen(bookingId):
	# save to DB with only foreign key of the booking ID
	cursor.execute("{CALL InsertAuthen (?)}", (bookingId))
	cursor.commit()

def GetNonActivatedAuths():
	cursor.execute("{CALL SelectNonActivatedAuths}")
	rows = cursor.fetchall()
	return rows

def ActivateAuthWithUID(authId, UID):
	# register the card UID and activate the entry in the database
	cursor.execute("{CALL UpdateAuth (?,?)}", (authId, UID))
	cursor.commit()


def AuthById(Id):
	cursor.execute("{CALL SelectAuthById (?)}", (Id))
	return cursor.fetchone()




''' visitorEnter '''

def CreateVisitorEnter(Time):
	output = 0
	cursor.execute("{CALL CreateVistorEnter (?)}", (Time))	
	row = cursor.fetchone()
	cursor.commit()
	return row

def UpdateVisitorEnterTemp(Id, Temp):
	cursor.execute("{CALL UpdateVisitorEnterTemp (?, ?)}", (Id, Temp))
	cursor.commit()


def UpdateVisitorEnterAuthenId(Id, AuthenId):
	cursor.execute("{CALL UpdateVisitorEnterAuthenId (?, ?)}", (Id, AuthenId))
	cursor.commit()

def UpdateVisitorEnterPhotoPath(Id, PhotoPath):
	cursor.execute("{CALL UpdateVisitorEnterPhotoPath (?, ?)}", (Id, PhotoPath))
	cursor.commit()

def UpdateVisitorEnterPermission(Id):
	cursor.execute("{CALL UpdateVisitorEnterPermission (?)}", (Id))
	cursor.commit()


''' timeslot '''
def NextThreeAvailableDates():
	cursor.execute("{CALL NextThreeBookingDates}")
	return cursor.fetchall()

def TimeslotsOfaDate(DateId):
	cursor.execute("{CALL TimeslotOfaDate (?)}",(DateId))
	return cursor.fetchall()

def TimeById(timeId):
	# get time by Id
	cursor.execute("{CALL SelectTimeById  (?)}", (timeId))
	return cursor.fetchone()

def DateById(dateId):
	# get date by Id
	cursor.execute("{CALL SelectDateById  (?)}", (dateId))
	return cursor.fetchone()

''' booking '''
def SaveBooking(Name, Email, timeslotId, entryTime):
	# save booking, return the Id of the scope
	cursor.execute("{CALL InsertBooking  (?,?,?,?)}", (Name,Email,timeslotId,entryTime))
	bookingId = cursor.fetchone()[0]
	cursor.commit()
	return bookingId

def BookingById(bookingId):
	# return the booking in a tuple format
	cursor.execute("{CALL SelectBookingById  (?)}", (bookingId))
	return cursor.fetchone()

# cursor = VerifyAuthen('Key')
# # the cursor it self is not subscriptable data can be accessed with in statement
# # if the result is empty the for in statment will yield empty
# for row in cursor:
# 	print('Hello')

if __name__ == "__main__":
	# output = 0
	# time = datetime.datetime.now().replace(microsecond=0)
	# var = CreateVisitorEnter(time)
	# print(var)

	print(KeyUIDExists('7914FC6E'))