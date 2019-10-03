from flask import Flask, render_template, request
import requests
import json
from pprint import pprint #pretty print json
import os #needed for .env
from dotenv import load_dotenv #needed for .env
load_dotenv() #needed for .env

app = Flask(__name__)

TENOR_API_KEY = os.getenv("TENOR_API_KEY") #set the api key #get it from our invisible .ENV file

@app.route("/") #Home Page #ROUTES are what we type in the browser into browser to go to different pages. We create these using ROUTE DECORATORS, which is a way to add additional functionalities to existing functions. This route decorator will handle all of the complicated backend stuff and simply allow us to write a function that returns the information that will be shown in our website
@app.route("/home") #will access our home page via / or /home
def index(): #homepage
    limit = request.args.get("search_limit",10) #set limit, if none then put 10
    search_term = request.args.get("search_result", "random") #search_term will contain search_result, else it will be random
    
    gif_json = get_gif_json(search_term, TENOR_API_KEY, limit)

    gif_list = get_gifs_list(gif_json)

    return render_template('index.html', gif_list = gif_list)

def get_gif_json(search_term, apiKey, limit):
    r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apiKey, limit)) #get our gifs and applying our parameters
    if r.status_code == 200:
        return r.json() #return json
    else:
        return None


def get_gifs_list(gif_json):
    gif_list = []
    json_results = gif_json["results"] #grab the results
    for json_result in json_results: #parse through each results
        gif_str = json_result["media"][0]["mediumgif"]["url"] #gives us url for each gifs
        gif_list.append(gif_str)
    return gif_list

if __name__ == "__main__": #__name__ is main. But if we import this somewhere else, then the name will be the name of our module
    app.run(debug=True) #This conditional is only true if we run this script directly and in development only
