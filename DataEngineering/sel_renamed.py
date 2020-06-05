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

url='https://www.instagram.com/explore/tags/cars/?hl=en'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument('--disable-notifications')
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--width=1600")
chrome_options.add_argument("--height=600")
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

main_window = driver.current_window_handle

a_tags=driver.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']//a")
div_tags=driver.find_elements_by_xpath("//div[@class='_9AhH0']")
hrefs=[a_tag.get_attribute('href') for a_tag in a_tags]
#parent.appendChild(el);

script = '''
var html = '<div id="div1">text</div>';
html += '<a href="javascript: void(0)" id="a1">bla</a>';
html += '<div id="dvi2">div2<div id="div3">div3</div></div>';

var body_tag=document.getElementsByClassName('Nnq7C weEfm');
body_tag[0].innerHTML = html;
'''
driver.execute_script(script)

driver.execute_script("window.open();")
driver.switch_to.window(driver.window_handles[1])
driver.get(hrefs[0])
driver.close()
driver.switch_to.window(main_window)

# WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//h2[@class='Whs(nw) Ov(h) Tov(e) Fz(19px) tdv2-applet-featurebar:h_Td(u)']")))
# driver.find_element_by_xpath("//h2[@class='Whs(nw) Ov(h) Tov(e) Fz(19px) tdv2-applet-featurebar:h_Td(u)']").click()

link = driver.find_element_by_xpath('//*[@class="tdv2-applet-featurebar Fz(m) C(#fff) Pos(r) D(b) Mb(22px) Whs(nw) Ov(h)"]')
addr = driver.find_element_by_xpath('//*[@class="tdv2-applet-featurebar Fz(m) C(#fff) Pos(r) D(b) Mb(22px) Whs(nw) Ov(h)"]').get_attribute("href")

link.send_keys(Keys.CONTROL + Keys.ENTER)

signin=driver.find_element_by_id('header-signin-link')
signin.send_keys(Keys.CONTROL + Keys.ENTER)
signin.click()

meteo=driver.find_elements_by_xpath("//*[@class='Ai(c) D(f) Jc(sb) Fz(13px) Py(0) Px(0)']")
ActionChains(driver).move_to_element(meteo[0]).context_click().perform()
meteo[0].send_keys(Keys.CONTROL + Keys.ENTER)

iframe=driver.find_element_by_class_name('cke_wysiwyg_frame cke_reset')
driver.switch_to.frame(iframe)

ActionChains(driver).move_to_element(signin).context_click().perform()
ActionChains(driver).move_to_element(signin).context_click().send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

signin.send_keys(Keys.CONTROL + Keys.ENTER)

# open new blank tab
driver.execute_script("window.open();")

# switch to the new window which is second in window_handles array
driver.switch_to.window(driver.window_handles[1])

# open successfully and close
driver.get(addr)
driver.close()

# back to the main window
driver.switch_to.window(main_window)
driver.get(addr)


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


