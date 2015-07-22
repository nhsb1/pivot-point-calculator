import ystockquote
import re
from argparse import ArgumentParser
from datetime import date, timedelta
#.9

def last_weekday(adate):
	adate -= timedelta(days=1)
	while adate.weekday() > 4:
		adate -= timedelta(days=1)
	return adate
	
def y_high(self):
	yesterday_high = newlist[2]
	yesterday_high_float = round(float(re.findall("\d+.\d{1,4}", yesterday_high)[0]), 3)
	return yesterday_high_float

def y_low(self):
	yesterday_low = newlist[3]
	yesterday_low_float = round(float(re.findall("\d+.\d{1,4}", yesterday_low)[0]),3)
	return yesterday_low_float

def y_open(self):
	yesterday_open = newlist[5]
	yesterday_open_float = round(float(re.findall("\d+.\d{1,4}", yesterday_open)[0]),3)
	return yesterday_open_float

def y_close(self):
	yesterday_close = newlist[4]
	yesterday_close_float = round(float(re.findall("\d+.\d{1,4}", yesterday_close)[0]),3)
	return yesterday_close_float

mylastweekday = last_weekday(date.today())
stringdate = mylastweekday.strftime('%Y-%m-%d')

parser = ArgumentParser(description = 'Get Pivots for ticker from ystockquote')
parser.add_argument("-t", "--ticker", dest="ticker", help="ticker for lookup", metavar="FILE")
args = parser.parse_args()

ticker = args.ticker
historicalinfo = ystockquote.get_historical_prices(ticker, stringdate, stringdate)
string_historical_info = str(historicalinfo)
newlist = string_historical_info.split(',')

pivot_high = y_high(newlist)
pivot_low = y_low(newlist)
pivot_open = y_open(newlist)
pivot_close = y_close(newlist)

#print pivot_high, pivot_low, pivot_open, pivot_close

def floor_classic(a1, a2, a3, a4):
	pp = ((pivot_high + pivot_low + pivot_close) / 3)
	r1 = (2 * pp) - pivot_low
	r2 = (pp + pivot_high - pivot_low)
	r3 = (pivot_high + 2*(pp - pivot_low))
	s1 = (2*pp) - pivot_high
	s2 = pp - pivot_high + pivot_low
	s3 = pivot_low - 2*(pivot_high - pp)
	#return pp, r1, r2, r3, s1, s2, s3
	fc_values = [pp, r1, r2, r3, s1, s2, s3]
	return fc_values

def woodie_formula(a1, a2, a3, a4):
	pp = ((pivot_high + pivot_low + 2 * pivot_close)/4)
	r1 = (2*pp) - pivot_low
	r2 = (pp + pivot_high - pivot_low)
	s1 = (2 * pp) - pivot_high
	s2 = pp - pivot_high + pivot_low
	wf_values = [pp, r1, r2, s1, s2]
	return wf_values


myfcvalues = floor_classic(pivot_high, pivot_low, pivot_open, pivot_close)
mywfvalues = woodie_formula(pivot_high, pivot_low, pivot_open, pivot_close)

print "Floor/Classic Pivots for %s, using closing prices from %s" %(ticker, mylastweekday)
print "R3:", myfcvalues[3]
print "R2:", myfcvalues[2]
print "R1:", myfcvalues[1]
print "Pivot Point:", myfcvalues[0]
print "S1:", myfcvalues[4]
print "S2:", myfcvalues[5]
print "S3:", myfcvalues[6]

print "Woodie's Formula Pivots for %s, using closing prices from %s" %(ticker, mylastweekday)
print "R2:", mywfvalues[2]
print "R1:", mywfvalues[1]
print "Pivot Point:", mywfvalues[0]
print "S1:", mywfvalues[3]
print "S2:", mywfvalues[4]










