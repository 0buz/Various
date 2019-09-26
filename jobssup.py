from bs4 import BeautifulSoup
import lxml
from misclib import filename
# import html
# html.unescape('Suzy &amp; John')


with open("jira20190926.txt", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, 'lxml')

#html_ids = ['td_jobpositionlink', 'md_skills', 'td_job_type','md_location','md_start_date','md_rate','md_recruiter','md_posted_date']
html_ids = ['td_jobpositionlink', 'md_skills', 'td_job_type','md_location','md_recruiter','md_posted_date']

jobs=[]
# syntax: {_____:_____ for __ in ____}
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ^^^^^ REMEMBER SYNTAX   ^^^^^^^^^^^^^^^^^^^^


for html_id in html_ids:
    items = soup.find_all(id=f"{html_id}")
    lst=[]
    for item in items:
        lst.append(item.get_text())
    print(html_id,len(lst))
    jobs.insert(html_ids.index(html_id),lst)


for job in jobs:
    print(list(zip(job)))

print(len(jobs))



print(zip(jobs))

tp = zip(jobs)

for item in list(tp):
    print("\n",item)

for job in jobs:


d = {k : v for k in html_ids}
file = filename('raw', 'csv')



