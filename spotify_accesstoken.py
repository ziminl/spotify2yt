import requests

#https://developer.spotify.com/dashboard

SPOTIFY_CLIENT_ID = ""
SPOTIFY_CLIENT_SECRET = ""

url = "https://accounts.spotify.com/api/token"
data = {
    "grant_type": "client_credentials",
    "client_id": SPOTIFY_CLIENT_ID,
    "client_secret": SPOTIFY_CLIENT_SECRET,
}

response = requests.post(url, data=data)
token_info = response.json()

if "access_token" in token_info:
    print(f"token: {token_info['access_token']}")
else:
    print(f"fail {token_info}")
