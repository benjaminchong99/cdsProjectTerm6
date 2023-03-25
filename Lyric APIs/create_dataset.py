import json, csv
import musixmatch

file = open("Spotify-2000.csv")

header = ["Title", "Artist", "Top Genre", "Year", "Beats Per Minute (BPM)", "Energy", "Danceability", "Loudness", "Liveness",
           "Valence", "Length (Duration)", "Acousticness", "Speechiness", "Popularity Score", "Lyrics"]

json_err_count = 0
no_lyric_count = 0
no_track_count = 0
not_english_count = 0
langdetect_exc_count = 0

with open("Spotify-2000.csv", 'r') as song_list_file:
    csv_reader = csv.reader(song_list_file)
    next(csv_reader)
    rows = list(csv_reader)

    with open("../Song data/song_data_3.csv", "w", encoding="utf-8", newline="") as song_data_file:
        # create the csv writer
        writer = csv.writer(song_data_file)

        # write a row to the csv file
        # writer.writerow(header)

        for i in range(1400, 1996):
            row = rows[i]
            track_id = musixmatch.get_track_id(row[2], row[1])
            if track_id == "JSON error":
                json_err_count += 1
            elif track_id == "This track has no lyrics":
                no_lyric_count += 1
            elif track_id == "No track of this title in musixmatch":
                no_track_count += 1

            elif track_id:
                lyrics = musixmatch.get_lyrics_from_track_id(track_id)
                if lyrics == "JSON error":
                    json_err_count += 1
                elif lyrics == "Not english":
                    not_english_count += 1
                elif lyrics == "lang detect exception":
                    langdetect_exc_count += 1

                elif lyrics:
                    data_row = [row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                row[9], row[10], row[11], row[12], row[13], row[14], lyrics]
                    writer.writerow(data_row)

print("Number of Json errors: " + str(json_err_count))
print("Number of no lyrics: " + str(no_lyric_count))
print("Number of no tracks: " + str(no_track_count))
print("Number of not english tracks: " + str(not_english_count))
print("Number of lang_detect errors: " + str(langdetect_exc_count))