import datetime
import pytz


#naive
print("Naive")
print()
var=datetime.date(2019,4,5)
print(var)
var=datetime.date.today()
print(var)
var=datetime.timedelta(days=7)
print(var)


var=datetime.time(1,2,3)
print(var)


var=datetime.datetime(2019,4,5,6,7,8)
print(var)
var=datetime.datetime.today()
print(var)
var=datetime.datetime.now()
print(var)


t=pytz.timezone('US/Mountain')
var1=t.localize(var)
var2=var.astimezone(pytz.timezone('US/Mountain'))
print(var2)

print()





#aware
print("Aware")
print()
var=datetime.datetime(2019,4,5,6,7,8,tzinfo=pytz.UTC)
print(var)
var=datetime.datetime.now(tz=pytz.UTC)
print(var)
var1=var.astimezone(pytz.timezone('US/Mountain'))
print(var1)

#for i in pytz.all_timezones:
#    print(i)
print()
print("string-datetime")

#string-datetime
str="December 12,2019"
dt=datetime.datetime.strptime(str,'%B %d,%Y')
print(dt)
print(dt.strftime('%B %d,%Y'))
