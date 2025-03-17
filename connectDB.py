import pyodbc
from datetime import datetime
from config import server, database, username, password

# Строка подключения
conn_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=Yes;'

# Подключение к базе данных
conn = pyodbc.connect(conn_str)

# Создание курсора
cursor = conn.cursor()

# Выполнение SQL-запроса
cursor.execute("SELECT * FROM dbo._AccumRg45510")

# Получение результатов

rows = cursor.fetchall()

# Вывод результатов
for row in rows:
    if row:
        for index, value in enumerate(row):
            if isinstance(value, bytes):  # Check if the value is binary
                string = value
                print(f"Column {index} (hex): {string}")

    else:
        print(f"Column {index}: {value}")
    # binary_data = row                             # Предположим, что второй столбец содержит бинарные данные
    # decoded_data = binary_data.hex()              # Декодируем бинарные данные
    # print(decoded_data)
    # print(row)

# Закрытие соединения
cursor.close()
conn.close()
