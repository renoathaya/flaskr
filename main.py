from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    stuff = "this is <strong>Bold</strong> Text  "
    nasigoreng =["Mawut" ,"Kampung" ,"Pete" ]
    return render_template('index.html' , stuff=stuff , nasigoreng=nasigoreng)

@app.route("/user/<name>")
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def error(e):
    return "Maaf Error" , 404
