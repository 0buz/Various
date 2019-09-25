import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

url = 'https://www.jobserve.com'

driver = webdriver.Chrome()
driver.get(url)

driver.find_element_by_id('selAge').click()
select = Select(driver.find_element_by_id('selAge'))
select.select_by_index(7)

# Industry
driver.find_element_by_class_name('ui-dropdownchecklist-text').click()
checked = driver.find_element_by_id('ddcl-selInd-i0').get_property('checked')
if checked:
    driver.find_element_by_id('ddcl-selInd-i0').click()

# ITC
checked = driver.find_element_by_id('ddcl-selInd-i14').get_property('checked')
if not checked:
    driver.find_element_by_id('ddcl-selInd-i14').click()

# Keyword
driver.find_element_by_id('txtKey').send_keys("jira")

# Search
driver.find_element_by_css_selector('.searchbcontain').click()

# print(driver.find_element_by_id('td_jobpositionlink').get_attribute('title'))
# driver.refresh()


#
# ActionChains(driver).move_to_element(driver.find_element_by_css_selector('.nextJobs')).perform()
#
# jobs = driver.find_elements_by_class_name('jobItem')
# jobs[len(jobs) - 1].click()

# while True:
#     if end_of_results == "Loading":
#         ActionChains(driver).move_to_element(driver.find_element_by_css_selector('.nextJobs')).perform()
#        # ActionChains(driver).send_keys_to_element(driver.)
#         WebDriverWait(driver, 3)
#         end_of_results = driver.find_element_by_class_name("nextJobs").text
#         jobs = driver.find_elements_by_class_name('jobItem')
#         #WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By., 'someid')))
#         time.sleep(3)
#         jobs[len(jobs) - 3].click()
#     else:
#         break

#print(len(jobs))

end_of_results = "Loading"

jobs = driver.find_elements_by_class_name('jobItem')
start = 0
end = len(jobs)
job_counter = driver.find_element_by_class_name('job-counter').text

while job_counter:
    job_counter = driver.find_element_by_class_name('job-counter').text
    for job in jobs[start:end]:
        driver.execute_script("arguments[0].scrollIntoView(true);", job)
        job.click()
        print(jobs.index(job))
        id = job.get_property('id')
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, id)))
        ActionChains(driver).send_keys_to_element(job, Keys.ARROW_DOWN)
        time.sleep(1)
    jobs = driver.find_elements_by_class_name('jobItem')
    start = end
    end = len(jobs)

print("You made it!")

count = 0
jobs = driver.find_elements_by_class_name('jobItem')
for job in jobs:
    driver.execute_script("arguments[0].scrollIntoView(true);", job)
    job.click()
    id = job.get_property('id')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, id)))
    # job_title = job.find_element_by_class_name('jobResultsTitle').text
    # xp = f"//*a[@title='{job_title}']"
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xp)))
    # innerHTML = driver.find_element_by_id('JobDetailPanel').get_property('innerHTML')
    ActionChains(driver).send_keys_to_element(job, Keys.ARROW_DOWN)
    time.sleep(2)
    count +=1

with open("structure.txt", "w") as structure:
    for job in jobs:
        job.click()
        job_title = job.find_element_by_class_name('jobResultsTitle').text
        xp = f"//*[@title='{job_title}']"
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xp)))
        innerHTML = driver.find_element_by_id('JobDetailPanel').get_property('innerHTML')
        structure.write("\nAdded job " + str(jobs.index(job)) + innerHTML)

#   # ActionChains(driver).send_keys_to_element(driver.)
    #jobs[len(jobs) - 3].click()
    #jobs[len(jobs) - 3].send_keys(Keys.ARROW_DOWN)
# index = 0
# #with open("structure.txt", "a") as structure:
# while not end_of_results:
#          job = driver.find_element_by_class_name('jobItem')
#          job.click()
#          job_title = job.find_element_by_class_name('jobResultsTitle').text
#          xp = f"//*[@title='{job_title}']"
#          WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xp)))
#          innerHTML = driver.find_element_by_id('JobDetailPanel').get_property('innerHTML')
#          job.send_keys(Keys.ARROW_DOWN)
#          index += 1
#          #structure.write("\nAdded job " + str(index) + innerHTML)


#:


scroller.send_keys(Keys, )

# soup = BeautifulSoup(scroll_content, 'html.parser')
#
# job_items = soup.find_all(class_='jobItem')
# next_set = soup.find_all_next(class_='jobItem')
#
# for job in job_items:
#     print('\nThis is the job title ' + str(job_items.index(job)) + ":\n", job.get_text())
#     driver


# title = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,'td_jobpositionlink')))


html = driver.page_source
# print(html)

# description = driver.find_element_by_id('JobDetailContainer').text


soup = BeautifulSoup(html, 'html.parser')
# driver.close()

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

# print(job_titles)
