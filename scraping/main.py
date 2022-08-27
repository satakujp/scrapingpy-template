import requests
import urllib.parse

from bs4 import BeautifulSoup


vgm_url = 'https://www.vgmusic.com/music/console/nintendo/nes/'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')

print(soup.select_one("head title").get_text())
