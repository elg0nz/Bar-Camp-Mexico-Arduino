from urllib import urlencode
import base64
import urllib2
import serial
import getpass
import time

class TwitObj(object):
	''' Handles the connection with the twitter REST api '''
	def __init__(self, user, passw):
		self.base64string = base64.encodestring('%s:%s' % (user,passw))[:-1] 
		self.req = urllib2.Request('http://twitter.com/statuses/update.xml')
		self.req.add_header("Authorization", "Basic %s" % self.base64string)

	def send(self, message):
		params = urlencode({'status':message})
		try:
			handle = urllib2.urlopen(self.req, params)
		except IOError, e:
			if hasattr(e, 'reason'):
				print 'Reason : '
				print e.reason
		else:
				string = handle.read()      
				#print string
				print 'Msg Sent:' + message

def getAverage(serial, samples):
	L = list()
	val =0
	for i in range(1,samples):
		val = serial.readline()
		if val !="":
			try:
				val = int(val)
			except:
				val = 0
		L.append(val)
	average = sum(L)/len(L)
	return average

ser = serial.Serial('/dev/tty.usbserial-A60049lS', 9600)
user = raw_input('Twitter Username: ')
passw = getpass.getpass('Twitter Password (hidden): ')
twitCon = TwitObj(user,passw)
message = raw_input('Message to twitt when you wake up: ')

ser.write('H')
time.sleep(0.250)

getpass.getpass('Calibration: Keep ON your lights, press enter when you are ready')
maxVal = getAverage(ser, 82)
print 'Max value:' + str(maxVal)

getpass.getpass('Calibration: Turn OFF your lights, press enter when you are ready')
lowVal = getAverage(ser, 52)
print 'Min value:' + str(lowVal)

medValue = (maxVal + lowVal) /2
print 'medValue:' + str(medValue)
ser.write('l')
time.sleep(0.250)

print 'Go to bed now. Next time you turn on the light the message  "' + message + '" will be twitted'
print 'The led on the arduino board will lit on when its done'

n =0

while n < medValue:
	n = getAverage(ser, 120)
	print str(n) + '\r'
print message
twitCon.send(message)
ser.write('H')
time.sleep(0.250)
ser.write('H')
time.sleep(0.250)