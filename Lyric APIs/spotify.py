import json, csv, requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

import cred, getlyrics

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                                    client_id=cred.client_id, client_secret= cred.client_secret,
                                    redirect_uri=cred.redirect_url))

# artist = sp.search(q="artist:" + "Bob Dylan", type="artist")
# artist_id = artist["artists"]["items"][0]["id"]

# artist_albums = sp.artist_albums(artist_id, limit=3)

def get_albums_from_artist_name(name):
  results = sp.search(q = "artist:" + name, type = "artist")
  items = results["artists"]["items"]
  if len(items) == 0:
    return None
  else:
    d = items[0]

  # get artistID and artist name from dict
  artistID = d["id"]     
  artistName = d["name"]   

  artistUri = "spotify:artist:" + artistID

  results = sp.artist_albums(artistUri, limit=1)
  albums = results["items"]
  while results["next"]:
    results = sp.next(results)
    albums.extend(results["items"])

  unique = set() # ignore duplicate albums
  for album in albums:
    name = album["name"]
    if not name in unique: 
      unique.add(name) # unique is a set

  print ("\nAlbums by %s:\n" %(artistName))
  unique = list(unique)
  return unique



def get_tracks_from_album(album):
  tracks = []
  results = sp.search(q="album" + album, type="album")
  
  # get the first album uri
  album_id = results['albums']['items'][0]['uri']

  # get album tracks
  tracks = sp.album_tracks(album_id)
  return tracks['items']

  # for track in tracks['items']:
  #   song_row = get_track_row(track, album, artistName)
     
  
def get_track_row(track, album, artistName):
  track_name = track['name']
  track_id = track['id']
  print("Track name: " + track_name)
  print("Track id: " + track_id)
  track_data = get_track(track)
  track_popularity = get_track_popularity(track_data)
  # track_lyrics = getlyrics.findlyrics(artistName, track_name)
  # if track_lyrics == "error" or track_lyrics == "":
  #   return "error"
  # return [artistName, album, track_name, track_popularity, track_lyrics]
  return [artistName, album, track_name, track_popularity]

def get_track(track):
  track_id = track['id']
  return sp.track(track_id)

def get_track_popularity(track_data):
  return str(track_data['popularity'])


results = sp.search(q="song:Viva La Vida&artist=Coldplay")
for i in range(10):
  print("id: " + results["tracks"]["items"][i]["id"] + " popularity: " + str(results["tracks"]["items"][i]["popularity"]))