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


#all_the_way_down=driver.find_element_by_xpath("//*[contains(text(), 'Nearby airports')]")
ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[contains(text(), 'Nearby airports')]")).click().perform()
Nearby airports

//*[@class='core-list-ref']

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


WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'first left bold noWrap')))
driver.find_element_by_css_selector('a.newBtn.LightGray.downloadBlueIcon.js-download-data').click()



wait = WebDriverWait(driver, 20)
driver.get("https://www.ryanair.com/ie/en/cheap-flights/?from=DUB&out-from-date=2020-03-31&out-to-date=2021-03-31&budget=150")
inputBox = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@name='departureInput']//div[@class='disabled-overlay']")))

actionChains = ActionChains(driver)
actionChains.move_to_element(inputBox).click().perform()

list = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='core-list']")))

for element in list:
     print(element.text)