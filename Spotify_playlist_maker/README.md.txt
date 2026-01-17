# 🎵 Billboard to Spotify Time Machine

A Python script that automates the creation of a Spotify playlist based on the Billboard Hot 100 charts from any date in history.

## 📌 Overview
This tool scrapes the top 100 songs from the Billboard website for a user-specified date and uses the Spotify API to create a private playlist with those tracks. It handles authentication securely and matches songs by title and year.

## 🚀 Features
- **Historical Data Scraping:** Extracts song titles from Billboard.com using `BeautifulSoup`.
- **Spotify Integration:** Uses `Spotipy` to authenticate and interact with the Spotify Web API.
- **Smart Search:** Filters Spotify search results by year to improve match accuracy.
- **Automated Playlist Creation:** Generates a new private playlist and populates it with the found tracks.

## 🛠️ Prerequisites
- Python 3.x
- A Spotify Developer Account (to get Client ID and Secret)
- Spotify Account (Free or Premium)

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>

SPOTIPY_CLIENT_ID=your_client_id_here
SPOTIPY_CLIENT_SECRET=your_client_secret_here