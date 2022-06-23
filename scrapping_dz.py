from bs4 import beautifulSoup
import requests

BASE_URL = 'https://habr.com/ru/all/'
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
TEXT = requests.get(BASE_URL).text

soup = beautifulSoup(TEXT, 'lxml')
for article in soup.find_all('article'):
    head = article.h2.a.text
    preview_text = article.div.div.text
    article_link = article.find('a', class_='post__title_link').get('href')
    public_date = article.find('span', class_='post_time').text

    for word in KEYWORDS:
        if (word.lower() in head.lower()) or (word.lower() in preview_text.lower()):
            print(f'Дата: {public_date} - Заголовок: {head} - Ссылка: {article_link}')
