import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facerecognition-83933-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "123456":{
        "name":"Shubham Raj",
        "major":"Electronics",
        "starting_year":2020,
        "total_attendance": 34,
        "standing": "G",
        "year":3,
        "last_attendance_time":"2023-3-29 00:54:34"
    },
"321654":{
        "name":"Hassan",
        "major":"Civil",
        "starting_year":2020,
        "total_attendance": 7,
        "standing": "B",
        "year":3,
        "last_attendance_time":"2023-3-29 00:54:34"
    },
"852741":{
        "name":"Emly Blunt",
        "major":"CSE",
        "starting_year":2020,
        "total_attendance": 7,
        "standing": "A",
        "year":3,
        "last_attendance_time":"2023-3-29 00:54:34"
    },
"963852":{
        "name":"Elon Musk",
        "major":"Chemical",
        "starting_year":2020,
        "total_attendance": 10,
        "standing": "G",
        "year":3,
        "last_attendance_time":"2023-3-29 00:54:34"
    },
"654321":{
        "name":"Rushikesh Langde",
        "major":"Electrical Engineering",
        "starting_year":2020,
        "total_attendance": 10,
        "standing": "G",
        "year":3,
        "last_attendance_time":"2023-3-29 00:54:34"

}
}

for key,value in data.items():
    ref.child(key).set(value)