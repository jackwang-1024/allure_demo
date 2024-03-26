

from datetime import datetime, timedelta

a=datetime.today()
b=a-timedelta(days=30)
c=a-timedelta(weeks=1)

print(a)
print(b)
print(c)