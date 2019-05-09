#! python3

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt') # Webページをダウンロード
print(type(res))
print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text[:250])

play_file = open('RomeoAndJuliet.txt', 'wb') # ダウンロードしたデータをローカルに保存
for chunk in res.iter_content(100000):
    play_file.write(chunk)
play_file.close()

res = requests.get('https://automatetheboringstuff.com/files/page_that_does_not_exist')
try:
    res.raise_for_status() # エラーをチェック
except Exception as exc:
    print('There is a problem: {}'.format(exc))

