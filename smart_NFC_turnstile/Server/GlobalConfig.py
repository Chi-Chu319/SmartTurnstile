from enum import Enum
import pyodbc
# Any static settings
# urls



class Resources(Enum):
	# To access the name
	# Databases.Authen.name
	# value
	# Databases.Authen.value
	Authen = "Authen"
	Booking = "Booking"
	VisitorEnter = "Visitor_Enter"
	VisitorExit = "Visitor_Exit"
	LocalSql = '(localdb)\mssqllocaldb'
	Database = 'Smart_turnstile'
	URL = "http://localhost:5000/Authen"
	# Server = '192.168.31.43'
	imagePath = 'D:\Assignments\Year_three1\IOT_project\smart_NFC_turnstile\Server'


def InitializeConnection(SqlServer, Database):
	conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server='+Resources.LocalSql.value+';'
                      'Database='+Resources.Database.value+';'
                      'Trusted_Connection=yes;')

	return conn.cursor()

