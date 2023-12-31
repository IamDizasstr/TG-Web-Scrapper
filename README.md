TG-MAPS-PARSER (TGMP)

Web Scraper для получения текста креативов с сайта TGMaps. Подойдёт для таргетологов и тех, кто интересуется рекламой конкурентов. Скраппер собирает текст всех рекламных креативов в один файл.

## Описание

Данный проект представляет собой скрипт на языке Python, который использует библиотеку Selenium для автоматизации веб-браузера Firefox. 
Скрипт позволяет автоматически авторизоваться на сайте TGMaps, перейти на страницу с креативами и получить текст каждого креатива, с каждой из представленных страниц. 
На момент написания скраппера их там 220.
Полученный текст сохраняется в файле формата .docx.

## Установка

Для работы с проектом необходимо установить следующие библиотеки:

- Selenium: `pip install selenium`

Также необходимо скачать драйвер для Firefox, который будет использоваться Selenium. Драйвер можно скачать с официального сайта Selenium: [ссылка на скачивание драйвера](https://github.com/mozilla/geckodriver/releases). После скачивания драйвера, разместите его в папке проекта.

## Зависимости

Проект использует следующие зависимости:

- Selenium: [ссылка на документацию Selenium](https://selenium-python.readthedocs.io/)

## Файлы

Проект состоит из следующих файлов:

- `main.py`: Основной файл проекта, содержащий код.
- `creatives.docx`: Файл, в который будет записан текст креативов. (Сохранять файл можно в любом расширении)

## Использование

1. Установите все необходимые зависимости, выполнив команду установки, указанную в разделе "Установка".
2. Скачайте драйвер для Firefox с официального сайта Selenium: [ссылка на скачивание драйвера](https://github.com/mozilla/geckodriver/releases).
3. Разместите скачанный драйвер в папке проекта.
4. Откройте файл `main.py` и укажите свои данные для авторизации на сайте TGMaps (строки 14-15).
5. Запустите файл `main.py` для выполнения скрипта.
6. После выполнения скрипта, текст креативов будет сохранен в файле `creatives.docx`.

## Связь
Для сотрудничества обращаться по адресу электронной почты: vv800180@gmail.com
