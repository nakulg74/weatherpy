#Nakul Gupta
#2017068
# function to get weather response
def weather_response(location, API_key):
	import urllib.request
	a="http://api.openweathermap.org/data/2.5/forecast?q="+location+"&APPID="+API_key
	d=urllib.request.urlopen(a).read().decode()
	return d
	# write your code 

# function to check for valid response 
def has_error(location,json):
	u=json.count('name')
	if (json[u+4:u+len(location)+5]==location):
		return False
	else:
		return True
	# write your code 

# function to get attributes on nth day
def get_temperature (json, n=0, t="3:00:00"):
	import datetime
	x=datetime.date.today()
	y=datetime.timedelta(days=n)
	z=x+y
	a=str(z)+" "+t
	b=json.find(a)
	c=json.rfind('"temp"')
	d=json.index(',',c)
	f=json.index(':',c)
	e=json[f+1:d]	
	e=float(e)
	# write your code 
	return e 

def get_humidity(json, n=0, t="3:00:00"):
	import datetime
	x=datetime.date.today()
	y=datetime.timedelta(days=n)
	z=x+y
	a=str(str(z)+" "+t)
	b=json.find(a)
	c=json.rfind('"humidity"')
	d=json.index(',',c)
	f=json.index(':',c)
	e=json[f+1:d]
	e=float(e)
	# write your code 
	return e 

def get_pressure(json, n=0, t="3:00:00"):
	import datetime
	x=datetime.date.today()
	y=datetime.timedelta(days=n)
	z=x+y
	a=str(str(z)+" "+t)
	b=json.find(a)
	c=json.rfind('"pressure"')
	d=json.index(',',c)
	f=json.index(':',c)
	e=json[f+1:d]	
	e=float(e)
	# write your code 
	return e

def get_wind(json, n=0, t="3:00:00"):
	import datetime
	x=datetime.date.today()
	y=datetime.timedelta(days=n)
	z=x+y
	a=str(str(z)+" "+t)
	b=json.find(a)
	c=json.rfind('"wind"')
	d=json.index(',',c)
	f=json.index(':',c)
	e=json[f+10:d]
	e=float(e)
	# write your code 
	return e

def get_sealevel(json, n=0, t="3:00:00"):
	import datetime
	x=datetime.date.today()
	y=datetime.timedelta(days=n)
	z=x+y
	a=str(str(z)+" "+t)
	b=json.find(a)
	c=json.rfind('"sea_level"')
	d=json.index(',',c)
	f=json.index(':',c)
	e=json[f+1:d]	
	e=float(e)
	# write your code 
	return e
