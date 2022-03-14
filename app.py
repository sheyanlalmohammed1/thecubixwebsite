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

@app.route("/2021/11/14/economic-inequality-caused-by-climate-change-developed-countries")
def economicinequalitycausedbyclimatechangedevelopedcountries():
    return render_template("economicinequalitycausedbyclimatechangedevelopedcountries.html")

@app.route("/2021/08/13/equal-investment-opportunity-to-balance-economic-opportunity")
def equalinvestmentopportunitytobalanceeconomicopportunity():
    return render_template("equalinvestmentopportunitytobalanceeconomicopportunity.html")

@app.route("/2021/07/21/the-broad-solution-to-solving-wealth-inequality-the-pathway")
def thebroadsolutiontosolvingwealthinequalitythepathway():
    return render_template("thebroadsolutiontosolvingwealthinequalitythepathway.html")

@app.route("/2021/06/22/the-broad-solution-to-solving-wealth-inequality-the-organization")
def thebroadsolutiontosolvingwealthinequalitytheorganization():
    return render_template("thebroadsolutiontosolvingwealthinequalitytheorganization.html")

@app.route("/2021/06/15/taking-a-needed-step-towards-solving-wealth-inequality-the-introduction")
def takinganeededsteptowardssolvingwealthinequalitytheintroduction():
    return render_template("takinganeededsteptowardssolvingwealthinequalitytheintroduction.html")

@app.route("/2021/04/09/the-thought-of-inflation")
def thethoughtofinflation():
    return render_template("thethoughtofinflation.html")

@app.route("/2021/04/01/what-exactly-the-ship-stuck-in-the-suez-canal-meant-to-the-economy")
def whatexactlytheshipstuckinthesuezcanalmeanttotheeconomy():
    return render_template("whatexactlytheshipstuckinthesuezcanalmeanttotheeconomy.html")