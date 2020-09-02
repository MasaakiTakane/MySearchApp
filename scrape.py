import bs4 as bs
from urllib.request import urlopen as uReq

name = input("Enter the name: ")
rname = name.replace(" ","_")

url = "https://en.wikipedia.org/wiki/" + rname

page_html = uReq(url).read()

soup = bs.BeautifulSoup(page_html, "html.parser")
table = soup.find("table")

for info in table.findAll("tr"):
  print(" : ".join([info.text]))


