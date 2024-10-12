from flask import Blueprint, render_template, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("Home.html")


@views.route('/MyCookbooks')
# login functionality requirement
def Cookbooks():
    if(current_user.is_authenticated):
        return render_template("MyCookbooks.html", user=current_user)
    else:
        flash('You need to log in to view this page', category='error')
        return redirect(url_for('views.home'))


@views.route('/Explore')
def Explore():
    return render_template("Explore.html")


@views.route('/Account')
def Account():
    if(current_user.is_authenticated):
        return render_template("Account.html", user=current_user)
    
    else:
        flash('You need to log in to view this page', category='error')
        return redirect(url_for('views.home'))