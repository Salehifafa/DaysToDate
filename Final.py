from datetime import date
d0 = date.today()
d1 = date(2023,6,8)
delta = d1-d0

print(delta.days)
