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


job_counter = driver.find_element_by_class_name('job-counter').text
jobs = driver.find_elements_by_class_name('jobItem')
start = 0
end = len(jobs)



with open("structure.txt", "w") as structure:
    while job_counter:
        job_counter = driver.find_element_by_class_name('job-counter').text
        for job in jobs[start:end]:
            driver.execute_script("arguments[0].scrollIntoView(true);", job)
            job.click()
            id = job.get_property('id')
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, id)))
            job_title = job.find_element_by_class_name('jobResultsTitle').text
            xp = f"//*[@title='{job_title}']"
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xp)))
            innerHTML = driver.find_element_by_id('JobDetailPanel').get_property('innerHTML')
            structure.write("\nAdded job " + str(jobs.index(job)) + innerHTML)
            ActionChains(driver).send_keys_to_element(job, Keys.ARROW_DOWN)
            time.sleep(1)
        jobs = driver.find_elements_by_class_name('jobItem')
        start = end
        end = len(jobs)

print("You made it!")

