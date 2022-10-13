from flask import Flask ,request,render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")
@app.route("/submit",methods=['POST','GET'])
def Average():
    if request.method=="POST":
        mark1=int(request.form["social"])
        mark2=int(request.form["science"])
        mark3=int(request.form["tamil"])
        mark4=int(request.form["English"])
        mark5=int(request.form["Maths"])
        r=int(mark1+mark2+mark3+mark4+mark5/ 5)
        if(r>50):
            s="you get passed"
            result= s
        else:
            s="sorry better luck next time"
            result= s
        return render_template("submit.html",result=result)

if __name__=="__main__":
    app.run(debug=True)
