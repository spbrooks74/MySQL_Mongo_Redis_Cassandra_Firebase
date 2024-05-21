# pip install pymongo
from pymongo import MongoClient
from datetime import datetime
import uuid

# make a connection
client = MongoClient('mongodb://localhost:27017')

# get database
db = client.EmployeeDB

# get collection
mycol = db["employees"]

employee = mycol.find_one({"LastName":"Rigby"})

print(employee)