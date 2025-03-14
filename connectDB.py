import pyodbc
from config import server, database, username, password

# Строка подключения
conn_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=Yes;'

# Подключение к базе данных
conn = pyodbc.connect(conn_str)

# Создание курсора
cursor = conn.cursor()

# Выполнение SQL-запроса
cursor.execute("SELECT * FROM v8users")

# Получение результатов
rows = cursor.fetchall()

# Вывод результатов
for row in rows:
    print(row)

# Закрытие соединения
cursor.close()
conn.close()