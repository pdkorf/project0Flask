import datetime
from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.static_url_path = '/static'

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

cont = [["Your website must contain at least four different .html pages, and it should be possible to get from any page on your website to any other page by following one or more hyperlinks.", False]
, ["Your website must include at least one list (ordered or unordered), at least one table, and at least one image.", True]
, ["Your website must have at least one stylesheet file.", True]
, ["Your stylesheet(s) must use at least five different CSS properties, and at least five different types of CSS selectors. You must use the #id selector at least once, and the .class selector at least once.", True]
, ["Your stylesheet(s) must include at least one mobile-responsive @media query, such that something about the styling changes for smaller screens.",True]
, ["Your stylesheet(s) must include at least one mobile-responsive @media query, such that something about the styling changes for smaller screens.", True]
, ["Your stylesheets must use at least one SCSS variable, at least one example of SCSS nesting, and at least one use of SCSS inheritance.",True]
, ["In README.md, include a short writeup describing your project, what’s contained in each file, and (optionally) any other additional information the staff should know about your project.",True]]

#notes = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index.html')
def home():
    return render_template("index.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/about.html')
def about():
    column1 = "First column"
    column2 = "Second column"
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("about.html", column1=column1, column2=column2, new_year=new_year)

@app.route('/content.html')
def content():
    return render_template("content.html", cont=cont)

@app.route('/hello', methods=["POST", "GET"])
def hello():
    if request.method == "GET":
        return "Please fill in the form"
    else:
        name = request.form.get("name")
        return render_template("hello.html", name=name)

@app.route('/note', methods=["GET", "POST"])
def note():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)
    return render_template("note.html", notes=session["notes"])
