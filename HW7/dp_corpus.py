import re
import csv
import time

import requests
from bs4 import BeautifulSoup as bs


month2digit = {
    'января': 1,
    'февраля': 2,
    'марта': 3,
    'апреля': 4,
    'мая': 5,
    'июня': 6,
    'июля': 7,
    'августа': 8,
    'сентября': 9,
    'октября': 10,
    'ноября': 11,
    'декабря': 12,
}

def get_rubrics():
    # получаем список всех рубрик, которые есть на сайте
    main_page = requests.get('https://www.dp.ru/')
    main_page_soup = bs(main_page.content)
    rubrics = main_page_soup.find_all('h3', class_="menu__heading menu__heading_small")
    rubrics = [rubric.text.strip() for rubric in rubrics]
    
    # последние 3 элемента не совсем рубрики
    return rubrics[:-3]

def get_all_links(rubrics, date):
    # получаем ссылки на все статьи до определенного месяуа, которые находятся на странице рубрики 
    # на вход нужен список рубрик
    all_links = []
    
    for rubric in rubrics:
        for i in range(1,100):
            rubric_page = requests.get(f'https://www.dp.ru/tag/{rubric}?page={i}')
            rubric_page_soup = bs(rubric_page.content)
            links = rubric_page_soup.find_all('a', class_="b-inline-article__preview")
            links = [link['href'] for link in links]
            all_links.extend(links)
            # если в ссылке есть месяц, который мы указали, то прекращаем поиск
            if any(re.search(f'a/{date}', link) for link in links):
                break
    # множество тк ссылки очень часто повторяются 
    return set(all_links)

def corpus_ro_csv(links, name_csv):
    csv_file = open(name_csv, 'w', encoding='utf-8')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['link', 'headline', 'article', 'date', 'tag'])

    for link in links:
        dp = requests.get(f'https://www.dp.ru{link}')
        soup_dp = bs(dp.content)
        # получаем тэг
        tag = soup_dp.find('a', class_="b-article-tag").text.strip()
        # получаем дату и меняем представление месяца (так легче воспринимается в таблице)
        date = soup_dp.find('span', class_="b-article-header-signature__date").text
        date = date[:-7]
        month = date.split()[1]
        date = date.replace(month, str(month2digit[month]))
        # получаем текст статьи 
        text = soup_dp.find('div', class_="b-article-stretched b-article-stretched_old-image-container b-article-stretched_main-preview")
        text = soup_dp.find_all('p')
        text = ' '.join([x.text for x in text])
        # получаем заголовки статьи 
        headline = soup_dp.find('h1', class_="b-article__heading").text.strip()
        # записываем всю информацию с csv
        csv_writer.writerow([f'https://www.dp.ru{link}', headline, text, date, tag])
    csv_file.close()
    return 'Done!'


def main():
    rubrics = get_rubrics()
    print(rubrics)

    # можно пустить по всем рубркам, но получается 7735 статей
    links =  get_all_links(['Новости СПб'], '2019/10')
    # links =  get_all_links(rubrics, '2019/10')
    print(len(links))

    corpus_to_csv(links, 'spb_dp_corpus.csv')
    
if __name__ == '__main__':
    main()
