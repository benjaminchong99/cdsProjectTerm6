import requests, json
import langdetect

# 15329078
# musixmatch api base url
base_url = "https://api.musixmatch.com/ws/1.1/"

SHAUN_API_KEY = "758167cadcb031bb4bc8298a2d9c48ea"
PS_API_KEY = "3cde298eb9a3071b0285150ca915e573"
KEY_1 = "93b20ac7348beace6aa213686553f564"
KEY_2 = "e218c513ee6f7f9140de336ea5b1ab58"
KEY_3 = "7d484435f321756468b03582cfdf2947"
KEY_4 = "f484a64a095f02d9262bc1cc09a5b8d9"

def get_track_id(artist_name: str, song_title: str):
    api_call = base_url + "track.search" + "&q_artist=" + artist_name + "&q_track=" + song_title + "&apikey=" + KEY_1
    try:
        request = requests.get(api_call)
        data = request.json()
        
    except requests.exceptions.JSONDecodeError:
        print("JSON error")
        return "JSON error"

    tracks = data["message"]["body"]["track_list"]

    if len(tracks) > 0:
        track_id = tracks[0]["track"]["track_id"]
        has_lyrics = tracks[0]["track"]["has_lyrics"]

        if has_lyrics:
            print(track_id)
            return track_id
        else: 
            print("This track has no lyrics")
            return "This track has no lyrics"
    
    else: 
        print("No track of this title in musixmatch")
        return "No track of this title in musixmatch"
    
def get_lyrics_from_track_id(track_id):
    api_call = base_url + "track.lyrics.get" + "&track_id=" + str(track_id) + "&apikey=" + KEY_1
    try:
        request = requests.get(api_call)
        data = request.json()
    except requests.exceptions.JSONDecodeError:
        print("JSON error")
        return "JSON error"
    
    lyrics = data["message"]["body"]["lyrics"]["lyrics_body"]

    # Check for english lyrics as we only use English for BERT
    try:
        lang = langdetect.detect(lyrics)
        if lang == "en":
            return lyrics
        else:
            return "Not english"
        
    except langdetect.lang_detect_exception.LangDetectException:
        return "lang detect exception"