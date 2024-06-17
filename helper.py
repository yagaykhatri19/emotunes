from fer import FER
import cv2
import requests

def get_emotion(img_path):
    img = cv2.imread(img_path) 
    detector = FER()
    emotion, score = detector.top_emotion(img)
    
    return emotion

def getToken():
    url = "https://accounts.spotify.com/api/token"

    client_id = "6b79d5ca83484349bac5b36a2a6dc35b"
    client_secret = "75c5f7f6bd004563ac5fac37cdc01b15"

    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, headers=headers, data=data)

    # print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data.get("access_token")
        return access_token

def getPlaylist(token, emotion):
    playlists = {
        'happy': 'spotify:playlist:37i9dQZF1DWTwbZHrJRIgD',
        'sad': 'spotify:playlist:37i9dQZF1DX3rxVfibe1L0',
        'angry': 'spotify:playlist:37i9dQZF1EIfTmpqlGn32s',
        'surprise': 'spotify:playlist:37i9dQZF1DX2sUQwD7tbmL',
        'neutral': 'spotify:playlist:37i9dQZF1DX0XUfTFmNBRM',
        'disgust': 'spotify:playlist:37i9dQZF1DX3rxVfibe1L0',
        'fear': 'spotify:playlist:37i9dQZF1EIfTmpqlGn32s'
    }
    return playlists.get(emotion)
