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

url = 'http://www.cssdesk.com/kGm7S'

driver = webdriver.Chrome()
driver.get(url)

iframe=driver.switch_to.frame('frame')
el = driver.find_element_by_id("was-returns-reconciliation-report-start-date")
el.clear()
el.send_keys("2020-02-01")
el.send_keys(Keys.ENTER)  # Separately

# Tried without clear as well
# no error but the date didn't change in the browser

driver.execute_script("document.getElementById('was-returns-reconciliation-report-start-date').value = '2020-01-05'")

WebDriverWait(driver, 20).until(driver.find_element_by_class_name('job-counter').text.strip() != '')

#  Extract the total number of parcels from string e.g. "1 of 24"
string=driver.find_element_by_xpath("//input[@name='DTLNavigator$txtFromTo']").get_attribute('value')
#  split string in separate words; last word i.e. [-1] is the total number of records e.g. "24"
total_records=string.split(' ')[-1]

for record in range(int(total_records)):
    # parse record here
    driver.find_element_by_xpath("//input[@name='DTLNavigator$imageNext']").click()
    time.sleep(0.5) # be nice to your source and don't load their server with numerous quick requests

html=driver.page_source
soup = BeautifulSoup(html, 'lxml')

selector = '.datalet_header_row'
job_descriptions = soup.select(selector)
items = soup.find_all(id='datalet_header_row')

driver.close()
driver.quit()


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

import re
re.findall(r"[\w']+|[.,!?;]", "Hello, I'm a string!")
['Hello', ',', "I'm", 'a', 'string', '!']

import itertools as it

l = it.combinations('ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ', 3) #List of every 3-letter combination
d = it.combinations('0123456789', 4)                    #List of every 4-digit combination
print(list(l))
print(list(d))

l=list(l)
joinl = [''.join(t) for t in l]
print(list(joinl))




