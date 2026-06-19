import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
URL = "https://appbrewery.github.io/bakeboard-hot-100/" + date + "/"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"}
response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
title_tags = soup.find_all(name="h3", class_="chart-entry__title")
title_list = []

for tag in title_tags:
    title_list.append(tag.getText())

ytmusic = YTMusic("browser.json")

playlist_lib = ytmusic.get_library_playlists()
playlist_name = date + " Billboard 100"
found = False

for playlist in playlist_lib:
    compare_title = playlist["title"]
    if compare_title == playlist_name:
        found = True
        break

if found == False:
    playlist_id = ytmusic.create_playlist(title=playlist_name, description=f"top 100 songs in {date}")
else:
    print("Title already exists")

for song in title_list:
    try:
        found_music = ytmusic.search(query=song, filter="songs", limit=1)
        ytmusic.add_playlist_items(playlist_id, [found_music[0]["videoId"]])
        print(f"Added: {song}")
    except Exception as e:
        print(f"Skipped: {song} | Reason: {e}")
