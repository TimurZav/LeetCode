import requests
from bs4 import BeautifulSoup

# # providing url
# url = "https://jetlend.ru/wp-content/uploads/jetlend.html"
#
# # opening the url for reading
# html = requests.get(url)
#
# # parsing the html file
# html_parse = BeautifulSoup(html.text, 'html.parser')
#
# count = 0
# for tag in html_parse.find_all():
#     if tag.attrs:
#         count += len(tag.attrs)
# print(count)

# print(sum(len(ele.attrs) + 1 for ele in html_parse.find_all()))
#
# tags_with_attributes = html_parse.find_all(True, attrs=True)
#
# print(f"Количество HTML-тегов с атрибутами: {len(tags_with_attributes)}")




# from html.parser import HTMLParser
# import requests
#
#
# class MyHTMLParser(HTMLParser):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.start_tags = []
#         self.end_tags = []
#
#     def handle_starttag(self, tag, attrs):
#         self.start_tags.append(tag)
#
#     def handle_endtag(self, tag):
#         self.end_tags.append(tag)
#
#
# if __name__ == '__main__':
#     parser = MyHTMLParser()
#
#     html_response = requests.get('https://jetlend.ru/wp-content/uploads/jetlend.html')
#     parser.feed(html_response.text)
#
#     print('Start tags:', len(parser.start_tags))
#     print('End tags:', len(parser.start_tags))
#     print('Amount:', len(parser.start_tags) + len(parser.start_tags))






# HTML-код вашей веб-страницы (замените на свой HTML-код)
html_code = """
<html>
<head>
    <title>Пример страницы</title>
</head>
<body>
    <p class="paragraph">Это абзац с классом</p>
    <a href="https://example.com">Ссылка на example.com</a>
    <div id="container">
        <p>Вложенный абзац
        <div class="test"><span>test<p id=''></p></span></div>
        </p>
    </div>
</body>
</html>
"""

# Создаем объект Beautiful Soup
soup = BeautifulSoup(html_code, 'html.parser')

# Используем метод find_all, чтобы найти все HTML-теги с атрибутами
tags_with_attributes = soup.find_all(attrs=True)

# Выводим количество найденных тегов
print(f"Количество HTML-тегов с атрибутами: {len(tags_with_attributes)}")
print(sum(len(ele.attrs) + 1 for ele in soup.find_all()))

count = sum(len(tag.attrs) for tag in soup.find_all() if tag.attrs)
print(count)
