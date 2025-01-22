import time

b = int (time.time())
print(b)
totalMinutes = b//60
print(totalMinutes)
print(type(totalMinutes))
totalDays = totalMinutes//(24*60)
print(totalDays)
print(type(totalDays))
totalYears = totalDays//365
print(totalYears)
print(type(totalYears))