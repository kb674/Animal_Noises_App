from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import requests

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')

class Animals(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String(50), nullable = False)
    noise = db.Column(db.String(50), nullable = False)
    

@app.route('/')
def home():
    animal = requests.get('http://animal-api:5000/get_animal')
    noise = requests.post('http://animal-api:5000/get_noise', data=animal.text)
   

    last_five_animals = Animals.query.all()
    db.session.add( Animals( type = animal.text, noise = noise.text ) )
    db.session.commit()

    return render_template('index.html', animal=animal.text, noise=noise.text, last_five_animals=last_five_animals)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)