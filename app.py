import requests

from flask import Flask, request, redirect, jsonify, json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def getSongData(query):
    response_API = requests.get(f'https://www.jiosaavn.com/api.php?__call=search.getResults&p=0&n=6&q={query}&_format=json&_marker=00&ctx=wap6dot0')
    data = response_API.text
    data = json.loads(data)
    dataArray = []
    for i in range(len(data["results"])):
        songUrl = data["results"][i]["media_preview_url"]
        songUrl = songUrl.replace("preview.saavncdn.com", "aac.saavncdn.com")
        songUrl = songUrl.replace("_96_p", "_320")
        
        imageUrl = data["results"][i]["image"]
        imageUrl = imageUrl.replace("150x150","500x500")

        artistName = data["results"][i]["singers"]

        songName = data["results"][i]["song"]

        dataArray.append({'songLink': songUrl, 'songName': songName,'songBanner':imageUrl,'artName':artistName})

    return dataArray

@app.route('/')
def search():
    dataArray = []
    query = request.args.get('query')
    if query:
        dataArray = getSongData(query)
        searchLength = len(dataArray)
        if searchLength > 0:
            return jsonify(dataArray)
        else:
            return jsonify({'searchQuery':query,'searchedData':dataArray})
        
    else:
        error = {
            "status": False,
            "error": 'Query is required to search songs!'
        }
        return jsonify(error)

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True,host="0.0.0.0", port=os.getenv("PORT", default=5000))
