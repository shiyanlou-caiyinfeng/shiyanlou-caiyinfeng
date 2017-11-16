#!/uxr/bin/env python3
import sys
try:
	gz=int(sys.argv[1])
except  ValueError:
	print("Parameter Error")
ynssde=gz-3500
if 0<ynssde<=1500:
	print(format(ynssde*0.03,".2f"))
elif 1500<ynssde<=4500:
	print(format(ynssde*0.10-105,".2f"))
elif 4500<ynssde<=9000:
	print(format(ynssde*0.20-555,".2f"))
elif 9000<ynssde<=35000:
	print(format(ynssde*0.25-1005,".2f"))
elif 35000<ynssde<=55000:
	print(format(ynssde*0.30-2755,".2f"))
elif 55000<ynssde<=80000:
	print(format(ynssde*0.35-5505,".2f"))
elif 80000<ynssde:
	print(format(ynssde*0.45-13505,".2f"))
else:
	print("Parameter Error")



