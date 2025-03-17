import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSheetReader:
    def __init__(self, credentials_file):
        self.credentials_file = credentials_file
        self.scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(self.credentials_file, self.scope)
        self.client = gspread.authorize(self.creds)

    def read_sheet(self, spreadsheet_name, sheet_name):
        spreadsheet = self.client.open(spreadsheet_name)
        sheet = spreadsheet.worksheet(sheet_name)
        return sheet.get_all_values()


credentials_file = 'my-project-2024-01-08-c21c4138f2ec.json'

# Пример использования

# spreadsheet_name = 'Your Spreadsheet Name'
# sheet_name = 'Sheet1'
#
# reader = GoogleSheetReader(credentials_file)
# data = reader.read_sheet(spreadsheet_name, sheet_name)
# for row in data:
#     print(row)
