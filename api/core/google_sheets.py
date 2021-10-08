import os
from google.oauth2 import service_account
from googleapiclient.discovery import build


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPREADSHEET_ID = '1qD07F9vmxUj4vV_AYsjnzReHmSXR0rxnoe-gClW4az4'
credentials = service_account.Credentials.from_service_account_file(f'{BASE_DIR}\\core\\creeds.json')

service = build('sheets', 'v4', credentials=credentials).spreadsheets().values()
RANGE_GRADES = 'aiogram'

