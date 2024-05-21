# firebase - backend as a service, BaaS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('c:/Users/spbro/OneDrive/Desktop/Sample/Activity 12.5/serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://activity12-5-be281-default-rtdb.firebaseio.com/'
})



# save data
ref = db.reference('py/')
users_ref = ref.child('teams')
users_ref.set({
    'PennState': {
        'city': 'State College',
        'rank': '10'
    },
    'Alabama': {
        'city': 'Tuscaloosa',
        'rank': '15'
    }
})

# update data
hopper_ref = users_ref.child('Alabama')
hopper_ref.update({
    'coach': 'Nick Saban'
})

# read data
handle = db.reference('py/teams/PennState')

# Read the data at the posts reference (this is a blocking operation)
print(ref.get())