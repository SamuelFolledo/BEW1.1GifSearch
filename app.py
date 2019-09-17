from flask import Flask, render_template, request
import requests
import json
from pprint import pprint #pretty print json

app = Flask(__name__)

@app.route("/") #Home Page #ROUTES are what we type in the browser into browser to go to different pages. We create these using ROUTE DECORATORS, which is a way to add additional functionalities to existing functions. This route decorator will handle all of the complicated backend stuff and simply allow us to write a function that returns the information that will be shown in our website
@app.route("/home") #will access our home page via / or /home
def index():
    """Return homepage."""
    # TODO: Extract query term from url

    # TODO: Make 'params' dict with query term and API key

    apiKey = "18F7OZJBE0WJ" #set the api key
    limit = request.args.get("limit") #set limit
    if limit == None:
        limit = 10

    search_term = request.args.get("search_result") #test search
    if search_term == "" or search_term == None or search_term == " ": #if we have no search then search randomly
        search_term = "random"

    #get our gifs and applying our parameters
    r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apiKey, limit)) #with limit

    gif_list = []
    if r.status_code == 200:
        gif_json = r.json() #load the GIFs using the urls for the smaller GIF sizes
        json_results = gif_json["results"]
        for x in range(int(limit)): #parse through each results
            gif_str = json_results[x]["media"][0]["mediumgif"]["url"] #gives us url for each gifs
            gif_list.append(
                gif_str
            )

    else:
        gif_list = []

    pprint(gif_list)
    return render_template('index.html', gif_list = gif_list)

    # TODO: Make an API call to Tenor using the 'requests' library


    # TODO: Get the first 10 results from the search results

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter



@app.route('/gifs')
def show_gifs():
    print("Hi gifs")




if __name__ == "__main__": #__name__ is main. But if we import this somewhere else, then the name will be the name of our module
    app.run(debug=True) #This conditional is only true if we run this script directly and in development only
