import feedparser
import time
import codecs
import sys
import serial

streamWriter = codecs.lookup('utf-8')[-1]
sys.stdout = streamWriter(sys.stdout)

ser = serial.Serial('/dev/tty.usbserial-A60049lS', 115200)
ser.write("Twittduino 0.1 FTW")
time.sleep(2)
ser.write("~")

while 1:
	try:
		d = feedparser.parse("http://search.twitter.com/search.atom?q=barcampmexico")
	except IOError, e:
		if hasattr(e, 'reason'):
			print 'Reason : '
			print e.reason
	else:  
		for n in d['items']:
			#print unicode(n.author).encode("utf-8")
			#print unicode("\t" + n.title).encode("utf-8")
			output = n.author + "\t" + n.title
			ser.write('~')
			ser.write(output.encode('ascii','ignore'))
			time.sleep(10)
			print output
	time.sleep(60) #update every 60 (1 min)
