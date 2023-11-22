from datetime import datetime, timedelta


now = datetime.now()

T = timedelta(days=1)

print((now - (now + T)).total_seconds())