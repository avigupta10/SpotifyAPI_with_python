import requests
from Spotify_Client_Secrets import *
import json

# user_id = input('Enter your spotify username: ')

'''
ENTER YOUR USER ID IN PLAYLIST_ENDPOINT
'''

PLAYLIST_ENDPOINT = "https://api.spotify.com/v1/users/{user_id}/playlists"
PLAY_ENDPOINT = "https://api.spotify.com/v1/me/player/play"
TOP_ENDPOINT = "https://api.spotify.com/v1/me/top/"
PAUSE_ENDPOINT = "https://api.spotify.com/v1/me/player/pause"
CURRENT_SONG_ENDPOINT = "https://api.spotify.com/v1/me/player/currently-playing"
SEARCH_ENDPOINT = "	https://api.spotify.com/v1/search"
USER_ALBUMS_ENDPOINT = "https://api.spotify.com/v1/me/albums"
BASE_URL = "https://api.spotify.com/v1/me/"


def user_top_artists():
    try:
        response = requests.get(
            TOP_ENDPOINT + 'artists',
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


def user_top_tracks():
    try:
        response = requests.get(
            TOP_ENDPOINT + 'tracks',
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


def user_albums():
    try:
        response = requests.get(
            USER_ALBUMS_ENDPOINT,
            headers={
                'Content-Type': 'application/json',
                "Authorization": f"Bearer {ACCESS_TOKEN}"
            },
        )
        if response.json():
            return response.json()
        else:
            return {'error': '204 NO CONTENT'}
    except:
        return {'Error': 'Issue with request'}


def search(query, type):
    try:
        response = requests.get(
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
    except:
        return {'Error': 'Issue with request'}


# d = search(query="travis+scott", type='artist')['artists']
# print(d['items'][0]['name'])
# print(d['items'][0]['genres'])
# print(d['items'][0]['popularity'])
# print(d['items'][0]['uri'])

def get_user_current_song():
    response = requests.get(
        CURRENT_SONG_ENDPOINT + "?market=ES",
        headers={
            'Content-Type': 'application/json',
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },

    ).json()

    return response


def play_song():
    try:
        response = requests.put(
            PLAY_ENDPOINT,
            headers={
                'Content-Type': 'application/json',
                "Authorization": f"Bearer {ACCESS_TOKEN}"
            },
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


i = 1

while i > 0:
    print("*********************************************")
    print("*********************************************")
    print('Welcome to Spot-Info')
    print("What do you want ?")
    print("1.Search on Spotify")
    print("2.Get your top tracks")
    print("3.Get your top artists")
    print("4.Create playlist")
    print("5.Play your current song")
    print("6.Pause your current song")
    print("7.Get info about your current song")
    print(" ")
    print("*********************************************")
    print("*********************************************")
    print(" ")
    inp = int(input("Enter your choice "))

    if inp == 1:
        query = input("Enter Artist or Album Name")
        type = input("Artist or album ?")
        d = search(query=query, type=type)['artists']
        print(f"Name -> {d['items'][0]['name']}")
        print(d['items'][0]['genres'])
        print(f"Popularity = {d['items'][0]['popularity']}M")
        print(d['items'][0]['uri'])

    elif inp == 2:
        d = user_top_tracks()
        print(f"Name -> {d['items'][0]['name']}")
        print(f"Popularity = {d['items'][0]['popularity']}M")
        print(d['items'][0]['uri'])

    elif inp == 3:
        d = user_top_artists()
        print(f"Name -> {d['items'][0]['name']}")
        print(f"Popularity = {d['items'][0]['popularity']}M")
        print(d['items'][0]['uri'])

    elif inp == 4:
        name = input("Enter the name of your new playlist")
        song = create_playlist(
            name=name,
            public=False
        )
        print(song)

    elif inp == 5:
        print(play_song())

    elif inp == 6:
        print(pause_song())

    elif inp == 7:
        d = get_user_current_song()
        print(f"Name -> {d['item']['name']}")
        print(f"playing? -> {d['is_playing']}")
        print(f"Explicit -> {d['item']['explicit']}")
        print(f"{d['item']['duration_ms']/60000} minutes")
    else:
        print('wrong choice')
    inpu = input("Do you want to continue Y or N")
    if inpu == "Y":
        continue
i = i + 1
