import re
import time
import logging
import psycopg2
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions as SE
from datetime import date
from bs4 import BeautifulSoup
from csv import writer, reader, DictReader
from datetime import datetime
from dateutil import parser
from selenium.webdriver.common.keys import Keys

url = 'https://www.investing.com/{}/{}-historical-data'

driver = webdriver.Chrome()
driver.get(url)

picker = driver.find_element_by_xpath("//div[@class='float_lang_base_1']")

html=driver.page_source
soup = BeautifulSoup(html, 'lxml')

selector = '.datalet_header_row'
job_descriptions = soup.select(selector)
items = soup.find_all(id='datalet_header_row')

driver.close()
driver.quit()
wait = WebDriverWait(driver, 20)
b = wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr')))
from bs4 import BeautifulSoup

page = "<span>Hello world</span><h1>Nice to see you</h1><span>no</span><span>Hello babe</span>"

soup = BeautifulSoup(page)

while len(soup.find_all('span')) > 0:
    soup.span.extract()
print(soup)


import pandas as pd
from random import randint
import time

# data (it takes some time to create [less than 1 minute in my computer])
data1   = [[[[randint(0, 100) for i in range(randint(1, 2))] for i in range(randint(1, 3))] for i in range(500)] for i in range(100)]
data2   = pd.DataFrame(
    [
        (i1, i2, i3, i4, x4)
        for (i1, x1) in enumerate(data1)
        for (i2, x2) in enumerate(x1)
        for (i3, x3) in enumerate(x2)
        for (i4, x4) in enumerate(x3)
    ],
    columns = ['i1', 'i2', 'i3', 'i4', 'x']
)
data2.drop(['i3', 'i4'], axis=1, inplace = True)
df   = data2.set_index(['i1', 'i2']).sort_index()

df.rolling
## conflicting part of the code ##
start = time.process_time()
df['rolling'] = df.groupby('i2')['x'].rolling(3).apply(lambda x: x[-3]*0.1+x[-2]*0.9).reset_index(level=0, drop=True).reindex(df.index)
print("Rolling time:", time.process_time() - start)



import time
from math import sqrt

start = time.process_time()
prime_numbers=[2]

for k in range(5,101):
    for i in range(2, int(sqrt(k))+2):
        j=i
        if k%i == 0:
            break
        else:
            j+=1
        if j==int(sqrt(k))+2:
            prime_numbers.append(k)

print(prime_numbers