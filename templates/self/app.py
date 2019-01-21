from flask import Flask ,render_template , request
import csv


app = Flask(__name__)

@app.route("/")
def home():
    f = open("all.csv","r",encoding="utf-8")
    al = csv.reader(f)
    return render_template("home.html", al = al)
    
@app.route("/new")
def new():
    return render_template("new.html")
    

