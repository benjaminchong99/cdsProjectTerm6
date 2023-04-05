import csv


header = ["Title", "Artist", "URI", "Danceability", "Energy", "Key", "Loudness", "Mode", "Speechiness",
           "Acousticness", "Instrumentalness", "Liveness", "Valence", "Tempo", "Duration (ms)", "Time signature", 
           "Chorus Hit", "Sections", "Target", "Lyrics"]

with open("./Song data/new_dataset_10s.csv", "r", encoding="utf-8", newline="") as song_data_file:
    csv_reader = csv.reader(song_data_file)
    next(csv_reader)
    rows = list(csv_reader)

    with open("./Song data/10s_cleaned.csv", "a", encoding="utf-8", newline="") as clean_file:
        # create the csv writer
        writer = csv.writer(clean_file)
        writer.writerow(header)

        for row in rows:
            uneditted = row[19]
            cleaned = uneditted.split("...")[0]
            row[19] = cleaned
            writer.writerow(row)

