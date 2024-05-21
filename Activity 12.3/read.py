# pip install redis
import redis

# connect to server
r = redis.Redis(host='localhost', port=6379, db=0)

# read items
Iprint = r.get("Italy")
Fprint = r.get("France")

print(Iprint)
print(Fprint)
