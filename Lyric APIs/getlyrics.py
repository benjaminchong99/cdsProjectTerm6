import requests
import re
from bs4 import BeautifulSoup

def findlyrics(artist, songTitle):
    song_lyrics = ""
    # search for the song using track name and artist name
    edited_songTitle = songTitle.lower()
    edited_songTitle = re.sub(" ", "-", edited_songTitle)
    edited_songTitle = edited_songTitle.replace(".", "")
    edited_artist = artist.lower()
    edited_artist = re.sub(" ", "-", edited_artist)
    # print(edited_songTitle, edited_artist)

    # start to search for the song below
    url = f"https://www.songlyrics.com/{edited_artist}/{edited_songTitle}-lyrics/"
    # print(url)
    session = requests.Session()
    session.max_redirects = 60
    r = session.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.find(id="songLyricsDiv")
    results = str(results)
    # print("Results: ", results)
    if results.__contains__("Sorry, we have no"):
        return "error"
    else:
        # scraping with regex
        initialgrab = re.findall(">[\w\s,!'â€~]+", results)
        print("Initialgrab: ", initialgrab)

        for clause in initialgrab:
            clause = re.sub("[>\nâ€~]", "", clause)
            print("Clause: ", clause)
            if clause == "":
                return "error"
            if "We do not have the lyrics" in clause:
                return "error"
            if clause != "":
                song_lyrics += clause
                song_lyrics += "\n"
            
        return song_lyrics
