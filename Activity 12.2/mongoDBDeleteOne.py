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

#Create Filter
filter = {"LastName":"Rose"}

#Call the Update one method on the collection
mycol.delete_one(filter)

employeeCursor = mycol.find()

for employee in employeeCursor:
    print(employee)