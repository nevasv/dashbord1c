import win32com.client
import pandas as pd
from config import Srvr, Ref, Pwd, Usr


def connect_to_1c():
    try:

        V83_CONN_STRING = f'Srvr={Srvr};Ref={Ref};Usr={Usr};Pwd={Pwd}'
        # Создаем объект V8.ComConnector
        connector = win32com.client.Dispatch("V83.COMConnector")

        # Подключаемся к 1С
        connection = connector.Connect(V83_CONN_STRING)

        # Проверяем, успешно ли подключились
        if connection is None:
            print("Не удалось подключиться к 1С!")
            return

        # Создаем запрос к базе 1С
        query = connection.NewObject("Query")
        query.Text = "ВЫБРАТЬ * ИЗ Справочник.Номенклатура"

        # Выполняем запрос
        result = query.Execute().Choose()

        # Создаем список для хранения данных
        data = []

        # Собираем заголовки столбцов
        columns = [result.Columns(i).Name for i in range(result.Columns.Count)]

        # Собираем данные из строк
        for i in range(result.Rows.Count):
            row = [result.Rows(i).Get(j) for j in range(result.Columns.Count)]
            data.append(row)

        # Создаем DataFrame из данных
        df = pd.DataFrame(data, columns=columns)

        # Выводим DataFrame в Excel
        df.to_excel("output.xlsx", index=False)

        print("Данные успешно загружены в output.xlsx!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        # Закрываем соединение
        if 'result' in locals():
            del result
        if 'query' in locals():
            del query
        if 'connection' in locals():
            del connection
        if 'connector' in locals():
            del connector


# Вызов функции
connect_to_1c()
