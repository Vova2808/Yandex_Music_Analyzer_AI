from flask import Flask, request, render_template, Response, stream_with_context
import requests
import ollama

app = Flask(__name__)

def get_tracks_from_playlist(playlist_url):
    try:
        user_login = playlist_url.split('/')[4]
        playlist_id = playlist_url.split('/')[6]

        api_url = f"https://api.music.yandex.net/users/{user_login}/playlists/{playlist_id}"
        response = requests.get(api_url)

        if response.status_code == 200:
            playlist_data = response.json()
            tracks = playlist_data.get('result', {}).get('tracks', [])
            if tracks:
                return [track.get('track', {}).get('title', 'Без названия') for track in tracks]
            else:
                return ["Треки не найдены в плейлисте."]
        else:
            return [f"Ошибка при получении данных: {response.status_code}"]
    except Exception as e:
        return [f"Ошибка обработки URL: {str(e)}"]

def analyze_personality_stream(tracks):
    model = 'llama3.1'
    tracks_text = "\n".join(tracks)
    messages = [
        {
            "role": "system",
            "content": (
                "Ты — эксперт по психологии музыки. На основе треков из плейлиста анализируй музыкальные вкусы человека "
                "и подробно описывай его личность, интересы, привычки, эмоциональное состояние и характер. "
                "Отвечай развернуто, с примерами и только на русском языке."
            )
        },
        {
            "role": "user",
            "content": f"Вот список треков из плейлиста:\n{tracks_text}\nОпиши личность владельца этого плейлиста подробно."
        }
    ]
    stream = ollama.chat(model=model, messages=messages, stream=True)
    for chunk in stream:
        yield chunk['message']['content']

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    playlist_url = request.form.get("playlist_url")
    tracks = get_tracks_from_playlist(playlist_url)

    if tracks and "Ошибка" not in tracks[0]:
        return Response(stream_with_context(analyze_personality_stream(tracks)), content_type='text/event-stream')
    else:
        error_message = tracks[0] if tracks else "Ошибка при обработке плейлиста."
        return Response(error_message, content_type='text/plain')

if __name__ == "__main__":
    app.run(debug=True)
