import pandas as pd
import re
from dateutil import parser
import os
import settings

# os.chdir(settings.WORKING_DIR)
# print(os.getcwd())


url = f'{settings.URL}'


def mystring(year=100):
    b_string=settings.URL.format(year=year)
    return b_string

s=mystring(855)

print(f'{mystring(588)}')

var = 42
user_input = "The answer is {variable}"
# in order to get The answer is 42, we can follow this method
print (user_input.format(variable=var))

def optimise_dtypes(dataframe):
    dates = dataframe['Date']
    dates = [re.sub('Euro Millions', '', str(date)) for date in dates]
    dates=[parser.parse(date) for date in dates]
    dataframe['Date'] = pd.to_datetime(dates)

    int_cols = dataframe.iloc[:, 1:]  # get all numerical columns
    for int_col in int_cols:
        dataframe[int_col] = pd.to_numeric(dataframe[int_col], downcast='integer')  # change to optimal integer type
    return dataframe


def all_draws():
    years = range(2004, 2021)

    df = pd.DataFrame()
    for year in years:
        url = f'{settings.URL}'
        table = pd.read_html(url)[1]
        df = df.append(table).reset_index(drop=True)
    df = optimise_dtypes(df)
    df.sort_values(by='Date', ascending=False, inplace=True)
    print(df.info())
    print(df.memory_usage(deep=True))
    return df.to_csv('PastDraws.csv', index=False, header=True)


def latest_draw():
    dtypes = settings.DTYPES
    url = settings.URL
    #url = f'http://www.lottology.com/europe/euromillions/?do=past-draws-archive&tab=&year=2020&group_num_selector=selected&numbers_selector_mode=add&numbers_selected='
    table = pd.read_html(url)[1]
    new_row = table.iloc[[0]] # get the latest draw results
    print(new_row)
    new_row = optimise_dtypes(new_row)

    df = pd.read_csv('PastDraws.csv', dtype=dtypes, parse_dates=['Date'])

    if not new_row.equals(df.iloc[[0]]):
        df = df.append(new_row).reset_index(drop=True)
        df.sort_values(by='Date', ascending=False, inplace=True)
        return df.to_csv('PastDraws.csv', index=False, header=True)
    else:
        return f"Already exists"


def year_draw(year='2020'):
    dtypes = settings.DTYPES
    url = settings.URL
    #url = f'http://www.lottology.com/europe/euromillions/?do=past-draws-archive&tab=&year={year}&group_num_selector=selected&numbers_selector_mode=add&numbers_selected='
    this_year = pd.read_html(url)[1]

    df = pd.read_csv('Draws/PastDraws.csv', dtype=dtypes, parse_dates=['Date'])
    df = optimise_dtypes(df)

    prev_years = df[df['Date'].dt.year != int(year)]

    all_years = prev_years.append(this_year).reset_index(drop=True)
    all_years = optimise_dtypes(all_years)
    all_years.sort_values(by='Date', ascending=False, inplace=True)

    return all_years.to_csv('PastDraws.csv', index=False, header=True)


if __name__ == '__main__':

    if not os.path.isfile('PastDraws.csv'):
        draws_csv = all_draws()
    else:
        draws_csv = year_draw()


# print(df)
# df.sort_values(by='Date', ascending=False, inplace=True)
# print(df.info())


