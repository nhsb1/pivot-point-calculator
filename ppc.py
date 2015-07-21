import ystockquote
import re
from argparse import ArgumentParser


from datetime import date, timedelta

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

print pivot_high, pivot_low, pivot_open, pivot_close

pp = ((pivot_high + pivot_low + pivot_close) / 3)
r1 = (2 * pp) - pivot_low
r2 = (pp + pivot_high - pivot_low)
r3 = (pivot_high + 2*(pp - pivot_low))
s1 = (2*pp) - pivot_high
s2 = pp - pivot_high + pivot_low
s3 = pivot_low - 2*(pivot_high - pp)
print r1, r2, r3
print s1, s2, s3
print pp




