import datetime
from .SqlConnector import SaveBooking, BookingById


class Booking:
    def __init__(self, Name, Email, timeslotId, Id=None, entryTime=datetime.datetime.now()):
        # initilze from a http form data
        self.Id = Id
        self.Name = Name
        self.Email = Email
        self.timeslotId = timeslotId
        self.entryTime = entryTime

    def SaveToDB(self):
        # save the complete booking to database
        self.Id = SaveBooking(self.Name, self.Email, self.timeslotId, self.entryTime)
        return self.Id


    def __str__(self):
        return str(self.__dict__).replace("{", "").replace("}", "")

def getById(bookingId):
    # get the booking from database and initialize it a object
    booking_tuple = BookingById(bookingId)
    booking_tuple, entryTime= booking_tuple[1:-1], booking_tuple[-1]
    booking = Booking(*booking_tuple, entryTime=entryTime)
    return booking

if __name__ =="__main__":
	# test
	pass
	# b = Booking({"Name":"name", "Email":"Email@email.com"})
	# print(str(b))


		