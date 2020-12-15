import requests as req
from bs4 import BeautifulSoup as BS
import zipfile


r = req.get(r'https://www.learndatasci.com/tutorials/ultimate-guide-web-scraping-w-python-requests-and-beautifulsoup/')

print(r.content[:100])

soup = BS(r.content, 'html.parser')
