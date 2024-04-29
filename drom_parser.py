
import requests
from bs4 import BeautifulSoup

# Задайте URL-адрес сайта
url = 'https://auto.drom.ru/bmw/3-series/'  # замените example.com на URL-адрес нужного сайта

# Отправьте GET-запрос на сайт
response = requests.get(url)

print(response.status_code)

# Проверьте, получен ли успешный ответ
if response.status_code == 200:
    # Используйте BeautifulSoup для парсинга HTML-кода страницы
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Найдите элемент, содержащий число объявлений
    element = soup.find('div', class_='css-1xkq48l eckkbc90')
    
    if element:
        # Извлеките текст из элемента и удалите ненужные символы
        number_of_ads = element.text.split()
        result = ''
        for i in  number_of_ads:
            if i.isdigit() == True:
                result += i
        print("Число объявлений:", result)
    else:
        print("Элемент не найден.")
else:
    print("Ошибка при запросе к сайту.")
