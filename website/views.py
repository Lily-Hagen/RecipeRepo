from flask import Blueprint, render_template, url_for, redirect, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, General_Recipe
from . import db


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


@views.route('/Explore', methods=['GET', 'POST'])
def Explore():
    if (request.method == 'POST'):
        return render_template("Explore.html")
    else:
        all_recipes = General_Recipe.query.all()
        return render_template("Explore.html", recipes=all_recipes)


@views.route('/Account')
def Account():
    if(current_user.is_authenticated):
        return render_template("Account.html", user=current_user)
    
    else:
        flash('You need to log in to view this page', category='error')
        return redirect(url_for('views.home'))
    
@views.route('/RecipeView', methods=['GET', 'POST'])
def RecipeView():
    return render_template("RecipeView.html")