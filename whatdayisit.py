import datetime
dayofyear = datetime.datetime.now().timetuple().tm_yday
#print dayofyear
#print 365-205
year =  datetime.datetime.now().timetuple().tm_year
yearafter = year - 2019
if (year%4 == 0):
    leap = 1
else:
    leap = 0
yearmod = 160 + (yearafter * 365) + leap
#print (dayofyear + 160)
print (dayofyear + yearmod)
#so the date today is 80, and is 12/10/2018. That's day 285 in the year, so day 0 is day 205 this year.
