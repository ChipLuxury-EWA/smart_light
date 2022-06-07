#I wrote this code in aug2020, I git-push this in june 2022
from ptprotoplus import adc
from time import sleep
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


##settings:##
LS = adc.ADCProbe()
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

##code:##
sheet = client.open("SMARTLIGHT_BM").sheet1
sheet_report = client.open("SMARTLIGHT_BM").get_worksheet(1)

while True:
	if LS.read_value(0) < 100:
		sheet.update_cell(4,4, "cheak report")
		#report_log
		BAD_LIGHT = ["over the sensor", "LED", "9W", "NOT OK", "replace!" ]
		sheet_report.insert_row(BAD_LIGHT,2)
		sleep(3)
		break
	else:
		sheet.update_cell(4,4, "ok")
		sleep(3)
