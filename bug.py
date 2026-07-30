# 載入套件
import sys
import requests
import random
from bs4 import BeautifulSoup

# 搜尋字詞
query = 'RPG Maker City Map'

# 設定headers
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

# 執行爬蟲下載搜尋結果頁面標題、URL、og:image、link rel="icon"
url = 'https://www.google.com/search?q=' + query
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
content = soup.find_all('div', class_='tF2Cxc')

results = []
for elem in content:
    title_elem = elem.find('h3')
    if title_elem:
        title = title_elem.getText()
        link = elem.find('a')['href']
        results.append({'title': title, 'link': link})

# 產生HTML
html_output = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Google 搜尋結果</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        ul {
            list-style: none;
            padding: 0;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
        }
        li {
            margin: 10px;
            text-align: center;
            flex: 1 1 300px;
        }
        a {
            text-decoration: none;
            color: #333;
            display: block;
        }
        img {
            width: 100%;
            height: auto;
            border-radius: 5px;
            transition: transform 0.3s ease-in-out;
        }
        img:hover {
            transform: scale(1.1);
        }
    </style>
</head>
<body>
    <h1>Google搜尋結果頁面共有以下標題:</h1>
    <ul>
'''

for result in results:
    html_output += f'''
    <li>
        <a href="{result["link"]}" target="_blank">
            <img src="https://via.placeholder.com/300" alt="{result["title"]}">
            <p>{result["title"]}</p>
        </a>
    </li>
    '''

html_output += '''
    </ul>
</body>
</html>
'''

# 寫入到HTML檔案中
with open('google_search_results.html', 'w', encoding='utf-8') as file:
    file.write(html_output)

print('HTML檔案已經成功建立: google_search_results.html')
