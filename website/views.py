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
        search_term = request.form.get('search', '').strip()

        # Get filter values from the form
        breakfast = request.form.get('is_breakfast')
        lunch = request.form.get('is_lunch')
        dinner = request.form.get('is_dinner')
        appetizer = request.form.get('is_appetizer')
        entree = request.form.get('is_entree')
        dessert = request.form.get('is_dessert')
        sidedish = request.form.get('is_sidedish')
        italian = request.form.get('is_italian')
        chinese = request.form.get('is_chinese')
        mexican = request.form.get('is_mexican')
        indian = request.form.get('is_indian')
        american = request.form.get('is_american')
        mediterranean = request.form.get('is_mediterranean')

        query = General_Recipe.query

        # Apply search term filter if present
        if search_term:
            query = query.filter(General_Recipe.title.ilike(f"%{search_term}%"))

        # Apply filter conditions directly
        if breakfast:
            query = query.filter(General_Recipe.is_breakfast == True)
        if lunch:
            query = query.filter(General_Recipe.is_lunch == True)
        if dinner:
            query = query.filter(General_Recipe.is_dinner == True)
        if appetizer:
            query = query.filter(General_Recipe.is_appetizer == True)
        if entree:
            query = query.filter(General_Recipe.is_entree == True)
        if dessert:
            query = query.filter(General_Recipe.is_dessert == True)
        if sidedish:
            query = query.filter(General_Recipe.is_sidedish == True)
        if italian:
            query = query.filter(General_Recipe.is_italian == True)
        if chinese:
            query = query.filter(General_Recipe.is_chinese == True)
        if mexican:
            query = query.filter(General_Recipe.is_mexican == True)
        if indian:
            query = query.filter(General_Recipe.is_indian == True)
        if american:
            query = query.filter(General_Recipe.is_american == True)
        if mediterranean:
            query = query.filter(General_Recipe.is_mediterranean == True)

        filtered_recipes = query.all()
        return render_template("Explore.html", recipes=filtered_recipes)
    
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