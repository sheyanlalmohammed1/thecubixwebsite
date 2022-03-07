from flask import Flask
from flask import render_template

app = Flask(__name__)


@ app.route("/")
@ app.route("/home")
def home():
    return render_template("home.html")


@app.route("/articles")
@app.route("/content")
def content():
    return render_template("articlepage.html")


@app.route("/theteam")
@app.route("/thecubixteam")
def theteam():
    return render_template("theteam.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/economicempowermentgraphics")
def economicempowerment():
    return render_template("economicempowermentofficial.html")





@app.route("/2022/01/23/the-relationship-between-globalization-and-economic-inequality")
def therelationshipbetweenglobalizationandeconomicinequality():
    return render_template("therelationshipbetweenglobalizationandeconomicinequality.html")

@app.route("/2021/12/20/climate-change-affecting-economic-inequality-developing-countries")
def climatechangeaffectingeconomicinequalitydevelopingcountries():
    return render_template("climatechangeaffectingeconomicinequalitydevelopingcountries.html")

@app.route("/2021/11/02/intergenerational-income-mobility-affecting-wealth-inequality")
def intergenerationalincomemobilityaffectingwealthinequality():
    return render_template("intergenerationalincomemobilityaffectingwealthinequality.html")