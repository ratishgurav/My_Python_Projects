import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

date=input("Which year would you like to get the BillBoard Top 100 From?YY-MM-DD: ")

BILL_URL="https://www.billboard.com/charts/hot-100/"+date
header={
    "User-Agent": "Chrome/143.0.0.0"
}
response=requests.get(url=BILL_URL,headers=header)
soup=BeautifulSoup(response.text,'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().split() for song in song_names_spans]
print(song_names)

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/callback",
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),  # Reads from .env
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)