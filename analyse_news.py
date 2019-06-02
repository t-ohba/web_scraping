#! python3
# analyse_html.py - Leadge.aiの記事を解析

import requests
import bs4
import time

top_res = requests.get('https://ledge.ai/')
top_res.raise_for_status()
top_soup = bs4.BeautifulSoup(top_res.text)  # res.text から beautifulsoupオブジェクトを生成

link_list = top_soup.select('.grid-item > a') # 記事へのリンクを取得
title_list = top_soup.select('article > .grid-item__title') # 記事のタイトルを取得
for i in range(len(title_list)): # 記事以外の要素を削除（style属性が設定されている要素を削除）
    if title_list[i].get('style') != None:
        title_list.remove(title_list[i])

# 記事のタイトルとリンクの一覧を表示
for i in range(len(link_list)):
    print(str(i) + ': ', end='')
    print(title_list[i].getText() + ', ', end='')
    print(link_list[i].get('href'))

# 記事の内容を取得
for i in range(len(link_list)):
    url = link_list[i].get('href')
    article_res = requests.get(url)
    article_res.raise_for_status()

    print('--- ' + title_list[i].getText() + '(' + link_list[i].get('href') + ') ---')
    article_soup = bs4.BeautifulSoup(article_res.text)

    # 見出し
    article_headings = article_soup.select('.entry-content > h2')
    for j in range(len(article_headings)):
        print(article_headings[j].getText())

    # 本文
    article_text = article_soup.select('.entry-content > p')
    for j in range(len(article_text)):
        print(article_text[j].getText())

    print()

    time.sleep(1)