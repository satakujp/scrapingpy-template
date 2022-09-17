import requests
import urllib.parse

from bs4 import BeautifulSoup

# HTMLソースコードを取得してBeautifulSoupで解析する。　
vgm_url = 'https://satakujp.z11.web.core.windows.net/'
html_text = requests.get(vgm_url).content
soup = BeautifulSoup(html_text, 'html.parser')

# ページのタイトルを取得して表示する。
print("ページのタイトルを取得して表示する。")
print(soup.select_one("head title").get_text())

# select_oneは最初に取れた要素を返す。
print("\nselect_oneは最初にとれた要素を返す。")
print(soup.select_one("div > h2").get_text())

# selectはすべての要素を返す。
print("\nselectはすべての要素を返す。")
for i,ele in enumerate(soup.select("div > h2")):
  print("{0} : {1}".format(i, ele.get_text()))

# 属性値はgetメソッドで取得する。
print("\n属性値はgetメソッドで取得する。")
print(soup.select_one("div > h2").get("class"))

# contentsで子要素(<td>)を取得できる。
print("\ncontentsで子要素をすべて取得できる。")
tr = soup.select("div > table > tr")
for ele in tr[1]:
  if ele.name:
    print("{0} : {1}".format(ele.name, ele.get_text()))

# n番目の子要素を取得する。
print("\nn番目の子要素を取得する。")
tr = soup.select("div > table > tr")
print(tr[1].contents[3].get_text())
print(soup.select_one("div > table > tr:nth-child(2) > td:nth-child(2)").get_text())
