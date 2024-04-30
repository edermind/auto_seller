

import requests
from bs4 import BeautifulSoup

async def parse_drom(link):
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        element = soup.find('div', class_='css-1xkq48l eckkbc90')
        if element:
            number_of_ads = element.text.split()
            result = ''.join(filter(str.isdigit, number_of_ads))
            return result
    return "Ошибка при парсинге"
