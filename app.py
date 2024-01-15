from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
from  random_dog import random__dog, random__cat


load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    
    return render_template('index.html', context={'dog':random__dog(), 'cat':random__cat()})

@app.route("/cat")
def cat():
    
    return render_template('cat.html', context={'img':random__cat()})


@app.route("/dog")
def dog():
    
    return render_template('dog.html', context={'img':random__dog()})


if __name__ == '__main__':
    app.run(debug=os.getenv("DEBUG"), port=os.getenv("PORT"))
