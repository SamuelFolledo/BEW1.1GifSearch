import requests
from flask import Flask
from pprint import pprint

app = Flask(__name__)

@app.route("/") #Home Page #ROUTES are what we type in the browser into browser to go to different pages. We create these using ROUTE DECORATORS, which is a way to add additional functionalities to existing functions. This route decorator will handle all of the complicated backend stuff and simply allow us to write a function that returns the information that will be shown in our website
def home():
    return "Hello World"

@app.route('/joke')
def make_joke():
    params = {"limitTo": ["nerdy"]} #create the parameters
    r = requests.get("http://api.icndb.com/jokes/random",params=params)
    joke_json = r.json() #conver
    joke_str = joke_json["value"]
    pprint(joke_str)
    return joke_str
    
if __name__ == "__main__": #__name__ is main. But if we import this somewhere else, then the name will be the name of our module 
    app.run(debug=True) #This conditional is only true if we run this script directly