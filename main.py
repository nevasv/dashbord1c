import GoogleSheets


spreadsheet_name = 'audit'
sheet_name = 'python'

reader = GoogleSheets.GoogleSheetReader(GoogleSheets.credentials_file)
data = reader.read_sheet(spreadsheet_name, sheet_name)
for row in data:
    print(row)
