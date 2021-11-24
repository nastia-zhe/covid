#!/usr/bin/env python

from lib.initial_data import get_data
from lib.tables import covid_cases_yesterday
import argparse

#Получение стран (для которых нужно составить таблицу) из командной строки:
parser = argparse.ArgumentParser() #создаем экземпляр парсера

parser.add_argument("--countries", '-c',nargs='+', default=['Japan']) #добавляем переменную 'countries', которой присваивается множество стран из ком.строки

args = parser.parse_args() #парсим аргументы из строки

#------------------------------------------------------------------------

data = get_data()
#------------------------------------------------------------------------

#в командной строке нужно написать: python3 covid.py --countries China Japan Singapore
#<python3> <назв.скрипта> <назв.переменной> <страны перечислить>

covid_cases_yesterday(args.countries,data=data)
