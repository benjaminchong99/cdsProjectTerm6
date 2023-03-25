import json, csv, requests
import spotify
import getlyrics
import musixmatch

file = open('songs.json')
songlist = json.load(file)["songs"]

file = open("Spotify-2000.csv")

header = ["Artist", "Song title", "Popularity Score", "Lyrics"]

# with open("Spotify-2000.csv", 'r') as song_list_file:
#     csv_reader = csv.reader(song_list_file)
#     next(csv_reader)

#     with open("song_data_4.csv", "w", encoding="utf-8", newline="") as song_data_file:
#         # create the csv writer
#         writer = csv.writer(song_data_file)

#         # write a row to the csv file
#         writer.writerow(header)

#         for row in csv_reader:
#             try:
#                 lyrics = getlyrics.findlyrics(row[2], row[1])
#                 if lyrics == "error":
#                     continue
#                 elif lyrics == "":
#                     continue
#                 else:
#                     data_row = [row[2], row[1], row[13], getlyrics.findlyrics(row[2], row[1])]
#                     writer.writerow(data_row)
#             except requests.exceptions.TooManyRedirects:
#                 continue
        
        


# open the file in the write mode
# with open('song_popularity.csv', 'w', encoding="utf-8") as f:
#     # create the csv writer
#     writer = csv.writer(f)

#     # write a row to the csv file
#     writer.writerow(header)

#     for song in songlist:
#         artist_name = song["artist"]
#         albums = spotify.get_albums_from_artist_name(artist_name)

#         for album in albums:
#             tracks = spotify.get_tracks_from_album(album)

#             for track in tracks:
#                 track_row = spotify.get_track_row(track, album, artist_name)
#                 if track_row == "error":
#                     continue
#                 else:
#                     writer.writerow(track_row)
#                     writer.writerow("\n")


with open("Spotify-2000.csv", 'r') as song_list_file:
    csv_reader = csv.reader(song_list_file)
    next(csv_reader)

    with open("song_data_musixmatch.csv", "w", encoding="utf-8", newline="") as song_data_file:
        # create the csv writer
        writer = csv.writer(song_data_file)

        # write a row to the csv file
        writer.writerow(header)

        for row in csv_reader:
            track_id = musixmatch.get_track_id(row[2], row[1])
            if track_id:
                lyrics = musixmatch.get_lyrics_from_track_id(track_id)
                if lyrics: 
                    data_row = [row[2], row[1], row[14], lyrics]
                    writer.writerow(data_row)
