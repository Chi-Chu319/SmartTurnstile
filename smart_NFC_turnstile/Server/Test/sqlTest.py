import pyodbc 
import datetime
import sys

sys.path.insert(1, '../')
from GlobalConfig import *

# LocalSql = '(localdb)\mssqllocaldb'
# Database = 'Smart_turnstile'

cursor = InitializeConnection(Resources.LocalSql, Resources.Database)





# for driver in pyodbc.drivers():
# 	print(driver)
# conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
#                       'Server=(localdb)\mssqllocaldb;'
#                       'Database=Smart_turnstile;'
#                       'Trusted_Connection=yes;')

# cursor = conn.cursor()
# # cursor.execute("INSERT INTO [dbo].[Booking]\
# #            ([Name]\
# #            ,[Time])\
# #      VALUES\
# #            ('John','20201119 15:06:12')")
# # conn.commit()


# # cursor.execute("EXEC   [dbo].[InsertBooking]\
# # 		@Name = N'john',\
# # 		@Time = N'20201119 11:11:11'")
# # cursor.commit()

# # cursor.execute("exec dbo.DeleteAllBookings")
# # cursor.commit()

# cursor.execute('SELECT * FROM dbo.Booking')
# for row in cursor:
#     print(row[0])


