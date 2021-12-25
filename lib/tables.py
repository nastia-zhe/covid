from prettytable import PrettyTable
import requests
import json


def get_data():
    """
    Функция получает данные в формате json, содержащие информацию о ковиде по странам

    """

    res = requests.get('https://api.covid19api.com/summary')
    return json.loads(res.text)


def covid_cases_yesterday(args, data):
    """
    Функция формирует таблицу с количеством заболевших/умерших в странах, указанных в аргументах функции (args).

    Исходные данные (data) для таблицы брать из функции get_data()

    Пример вызова функции: covid_cases_yesterday(['Russian Federation','Japan','Singapore'],get_data())

    """

    # определяет кол-во стран в выгруженном массиве данных:
    country_quantity = len(data["Countries"])

    # создает шаблон таблицы для красивого вывода:
    covid_table = PrettyTable()
    covid_table.field_names = ['Страна', 'Кол-во заболевших', 'Кол-во умерших']
    rows = []

    # ищет данные по странам, указанным в аргументах функции и добавляет их во вложенные списки:
    for n in range(country_quantity):
        for i in args:
            if data["Countries"][n]['Country'] == i:
                rows.append([data["Countries"][n]["Country"], data["Countries"][n]["NewConfirmed"],
                             data["Countries"][n]["NewDeaths"]])

    # добавляет получившиеся вложенные списки в таблицу, выравнивает столбец "Страны" по левому краю, сортирует данные по убыванию кол-ва умерших:
    covid_table.add_rows(rows)
    covid_table.align['Страна'] = 'l'
    covid_table.sortby = 'Кол-во умерших'
    covid_table.reversesort = True

    return covid_table
