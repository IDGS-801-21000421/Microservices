import requests
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/videos-page')
def videos_page():
    return render_template('videos.html')

@app.route('/usuarios/<path:path>', methods=['POST', 'GET'])
def usuarios(path):
    response = requests.request(
        method=request.method,
        url=f"http://localhost:5001/{path}",
        json=request.json
    )
    return jsonify(response.json()), response.status_code

@app.route('/videos', methods=['GET', 'POST'])
def videos():
    if request.method == 'GET':
        response = requests.get('http://localhost:5002/videos')
    else: # POST
        response = requests.post('http://localhost:5002/videos',
                                 json=request.json,
                                 headers={'Content-Type': 'application/json'})

    return jsonify(response.json()), response.status_code


if __name__ == "__main__":
    app.run(port=5000, debug=True)
