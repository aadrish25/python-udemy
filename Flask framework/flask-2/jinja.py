from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__) 


@app.route("/index",methods=["GET"])  
def welcome():
    return render_template("index.html")  


@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method=="POST":
        name=request.form["name-input"]
        return f"Hello {name}!"
    return render_template("form.html")


# variable rule and dynamic url example
@app.route("/success/<int:score>")
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    
    return render_template("result.html",results=res)

# for loop example
@app.route("/success_res/<int:score>")
def success_res(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    
    exp={"score":score,"result":res}
    return render_template("result1.html",results=exp)


# if statement example
@app.route("/success_if/<int:score>")
def success_if(score):
    return render_template("result2.html",results=score)


@app.route("/get_result",methods=["POST","GET"])
def get_result():
    avg_score=0
    if request.method=="POST":
        science=float(request.form["science"])
        math=float(request.form["maths"])
        english=float(request.form["english"])
        computer=float(request.form["computer"])
    else:
        return render_template("get_result.html")
    avg_score=(science+math+english+computer)/4
    return redirect(url_for("success_res",score=avg_score))




# creating an about page
@app.route("/about")
def about_us():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)