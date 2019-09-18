import unittest
from flask import request
import requests
import json

apiKey = "18F7OZJBE0WJ" #set the api key
limit = 10
search_term = "random"

def get_gif_json(search_term, apiKey, limit):
    r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apiKey, limit)) #get our gifs and applying our parameters
    if r.status_code == 200:
        print(r.json())
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



class GetGifTests(unittest.TestCase):
    
    def test_get_gif_json(self):
        self.assertEqual(get_gif_json(search_term, "RANDOM API KEY", limit), {'error': 'invalid key'}) #this will test if we receive an error invalid key if we have the wrong apiKey

    def test_get_gifs_list(self):
        self.assertEqual(get_gifs_list({"results":[]}), []) #if we pass a json with no results, it should not return an array




if __name__ == "__main__":
    unittest.main()