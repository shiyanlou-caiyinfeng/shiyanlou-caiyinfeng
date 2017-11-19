#!/usr/bin/env python3
import sys
class Config(object):
	def __init__(self):
		self._config = {}
	def set_config(self,value):
		a= value.split('=')
		self._config[a[0].strip()] = float(a[1].strip(' \n'))
	def get_config(self,value):
		return self._config[value]
def salary(gh,gz,zsgz=None):
	if JishuL<=gz<=JiShuH:
		jiaofei=gz*tax
	elif gz<JishuL:
		jiaofei=JiShuL*tax
	else:
		jiaofei=JiShuH*tax
	if zsgz is None:
		zsgz={}
	ynssde=gz-3500-jiaofei
	if ynssde<=0:
		shgz=format(gz-jiaofei,".2f")
	elif 0<ynssde<=1500:
		shgz=format(gz-ynssde-jiaofei,".2f")
	elif 1500<ynssde<=4500:
		shgz=format(gz-ynssde*0.10+105-jiaofei,".2f")
	elif 4500<ynssde<=9000:
		shgz=format(gz-ynssde*0.20+555-jiaofei,".2f")
	elif 9000<ynssde<=35000:
		shgz=format(gz-ynssde*0.25+1005-jiaofei,".2f")
	elif 35000<ynssde<=55000:
		shgz=format(gz-ynssde*0.30+2755-jiaofei,".2f")
	elif 55000<ynssde<=80000:
		shgz=format(gz-ynssde*0.35+5505-jiaofei,".2f")
	elif 80000<ynssde:
		shgz=format(gz-ynssde*0.45+13505-jiaofei,".2f")
	else:
		print("Parameter Error")
	zsgz[gh]=shgz
	for gh,shgz in zsgz.items():
		print("{0}:{1}".format(gh,shgz))
class UserData(object):
	def __init__(self):
		self._userdata={}
	def calculator(self,value):
		b=value.split(',')
		self._userdata[b[0].strip()] = b[1].strip(' \n')
		gz=int(b[1].strip('\n'))
		gh=int(b[0].strip())
		salary(gh,gz)
cai=UserData()
test=Config()
with open(sys.argv[1]) as file1:
	lines = file1.readlines()
	for line in lines:
		test.set_config(line)
JiShuL = test.get_config('JiShuL')
JiShuH = test.get_config('JiShuH')
YangLao = test.get_config('YangLao')
YiLiao = test.get_config('YiLiao')
ShiYe = test.get_config('ShiYe')
GongShang = test.get_config('GongShang')
ShengYu = test.get_config('ShengYu')
GongJiJin = test.get_config('GongJiJin')
tax=YangLao+ShiYe+GongShang+ShengYu+YiLiao+GongJiJin
with open(sys.argv[2]) as file2:
	lines=file2.readlines()
	for line in lines:
		cai.calculator(line)
		
		
