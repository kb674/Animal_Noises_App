from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/get_animal', methods=['GET'])
def get_animal():
    return random.choice(['cow', 'dog', 'fox'])

@app.route('/get_noise', methods=['POST'])
def get_noise():
    noises = {
        "cow" : "moo",
        "dog" : "bark",
        "fox" : "what does the fox say"
    }
    return noises[request.data.decode('utf-8')]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)