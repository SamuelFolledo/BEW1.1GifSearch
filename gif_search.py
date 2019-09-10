import requests
from flask import Flask
from pprint import pprint

app = Flask(__name__)

@app.route('/joke')
def make_joke():
    params = {"limitTo": ["nerdy"]} #create the parameters
    r = requests.get("http://api.icndb.com/jokes/random",params=params)
    joke_json = r.json() #conver
    joke_str = joke_json["value"]
    pprint(joke_str)
    return joke_str
    
make_joke()