#! python3
# mapit.py - コマンドラインやクリップボードに指定した住所の地図を開く

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://google.com/maps/place/' + address)