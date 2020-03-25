from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import bs4
browser = webdriver.Chrome()

browser.get("https://www.cosicomodo.it/mercato/torino-hd/pages/tutte-le-categorie")
html = bs4.BeautifulSoup(browser.page_source, "html.parser")
print(html.contents)

titles=html.find('div',class_='store-selector-header')
table = html.find("table",class_="table table-bordered table-hover main_table_countries dataTable no-footer")

for row in table:
    print(row)

url='https://fasttimes.com.au/checkout/onepage/'
driver = webdriver.Chrome()
driver.get(url)
driver.refresh()

driver.find_element_by_id('login:guest').click()
#driver.find_element_by_xpath("//*[@id='shipping-method-buttons-container']/button").send_keys(u'\ue007')
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='onepage-guest-register-button']")))
driver.find_element_by_xpath("//*[@id='onepage-guest-register-button']").click()

driver.find_element_by_xpath('//*[@id="billing-buttons-container"]/button').click()
driver.find_element_by_xpath('//*[@id="shipping-buttons-container"]/button').click()
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='shipping-method-buttons-container']/button")))
driver.find_element_by_xpath("//*[@id='shipping-method-buttons-container']/button").click()
try:
    popup = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i[class*='largeBannerCloser']")))
    popup.click()
except TimeoutException as to:
    print(to)

#driver.find_element_by_css_selector("i.popupCloseIcon").click()
driver.find_element_by_css_selector("a[class*='login']").click()
driver.find_element_by_id('loginFormUser_email').send_keys('myemail')
driver.find_element_by_id('loginForm_password').send_keys('pass')
driver.find_element_by_xpath("//div[@id='loginEmailSigning']//following-sibling::a[@class='newButton orange']").click()

driver.find_element_by_id('flatDatePickerCanvasHol').click()
start_date = driver.find_element_by_id('startDate')
start_date.send_keys(Keys.BACKSPACE*10)
start_date.send_keys(date(2014,1,1).strftime("%d/%m/%Y"))
driver.find_element_by_id('applyBtn').click()
#driver.implicitly_wait(30)

WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'first left bold noWrap')))
driver.find_element_by_css_selector('a.newBtn.LightGray.downloadBlueIcon.js-download-data').click()