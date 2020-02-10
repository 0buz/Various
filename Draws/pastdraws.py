import pandas as pd
import re
from dateutil import parser


def optimise_dtypes(dataframe):
    dates = dataframe['Dates']
    dates = [re.sub('Euro Millions', '', str(date)) for date in dates]
    dates=[parser.parse(date) for date in dates]
    dataframe['Dates'] = pd.to_datetime(dates)

    int_cols = dataframe.iloc[:, 1:]  # get all numerical columns
    for int_col in int_cols:
        dataframe[int_col] = pd.to_numeric(dataframe[int_col], downcast='integer')  # change to optimal integer type
    return dataframe


def all_draws():
    years = range(2004, 2021)

    df = pd.DataFrame()
    for year in years:
        url = f'http://www.lottology.com/europe/euromillions/?do=past-draws-archive&tab=&year={year}&group_num_selector=selected&numbers_selector_mode=add&numbers_selected='
        table = pd.read_html(url)[1]
        df = df.append(table).reset_index(drop=True)
    df = optimise_dtypes(df)
    df.sort_values(by='Dates', ascending=False, inplace=True)
    print(df.info())
    print(df.memory_usage(deep=True))
    return df.to_csv('Draws/PastDraws.csv', index=False, header=True)


def latest_draw():
    dtypes = {
        # 'Dates':'datetime64[ns]',
        '1': 'int8',
        '2': 'int8',
        '3': 'int8',
        '4': 'int8',
        '5': 'int8',
        'Star1': 'int8',
        'Star2': 'int8',
    }
    url = f'http://www.lottology.com/europe/euromillions/?do=past-draws-archive&tab=&year=2020&group_num_selector=selected&numbers_selector_mode=add&numbers_selected='
    table = pd.read_html(url)[1]
    new_row = table.iloc[[0]] # get the latest draw results
    print(new_row)
    new_row = optimise_dtypes(new_row)

    df = pd.read_csv('Draws/PastDraws.csv', dtype=dtypes, parse_dates=['Dates'])

    if not new_row.equals(df.iloc[[0]]):
        df = df.append(new_row).reset_index(drop=True)
        df.sort_values(by='Dates', ascending=False, inplace=True)
        return df.to_csv('Draws/PastDraws.csv', index=False, header=True)
    else:
        return f"Already exists"


x=latest_draw()

import sys

sys.

sys.
# print(df)
# df.sort_values(by='Dates', ascending=False, inplace=True)
# print(df.info())

draws_csv = all_draws()
df.to_csv('PastDraws.csv', index=False, header=False, mode='a')
