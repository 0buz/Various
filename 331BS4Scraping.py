import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

url='https://www.jobserve.com'


driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(2)

driver.find_element_by_id('selAge').click()
select = Select(driver.find_element_by_id('selAge'))
select.select_by_index(7)

driver.find_element_by_class_name('ui-dropdownchecklist-text').click()


checked = driver.find_element_by_id('ddcl-selInd-i0').get_property('checked')
if checked:
    driver.find_element_by_id('ddcl-selInd-i0').click()


checked = driver.find_element_by_id('ddcl-selInd-i14').get_property('checked')
if not checked:
    driver.find_element_by_id('ddcl-selInd-i14').click()

driver.find_element_by_css_selector('.searchbcontain').click()   # Search


driver.refresh()
driver.find_element_by_css_selector('.summary-content').find_element_by_css_selector('.dragger.ui-draggable').click()
#By.XPATH, '//*[@id="nextJobs"]')
end_of_results = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME,'nextJobs')))
driver.execute_script("return arguments[0].scrollIntoView(true);", end_of_results)


# URL = "https://silpo.ua/offers/?categoryId=13"
# driver = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe')
# driver.get(URL)
# copyright = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.copyrights")))
# driver.execute_script("return arguments[0].scrollIntoView(true);", copyright)




html = driver.page_source
print(html)

description = driver.find_element_by_id('JobDetailContainer').text


#print(f"Your request to {url} came back w/ status code {r.status_code}")

#soup = BeautifulSoup(r.text, 'lxml')
soup = BeautifulSoup(html, 'html.parser')
#driver.close()

selector = '.jobItem'
job_titles = soup.select(selector)

for j in job_titles:
    print(j.get_text())


selector = '.md_skills'
job_descriptions = soup.select(selector)

for d in job_descriptions:
    print(d.get_text())

# job_titles = soup.find_all(class_='jobResultsTitle', limit=10)
# for j in job_titles:
#     print(j.text)

#print(job_titles)



