import requests

url = 'https://api.musixmatch.com/ws/1.1/'
API_KEY = '236e0d15c2fdc11e1d9ffc90054e9c0b'

lyrics = input('Lyrics of song: ')

params = {
    'apikey': API_KEY,
    'q_lyrics': lyrics,
    'q_track': '',
    'f_has_lyrics': 1,
    's_track_rating': 'desc',
    'page_size': 10,
    'page': 1
}

response = requests.get(url + 'track.search', params=params)

if response.status_code == 200:
    data = response.json()
    track_name = data["message"]["body"]["track_list"][0]["track"]["track_name"]
    print(f"The track you are looking for is: {track_name}")
else:
    print("Error:", response.status_code)
