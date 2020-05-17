#Project ID: images-5a37d

import pyrebase
import pandas as pd
import csv

config = {"apiKey": "AIzaSyCKQl74vgI56uxAGqVWYwAO_YmR6XoFwGo",  
"authDomain": "images-5a37d.firebaseapp.com",  
"databaseURL": "https://images-5a37d.firebaseio.com",  
"storageBucket": "images-5a37d.appspot.com",  
"serviceAccount": "serviceAccountCredentials.json"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth() 
#authenticate a user
user = auth.sign_in_with_email_and_password("olawal196@gmail.com", "JimmyCarter123")

user['idToken']

#Push image data to database.
def input_image_data(url, tag, data_num):
	print("image_data" + str(data_num))
	data = {"url": url, "url_tag": tag, "data_number": data_num}
	db.child("image_refrences").push(data, user['idToken'])
#open firebase database
db = firebase.database()

#open excel file and push all image data to database. 
with open("images_urls.csv") as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	for data in csvReader:
		data = list(csv.reader(csvDataFile))
		x = 0

		for x in range(len(data)):
			if x % 2 != 0:
				if data[x][0] != "End Data Range":
					print(x)
					url = data[x][0]
					tag = data[x][1]
					data_num = data[x][2]

				input_image_data(url, tag, data_num)

'''
	lana = {"url": ddd3urke4e444, "token": "Figgis Agency"}
	db.child("agents").child("Lana").set(lana, user['idToken'])
'''