"""
An auto logger to automatically log into web page
"""
import requests
from bs4 import BeautifulSoup

HACKERRANK_URL = 'https://www.hackerrank.com/login'

payload = {
    "login": "yashLadha",
    "password": "iamstudious10",
    "authenticity_token": "qgEIT8KJZ0u5hzHSDCklUULfk58hZiPT/xOUZ8P34dk="
}

session_requests = requests.session()
result = session_requests.get(HACKERRANK_URL)
result = session_requests.post(
    HACKERRANK_URL,
    data=payload,
    headers=dict(referer=HACKERRANK_URL)
)
result = session_requests.get('https://www.hackerrank.com/domains',
                              headers=dict(referer='https://www.hackerrank.com/domains'))
soup = BeautifulSoup(result.content, 'html.parser')
print(soup.prettify())
