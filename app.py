from flask import Flask, render_template, request, jsonify, redirect, url_for
import cv2
import base64
import numpy as np
from helper import get_emotion, getToken, getPlaylist

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('dashboard.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/feature')
def feature():
    return render_template('feature.html')

@app.route('/try', methods=['GET', 'POST'])
def emotunes():
    if request.method == 'POST':
        try:
            data = request.get_json()
            img_data = data['image']
            img_data = base64.b64decode(img_data.split(',')[1])
            np_arr = np.frombuffer(img_data, np.uint8)
            img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            cv2.imwrite('static/images/captured_image.png', img)

            emotion = get_emotion(img_path='static/images/captured_image.png')

            return jsonify({'redirect': '/playlist', 'emotion': emotion})
        except Exception as e:
            return jsonify({'error': str(e)})
    else:
        return render_template('emotunes.html')
    
@app.route('/playlist', methods=['GET', 'POST'])
def playlist():
    emotion = request.args.get('emotion')
    token = getToken()
    playlist_uri = getPlaylist(token, emotion)
    print(playlist_uri)
    return render_template('playlist.html', image='static/images/captured_image.png', emotion=emotion, playlist_uri=playlist_uri)

if __name__ == "__main__":
    app.run(debug=True, port=8000)