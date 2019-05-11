#! python3
# analyse_html.py - HTMLを解析

import requests
import bs4

res = requests.get('http://nostarch.com')
print(res.raise_for_status())
no_starch_soup = bs4.BeautifulSoup(res.text) # res.text から beautifulsoupオブジェクトを生成
print(type(no_starch_soup))

example_file = open('example.html')
example_soup = bs4.BeautifulSoup(example_file) # ローカルに保存したHTMLファイルから beautifulsoupオブジェクトを制し
elems = example_soup.select('#author') # id属性がauthorである要素を見つける
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

p_elems = example_soup.select('p') # <p>要素を取り出す
for i in range(len(p_elems)):
    print(str(p_elems[i])) # <p>要素の文字列を取得
    print(p_elems[i].getText()) # <p>要素の内部テキストを取得

span_elem = example_soup.select('span')[0]
print(str(span_elem))
print(span_elem.get('id')) # id属性の阿多を取得
