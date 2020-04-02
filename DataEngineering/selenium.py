from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import bs4

path = "/home/quentin/bin/chromedriver"
base_url = "https://www.investing.com/economic-calendar/"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument('--disable-notifications')
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)
driver.get(base_url)

WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='pdynamicbutton']//a[@class='call']")))
driver.find_element_by_xpath("//div[@class='pdynamicbutton']//a[@class='call']").click()


url='https://www.ryanair.com/ie/en/cheap-flights/?from=DUB&out-from-date=2020-03-31&out-to-date=2021-03-31&budget=150'
driver = webdriver.Chrome()

driver.get(url)

WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//*[@icon-id='glyphs.earth']")))
driver.find_element_by_xpath("//*[@icon-id='glyphs.earth']").click()

WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CLASS_NAME,"airports")))
airports_root=driver.find_element_by_class_name('airports')
airport_tags=airports_root.find_elements_by_tag_name('text')

airport_names=[]
for airport in airport_tags:
    airport_names.append(airport.get_property('innerHTML'))

#From
city_from = input('From which city? ')
departure=driver.find_element_by_xpath("//div[@name='departureInput']//div[@class='disabled-wrap']/input")
driver.execute_script("arguments[0].value = '"+ city_from + "';", departure)

# To
city_to = input('From which city? ')
destination=driver.find_element_by_xpath("//div[@name='destinationInput']//div[@class='disabled-wrap']/input")
driver.execute_script("arguments[0].value = '"+ city_to + "';", destination)
# city_to.clear()
# city_to.send_keys("Tallin")


input_fields[0].find_element_by_tag_name('input').send_keys("Tallin")
input_fields[1].find_element_by_tag_name('input').send_keys("Aarhus")
input_fields[2].find_elements_by_class_name('options')

driver.switch_to.frame('formFaresSearch')
city_to = driver.find_element_by_xpath("//div[@name='departureInput']//div[@class='disabled-overlay']")
city_from.click()


