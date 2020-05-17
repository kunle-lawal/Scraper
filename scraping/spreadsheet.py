import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

#gain access to the google sheets
scope = ['https://www.googleapis.com/auth/drive']
cred = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(cred)

#open The google sheets
sheet = client.open('google images').sheet1


row = ["i'm", "updating", "a", "spreadsheet", "from", "Python!"]
index = 3
sheet.insert_row(row, index)