# GIF Search Project

## About
This Gif search project displays randomized gifs from [Tenor's](https://tenor.com) API on the home page. The amount of Gifs displayed is defaulted at 10 but can be change by utilizing a **drop down**. The default searched results is random but the **search bar** can also be used to find a specific Gifs. Feel free to use and download any gifs using our site created with [Tenor's](https://tenor.com/gifapi/documentation#quickstart) API, Flask, and Jinja templates.

![Gif Screenshot](/screenshot.png)

## Authors
* **Samuel P. Folledo and Padyn Riddell** - [Padyn's GitHub](https://github.com/squeaky1273)



## Requirements
1) The page must use templates
2) The page must display GIFs (10 at the most)
3) GIFs should appear in a single vertical list
4) At the top of the page there should be a page title
5)Below the title there should be a search bar with a “Search” button near it (placement up to you, but needs to be on one side of the bar)
6) Users should be able to type a string into the search bar, press the search button, and be shown up to 10 GIFs related to the search query
7) GIFs should be displayed on a fresh load of the page, i.e. before a query has even been typed.
8) GIFs should only update once a user has pressed the “Search” button
9) If no GIFs could be found for the search term, display an error message saying that no GIFs could be found, and to try another search query
10) The following elements should have some custom styling (i.e. CSS rules) added to them:</br>
- Page title</br>
    -  Search Bar</br>
    - Search Button
11) All code must be commented with a description of what the code is doing, expected input, and expected output
## Stretch Requirements/Challenges (Optional)
- Add a gitignore file and edit it so that “.DS_Store” and “.env” won’t get tracked in Git. What else shouldn't be tracked?
- Center-align everything on the page
- Display the GIFs in a grid instead of a list
- Add a button that displays the top 10 trending GIFs on Tenor
- Add a button that displays 10 random GIFs on Tenor
- Type-ahead: as the user types in the search box, the page is reloading the gifs to match the search query in real time (no longer needing to click the search button)



# How to Use This Starter Code

To create your own repository using this code:

1. Clone the repository onto your computer using the `git clone` command
1. Run `git remote remove origin` to disconnect the code from Make-School-Labs
1. In GitHub.com, create your own repository. **IMPORTANT**: Do not add a README
1. Run `git remote add origin git@github.com:YOUR_USERNAME/YOUR_REPO_NAME.git`, replacing YOUR_USERNAME with your username and YOUR_REPO_NAME with your repository name
1. Now you should be able to add, commit, and push as normal!

# How to Run This Starter Code

You may need to install `flask` and/or `requests`. To do so, run:

```bash
pip3 install flask
pip3 install requests
```

To run, open the folder containing `app.py` in a Terminal instance, and run:

```bash
export FLASK_ENV=development
flask run
```

# Resources

You may find the following resources helpful in your development process:

1. [Tenor API Documentation](https://tenor.com/gifapi/documentation) - useful for understanding which URL we want to visit in order to make an API request for GIFs
1. [BEW 1.1 Lesson on Flask](https://make-school-courses.github.io/BEW-1.1-RESTful-and-Resourceful-MVC-Architecture/#/./Lessons/03-Intro-to-Flask/README)
1. [BEW 1.1 Lesson on Templates](https://make-school-courses.github.io/BEW-1.1-RESTful-and-Resourceful-MVC-Architecture/#/./Lessons/04-Flask-Templating/README)
1. [BEW 1.1 Lesson on APIs](https://make-school-courses.github.io/BEW-1.1-RESTful-and-Resourceful-MVC-Architecture/#/./Lessons/05-URLs-HTTP-REST-and-Reading-Errors/README)

# Shout out to Dani for being the best Back End instructor!!!