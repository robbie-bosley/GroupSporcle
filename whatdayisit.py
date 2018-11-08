import datetime
dayofyear = datetime.datetime.now().timetuple().tm_yday


print dayofyear - 205

#so the date today is 80, and is 12/10/2018. That's day 285 in the year, so day 0 is day 205 this year.
