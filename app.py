from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/gifs")
def get_gif():

    return render_template("gifs.html")


@app.route("/") #Home Page #ROUTES are what we type in the browser into browser to go to different pages. We create these using ROUTE DECORATORS, which is a way to add additional functionalities to existing functions. This route decorator will handle all of the complicated backend stuff and simply allow us to write a function that returns the information that will be shown in our website
@app.route("/home") #will access our home page via / or /home
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    
    # TODO: Make 'params' dict with query term and API key

    # TODO: Make an API call to Tenor using the 'requests' library

    # TODO: Get the first 10 results from the search results

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter

    


    return render_template("index.html")


if __name__ == "__main__": #__name__ is main. But if we import this somewhere else, then the name will be the name of our module 
    app.run(debug=True) #This conditional is only true if we run this script directly 