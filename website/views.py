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
        search_term = request.form.get('searchbox', '').strip()

        # Get filter values from the form
        breakfast = request.form.get('is_breakfast')
        lunch = request.form.get('is_lunch')
        dinner = request.form.get('is_dinner')
        snack = request.form.get('is_snack')
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

        query_string_list = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        query = General_Recipe.query

        # Apply search term filter if present
        if search_term:
            query = query.filter(General_Recipe.title.ilike(f"%{search_term}%"))
            query_string_list[0] = search_term

        # Apply filter conditions directly
        if breakfast:
            query = query.filter(General_Recipe.is_breakfast == True)
            query_string_list[1] = 'checked'
        if lunch:
            query = query.filter(General_Recipe.is_lunch == True)
            query_string_list[2] = 'checked'
        if dinner:
            query = query.filter(General_Recipe.is_dinner == True)
            query_string_list[3] = 'checked'
        if snack:
            query = query.filter(General_Recipe.is_snack == True)
            query_string_list[4] = 'checked'
        if appetizer:
            query = query.filter(General_Recipe.is_appetizer == True)
            query_string_list[5] = 'checked'
        if entree:
            query = query.filter(General_Recipe.is_entree == True)
            query_string_list[6] = 'checked'
        if dessert:
            query = query.filter(General_Recipe.is_dessert == True)
            query_string_list[7] = 'checked'
        if sidedish:
            query = query.filter(General_Recipe.is_sidedish == True)
            query_string_list[8] = 'checked'
        if italian:
            query = query.filter(General_Recipe.is_italian == True)
            query_string_list[9] = 'checked'
        if chinese:
            query = query.filter(General_Recipe.is_chinese == True)
            query_string_list[10] = 'checked'
        if mexican:
            query = query.filter(General_Recipe.is_mexican == True)
            query_string_list[11] = 'checked'
        if indian:
            query = query.filter(General_Recipe.is_indian == True)
            query_string_list[12] = 'checked'
        if american:
            query = query.filter(General_Recipe.is_american == True)
            query_string_list[13] = 'checked'
        if mediterranean:
            query = query.filter(General_Recipe.is_mediterranean == True)
            query_string_list[14] = 'checked'

        filtered_recipes = query.all()

        return render_template("Explore.html", recipes=filtered_recipes, query_string_list=query_string_list)
    
    else:
        all_recipes = General_Recipe.query.all()
        return render_template("Explore.html", recipes=all_recipes, query_string_list=['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''])


@views.route('/Account', methods=['GET', 'POST'])
def Account():
    if(current_user.is_authenticated):
        if (request.method == 'POST'):
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            email = request.form.get("email")

            same_email = email == current_user.email
            user_exists = User.query.filter_by(email=email).first()
            if ((not user_exists) or same_email == True):
                current_user.first_name = first_name
                current_user.last_name = last_name
                current_user.email = email
                db.session.commit()

                flash('User details changed successfully', category='success')
            else:
                flash('Email typed in is currently in use', category='error')
            
        return render_template("Account.html", user=current_user)
    
    else:
        flash('You need to log in to view this page', category='error')
        return redirect(url_for('views.home'))
    
@views.route('/RecipeView', methods=['GET', 'POST'])
def RecipeView():
    return render_template("RecipeView.html")