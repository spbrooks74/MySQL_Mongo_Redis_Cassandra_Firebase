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

# document
employeeCollection = [
                        {"FirstName":"John", "LastName":"Smith", "Age":25},
                        {"FirstName":"Peter", "LastName":"Smith", "Age":26},
                        {"FirstName":"Gabriel", "LastName":"Smith", "Age":28},
                        {"FirstName":"Penny", "LastName":"Lane", "Age":22},
                        {"FirstName":"Eleanor", "LastName":"Rigby", "Age":23},
                        {"FirstName":"Helen", "LastName":"Rose", "Age":23}
                     ]


# insert document
x = mycol.insert_many(employeeCollection)

if "EmployeeDB" in client.list_database_names():

    print("Employee database created!")

print(x.inserted_ids)