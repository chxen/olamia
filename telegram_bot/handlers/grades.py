from api.core.google_sheets import service, SPREADSHEET_ID, RANGE_GRADES

grades = {'values': [['email', 'score', 'something']]}
service.append(spreadsheetId=SPREADSHEET_ID,
               range=RANGE_GRADES,
               valueInputOption='USER_ENTERED',
               body=grades).execute()
