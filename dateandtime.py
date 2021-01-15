#python module..
#1)datetime
import datetime
x =datetime.datetime.now()
print(x.date())
print(x.time())
print(x.strftime('%A'))
#creating a date
y =datetime.datetime(2021,1,8).date()
print(y.strftime('%x'))
