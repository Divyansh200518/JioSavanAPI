from flask import Flask, request, redirect, jsonify, json
import time
from jiosaavn.Sync import searchSong
from jiosaavn.Sync import song
import os
from traceback import print_exc
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET", 'thankyoutonystark#weloveyou3000')
CORS(app)


@app.route('/')
def home():
    return redirect("https://cyberboysumanjay.github.io/JioSaavnAPI/")


@app.route('/song/')
def search():
    query = request.args.get('query')
    if query:
        search = searchSong(user_query)
        result = song(id=search[0]["id"])['audioUrls']["320_KBPS"]
        return jsonify(result)
    else:
        error = {
            "status": False,
            "error": 'Query is required to search songs!'
        }
        return jsonify(error)

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True, port=os.getenv("PORT", default=5000))
