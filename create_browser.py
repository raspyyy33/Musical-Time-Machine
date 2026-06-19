from ytmusicapi import setup
#create a file named headers.txt and copy paste your header request from YouTube music
with open("headers.txt", "r", encoding="utf-8") as f:
    headers = f.read()

setup(filepath="browser.json", headers_raw=headers)
