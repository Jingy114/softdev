from flask import Flask
from flask import render_template
from flask import request
import requests
import json

app = Flask(__name__)


f = open('key_nasa.txt', 'r')
key = f.read() 
#key = key.strip() 

@app.route("/")
def index():
    api_url = f"https://api.nasa.gov/planetary/apod?api_key={key}"
    web = requests.get(api_url).json() 
    img_url = web["image"] 
    img_title = web["title"]
    img_expl = web["expl"]
    return render_template("main.html", title=img_title, explanation=img_expl, url=img_url)

if __name__ == "__main__":
    app.debug = True
    app.run()
