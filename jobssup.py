from bs4 import BeautifulSoup
import lxml
from misclib import filename
# import html
# html.unescape('Suzy &amp; John')


with open("structure.txt", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, 'lxml')
# driver.close()

selector = '.md_skills'
job_titles = soup.select(selector)

for j in job_titles:
    print(j.get_text())

selector = 'md_recruiter'
agencies = soup.find_all(id=f"{selector}")

for agency in agencies:
    print(agency.get_text())


# job_titles = soup.find_all(class_='jobResultsTitle', limit=10)
# for j in job_titles:
#     print(j.text)

# print(job_titles)


file = filename('raw', 'txt')

with open(file,"w") as f:

