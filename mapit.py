#! python3
# mapit.py - コマンドラインやクリップボードに指定した住所の地図を開く

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]) # コマンドラインから住所を取得する
else:
    address = pyperclip.paste() # クリップボードから住所を取得する

webbrowser.open('https://google.com/maps/place/' + address)