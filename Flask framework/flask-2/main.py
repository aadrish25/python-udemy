from flask import Flask,render_template

app=Flask(__name__) # WSGI


@app.route("/index")
def welcome():
    return render_template("index.html")  # it will search for the 'index.html' inside the templates folder
                                          # so you must make a folder with name templates, and all templates should be stored inside it

# creating an about page
@app.route("/about")
def about_us():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)