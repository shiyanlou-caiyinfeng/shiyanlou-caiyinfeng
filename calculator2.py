#!/uxr/bin/env python3
import sys
def salary(gh,gz,zsgz=None):
	if zsgz is None:
		zsgz={}
	ynssde=gz-3500-gz*0.165
	if ynssde<=0:
		shgz=format(gz-gz*0.165,".2f")
	elif 0<ynssde<=1500:
		shgz=format(gz-ynssde*0.03-gz*0.165,".2f")
	elif 1500<ynssde<=4500:
		shgz=format(gz-ynssde*0.10+105-gz*0.165,".2f")
	elif 4500<ynssde<=9000:
		shgz=format(gz-ynssde*0.20+555-gz*0.165,".2f")
	elif 9000<ynssde<=35000:
		shgz=format(gz-ynssde*0.25+1005-gz*0.165,".2f")
	elif 35000<ynssde<=55000:
		shgz=format(gz-ynssde*0.30+2755-gz*0.165,".2f")
	elif 55000<ynssde<=80000:
		shgz=format(gz-ynssde*0.35+5505-gz*0.165,".2f")
	elif 80000<ynssde:
		shgz=format(gz-ynssde*0.45+13505-gz*0.165,".2f")
	else:
		print("Parameter Error")
	zsgz[gh]=shgz
	print(zsgz)
try:
	for arg in sys.argv[1:]:	
		gh=int(arg.split(':')[0])
		gz=int(arg.split(':')[1])
		salary(gh,gz)
except  ValueError:
	print("Parameter Error")




