import pandas as pd

years = [2019, 2020]

df = pd.DataFrame()
for year in years:
    url = f'http://www.lottology.com/europe/euromillions/?do=past-draws-archive&tab=&year={year}&group_num_selector=selected&numbers_selector_mode=add&numbers_selected='
    table = pd.read_html(url)[1]
    win_nums = table.loc[:,1].str.split(" ",expand=True).reset_index(drop=True)
    dates = pd.DataFrame(list(table.loc[:,0]), columns=['date'])

    table = dates.merge(win_nums, left_index=True, right_index=True)

    df = df.append(table, sort=True).reset_index(drop=True)

df['date']= pd.to_datetime(df['date'])
df = df.sort_values('date').reset_index(drop=True)

df.to_csv('0file.csv', index=False, header=False)


url = f'http://www.lottology.com/europe/euromillions/?do=past-draws-archive&tab=&year=2020&group_num_selector=selected&numbers_selector_mode=add&numbers_selected='
table = pd.read_html(url)[1]