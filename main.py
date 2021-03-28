import requests
from Spotify_Client_Secrets import *
import json

# user_id = input('Enter your spotify username: ')

PLAYLIST_ENDPOINT = "https://api.spotify.com/v1/users/317vxru6yl74egib5kuayaf4qt44/playlists"
PLAY_ENDPOINT = "https://api.spotify.com/v1/me/player/play"
PAUSE_ENDPOINT = "https://api.spotify.com/v1/me/player/pause"
CURRENT_SONG_ENDPOINT = "https://api.spotify.com/v1/me/player/currently-playing"
SEARCH_ENDPOINT = "	https://api.spotify.com/v1/search"
BASE_URL = "https://api.spotify.com/v1/me/"


def search(query, type):
    try:
        response = requests.put(
            SEARCH_ENDPOINT + f"?query={query}&type={type}",
            headers={
                'Content-Type': 'application/json',
                "Authorization": f"Bearer {ACCESS_TOKEN}"
            },
        )
        if response.json():
            return response.json()
        else:
            return {'error': '204 NO CONTENT'}
    except json.JSONDecodeError as e:
        return {'Error': 'Issue with request'}


def get_user_current_song():
    response = requests.get(
        CURRENT_SONG_ENDPOINT + "?market=ES",
        headers={
            'Content-Type': 'application/json',
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },

    ).json()

    return response


def play_song(context_uri, offset):
    try:
        response = requests.put(
            PLAY_ENDPOINT,
            headers={
                'Content-Type': 'application/json',
                "Authorization": f"Bearer {ACCESS_TOKEN}"
            },
            # json={
            #     "context_uri": context_uri,
            #     "offset": offset
            # }
        )
        if response.json():
            return response.json()
        else:
            return {'error': '204 NO CONTENT'}
    except:
        return {'Error': 'Issue with request'}


def pause_song():
    try:
        response = requests.put(
            PLAY_ENDPOINT,
            headers={
                'Content-Type': 'application/json',
                "Authorization": f"Bearer {ACCESS_TOKEN}"
            },
            # json={
            #     "context_uri": context_uri,
            #     "offset": offset
            # }
        )
        if response.json():
            return response.json()
        else:
            return {'error': '204 NO CONTENT'}
    except json.JSONDecodeError as e:
        return {'Error': 'Issue with request'}


def create_playlist(name, public):
    response = requests.post(
        PLAYLIST_ENDPOINT,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json={
            "name": name,
            "public": public
        }
    )
    data = response.json()
    return data


def main():
    song = create_playlist(
        name="SpotifyAPI",
        public=False
    )
    print(song)


print('Welcome to Spot-Info')
print("What do you want ?")
print("1.Search on Spotify")

if __name__ == '__main__':
    main()
