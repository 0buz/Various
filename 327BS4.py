from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special super-special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
#d = soup.select("#first")
d = soup.select(".special")   #select by class
d = soup.select("[data-example]")   #select by atribute
print(d)

el = soup.select(".special")[0]

print("\n",el)

# get_text usage
for el in soup.select(".special"):
    print("\nEL: ",el.get_text())
    print(el.name) #tag name
    print(el.attrs)   # all attributes for the element


#============  Navigating with BS ========================================

tag = soup.body
print(tag)
data = soup.body.contents[1].contents
print("\n",data)

# Navigate through siblings
data = soup.body.contents[1].next_sibling.next_sibling
print(data)

# navigate parent
data = soup.find(class_="super-special").parent.parent

data = soup.find(id="first").find_next_sibling()
print(data)

data = soup.find(id="first").find_next_sibling().find_next_sibling()
print("\n", data)

data = soup.find(id="first").find_parent()
print("\nlllllla", data)

#===============================================================================

import requests
from bs4 import BeautifulSoup

url='https://hotnews.ro'
r=requests.get(url)

print(f"Your request to {url} came back w/ status code {r.status_code}")
print(r.text)

soup=BeautifulSoup(r.text, 'html.parser')

titles=soup.find_all(class_="article_title")

count=0
with open("00article_titles.txt", "w") as article_file:
    for item in titles:
        if item.a:
            article_file.write("\n"+item.a.text)
        else:
          count+=1
          article_file.write("\nTitle with no a tag:" + item.contents[0])