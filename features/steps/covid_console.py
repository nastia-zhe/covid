from behave import *
import subprocess


@when('we run \'covid.py\' for the "{country}" and specify filename "{file}"')
def step_impl(context, country, file):
    subprocess.run(f'/home/nazhe/PycharmProjects/covid/covid.py -c {country} -f {file}', shell=True, encoding='utf-8')


@then('the table is written into a "{file}"')
def step_impl(context, file):
    with open(file, 'r') as f:
        context.covid_table = f.read()
        assert bool(context.covid_table)

        print('Table from the file:', '\n', context.covid_table)


@step("table is not empty (contains more than 4 rows)")
def step_impl(context):
    lines_number = context.covid_table.count('\n')
    assert lines_number > 4, f'Table is empty and contains {lines_number + 1} rows'
    print(f'Table contains {lines_number} rows')


@step('table contains "{country}"')
def step_impl(context, country):
    # удаляем комбинации кавычек если в переменной country есть "сложные страны" (н-р: "Russian Federation" "United States of America")
    quotes_to_delete = ['" "', '" ', ' "']
    country_without_quotes = country
    for quotes in quotes_to_delete:
        if quotes in country:
            country_without_quotes = country_without_quotes.replace(quotes, ' ')

    elements_in_country = country_without_quotes.strip('\"').split()  # сплитим строку на отд.слова в составе стран

    elements_in_table = 0

    for element in elements_in_country:
        if element in context.covid_table:
            elements_in_table += 1

    if elements_in_table == len(elements_in_country):
        print(f'{country} is in the table')
    else:
        raise ValueError(f'NO!!! {country} in the table')


@when('we run \'covid.py\' for the "{country}"')
def step_impl(context, country):
    context.covid_table = subprocess.run(f'/home/nazhe/PycharmProjects/covid/covid.py -c {country}', shell=True,
                                         stdout=subprocess.PIPE, encoding='utf-8').stdout


@then("we get the table on the screen")
def step_impl(context):
    print(context.covid_table)
