from flask import Flask,render_template,request

app=Flask(__name__) # WSGI


@app.route("/index",methods=["GET"])  # by default, the method is 'GET' 
def welcome():
    return render_template("index.html")  

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="POST":
        name=request.form["name-input"]
        return f"Hello {name}!"
    return render_template("form.html")


@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method=="POST":
        name=request.form["name-input"]
        return f"Hello {name}!"
    return render_template("form.html")


# creating an about page
@app.route("/about")
def about_us():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)