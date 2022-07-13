from bs4 import BeautifulSoup

with open("blank/index.html") as file:
    src = file.read()
#print(src)

soup = BeautifulSoup(src, "lxml")

title = soup.title
print(title)
print(title.text)

