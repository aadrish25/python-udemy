from flask import Flask

app=Flask(__name__)


# adding an app route, that takes you to home page
# as soon as we add '/' to our website url, this function will be called
# and the message will be displayed on web page
@app.route("/")
def welcome():
    return "Welcome to Flask course! Flask is fun..."


# creating an index page
# add '/index' to web page url to access this page 
@app.route("/index")
def lets_start():
    return "So lets get started! This is my index page.."


# similarly you can create any number of routes

if __name__=="__main__":
    app.run(debug=True)