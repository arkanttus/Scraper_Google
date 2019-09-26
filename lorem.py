import requests
from bs4 import BeautifulSoup as Bs

url = "https://www.lipsum.com/"

response = requests.get(url)

soup = Bs(response.text, 'html.parser')


