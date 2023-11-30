# pip install pyshorteners
# pip install pyperclip

import pyshorteners
url = input('Enter the url:\n')

def shortenurl(url):
    s = pyshorteners.Shortener()

    print(s.tinyurl.short(url))
    

shortenurl(url)    