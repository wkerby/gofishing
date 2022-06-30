#create custom error for incorrect time
class TimeError(Exception):
	def __init__(self,time,message):
		super.__init__(message)
		self.time = time
#create user-defined function that returns safe starting fishing hour at various locations along Chattahoochee River
#e.g. gofishing("10PM","Jones Bridge")
def gofishing(timestr,location):
	receed_dict = {'Settles':3,'Mcginnis':6,'Abbots':8,'Jones Bridge':14,'Island Ford':20}
	if timestr[-2:].lower() == "pm":
		ind = timestr.lower().find("pm")
		hour = int(timestr[:ind]) + 12 + receed_dict[location]
	elif timestr[-2:].lower() == "am":
		ind = timestr.lower().find("am")
		hour = int(timestr[:ind]) + receed_dict[location]
	else:
		raise TimeError(timestr,"You entered an invalid time format")
	if hour >= 24:
		hour -= 24
	if hour == 0:
		return "Safe to wade beginning at 12 AM"
	elif hour == 12:
		return "Safe to wade beginning at 12 PM"
	elif hour > 12:
		return "Safe to wade beginning at " + str(hour - 12) + " PM"
	elif hour > 0 and hour < 12:
		return "Safe to wade beginning at " + str(hour) + " AM"

try:
	print(gofishing("5PM","Jones Bridge"))
except TimeError as te:
	print(te, ":", te.time[-2:])

from datetime import date
from datetime import datetime
timenow = datetime.now()
GREdate = date(2022,7,29)
today = date.today()
print(GREdate - today)

somelist = [1,2,3,4,15,20,30,45]

for timeframe in somelist:
	if timeframe >= 15:
		if somelist.index(timeframe) == len(somelist) -1:
			print(str(timeframe) + " mins", end = "")
		else:
			print(str(timeframe) + " mins", end = ",")
	elif timeframe == 1:
		print(str(timeframe) + " hr", end = ",")
	else:
		print(str(timeframe) + " hrs", end = ",")