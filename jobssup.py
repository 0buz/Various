from bs4 import BeautifulSoup
from lxml import html
from csv import reader, writer, DictReader, DictWriter
from misclib import filename, remove_white_space


remove_white_space("jira20190926x.txt")

with open("jira20190926x.txt", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

html_ids = ['td_jobpositionlink', 'md_skills', 'td_job_type','location','duration','startdate','rate','md_recruiter','md_posted_date']
#html_ids = ['td_jobpositionlink', 'md_skills', 'td_job_type','md_location','md_recruiter','md_posted_date']

jobs=[]
# syntax: {_____:_____ for __ in ____}
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ^^^^^ REMEMBER SYNTAX   ^^^^^^^^^^^^^^^^^^^^


for html_id in html_ids:
    items = soup.find_all(id=f"{html_id}")
    lst=[]
    for item in items:
        lst.append(item.get_text())
    print(html_id,len(lst), lst)
    jobs.insert(html_ids.index(html_id),lst)

rows = list(zip(*jobs))

for item in rows:
    print("\n",item)


file = filename('preprocessed','csv')

with open(file, "w") as f:
    csv_writer = writer(f)
    csv_writer.writerow(html_ids)  # write header
    for row in rows:
        csv_writer.writerow(row)


work on removing Duration, Rate etc!!!!!



