import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Укажите путь к вашему JSON-файлу с учетными данными
json_keyfile = 'my-project-2024-01-08-c21c4138f2ec.json'

# Определите область действия (scope)
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# Авторизация
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile, scope)
client = gspread.authorize(credentials)

# Откройте таблицу по её названию
spreadsheet = client.open("audit")

# Получите список всех листов
sheets = spreadsheet.worksheets()
sheet_names = [sheet.title for sheet in sheets]
my_list = "Python"

if my_list in sheet_names:
    print(f"Лист '{my_list}' найден.")
else:
    print(f"Лист '{my_list}' не найден.")
    # Добавляем новый лист
    spreadsheet.add_worksheet(title=f'{my_list}', rows=100, cols=20)

# Выберите лист по индексу или названию
sheet = spreadsheet.worksheet(f'{my_list}')  # или spreadsheet.worksheet("Лист1")


# Чтение данных
data = sheet.get_all_values()
print(data)

# Запись данных
sheet.update_cell(1, 1, "Новое значение")  # Обновление ячейки A1

# Добавление строки
sheet.append_row(["Новая строка", "Значение 1", "Значение 2"])
