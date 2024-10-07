from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("Home.html")


@views.route('/MyCookbooks')
def Cookbooks():
    return render_template("MyCookbooks.html")


@views.route('/Explore')
def Explore():
    return render_template("Explore.html")

@views.route('/Account')
def Account():
    return render_template("Account.html")