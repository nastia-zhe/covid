#!/usr/bin/env python

"""
Пример вызова этого скрипта в терминале: python3 (или ./) covid.py -c China 'Russian Federation' Singapore -f some_table.txt
"""

import argparse
from contextlib import redirect_stdout
from lib.tables import (covid_cases_yesterday, get_data)

# Разбор аргументов командной строки

# создаем экземпляр парсера
parser = argparse.ArgumentParser()

# добавляем переменную 'countries', которой присваивается одна/множество стран из ком.строки
parser.add_argument("--countries", '-c', nargs='+', default=['Japan'])

# добавляем переменную 'filename', которой присваиватся имя файла для для записи в него результата выполнения функции (таблицы с данными по ковиду)
parser.add_argument('--filename', '-f')

# парсим аргументы из строки
args = parser.parse_args()

# Получить исходные данные для таблицы
data = get_data()

# Привести данные к табличному виду
result_table = covid_cases_yesterday(args.countries, data)

# Печать итоговой таблицы в файл, если имя файла указано в командной строке (н-р: -f some_table.txt):
if type(args.filename) == str:
    with open(args.filename, 'w') as f:
        with redirect_stdout(f):  # временное перенаправление стандартного вывода в файл
            print(result_table)
else:
    print(result_table)
