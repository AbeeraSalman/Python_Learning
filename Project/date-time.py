import datetime

today=datetime.date.today()
print(today.year)
print(today.month)
print(today.day)


birthday=datetime.date(2001,11,11)
print(birthday)


curr_date=datetime.datetime.now().time()
print(curr_date)

now = datetime.datetime.now()

print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.minute)
print(now.hour)
print(now.second)



future_date = today + datetime.timedelta(days=5)

print(future_date)