#!/usr/bin/env python3
import sys
import os.path
try:
	args=sys.argv[1:]
	index_c=args.index('-c')
	configfile_c=args[index_c+1]
	index_d=args.index('-d')
	configfile_d=args[index_d+1]
	index_o=args.index('-o')
	configfile_o=args[index_o+1]
except:
	print("Parameter Error")
class Config(object):
	def __init__(self):
		self._config = {}
	def set_config(self,value):
		a= value.split('=')
		self._config[a[0].strip()] = float(a[1].strip(' \n'))
	def get_config(self,value):
		return self._config[value]
test=Config()
def salary(gh,gz,zsgz=None):
	with open(configfile_c) as file1:
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
	if JiShuL<=gz<=JiShuH:
		jiaofei=gz*tax
	elif gz<JishuL:
		jiaofei=JiShuL*tax
	else:
		jiaofei=JiShuH*tax
	if zsgz is None:
		zsgz={}
	ynssde=gz-3500-jiaofei
	if ynssde<=0:
		gsje=format(0,".2f")
		shgz=format(gz-jiaofei,".2f")
	elif 0<ynssde<=1500:
		gsje=format(ynssde,".2f")
		shgz=format(gz-ynssde-jiaofei,".2f")
	elif 1500<ynssde<=4500:
		gsje=format(ynssde*0.10-105,".2f")
		shgz=format(gz-ynssde*0.10+105-jiaofei,".2f")
	elif 4500<ynssde<=9000:
		gsje=format(ynssde*0.20-555,".2f")
		shgz=format(gz-ynssde*0.20+555-jiaofei,".2f")
	elif 9000<ynssde<=35000:
		gsje=format(ynssde*0.25-1005,".2f")
		shgz=format(gz-ynssde*0.25+1005-jiaofei,".2f")
	elif 35000<ynssde<=55000:
		shgz=format(gz-ynssde*0.30+2755-jiaofei,".2f")
	elif 55000<ynssde<=80000:
		gsje=format(ynssde*0.35-5505,".2f")
		shgz=format(gz-ynssde*0.35+5505-jiaofei,".2f")
	elif 80000<ynssde:
		gsje=format(ynssde*0.45-13505,".2f")
		shgz=format(gz-ynssde*0.45+13505-jiaofei,".2f")
	else:
		print("Parameter Error")
	zsgz[gh]=shgz	
	s="{0},{1},{2},{3},{4}".format(gh,gz,format(jiaofei,".2f"),gsje,shgz)
	with open(configfile_o,'a') as file3:
		file3.write(s+'\n')
class UserData(object):
	def __init__(self):
		self._userdata={}
	def calculator(self,value):
		b=value.split(',')
		self._userdata[b[0].strip()] = b[1].strip(' \n')
		gz=int(b[1].strip('\n'))
		gh=int(b[0].strip())
		salary(gh,gz)
	#def dumptofile(self,outputfile): 
try:
	if(len(args)<6):
		raise
	if((index_c%2)or(index_d%2)or(index_o%2)):
		raise
	if(not(os.path.isfile(configfile_c))):
		raise
	if(not(os.path.exists(configfile_c))):
                raise
	if(not(os.path.isfile(configfile_d))):
                raise
	if(not(os.path.exists(configfile_d))):
                 raise
	if(not(os.path.dirname(configfile_o))):
		 raise
	cai=UserData()
	with open(configfile_o,'w') as file4:
		file4.write('')
	with open(configfile_d) as file2:
		lines=file2.readlines()
		for line in lines:
			cai.calculator(line)
			#cai.dumptofile(sys.argv[3])
except:
	print("Parameter Error")
		
		
