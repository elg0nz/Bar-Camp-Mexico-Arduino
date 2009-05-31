import feedparser
d = feedparser.parse("http://search.twitter.com/search.atom?q=barcampmexico")

for n in d['items']:
	print unicode(n.author).encode("utf-8")
	print unicode("\t" + n.title).encode("utf-8")