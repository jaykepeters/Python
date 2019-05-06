# LS Domain Categorization
import sys
import requests
from bs4 import BeautifulSoup

domain = str(input("Domain: "))
page = requests.get('https://archive.lightspeedsystems.com/SubmitDomain.php?Domain='+domain)

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
category = soup.find(class_='button button--blue m-right--8').text
print("Category: "+category)
