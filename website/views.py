from flask import Blueprint, render_template, url_for, redirect, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, General_Recipe, Cookbook, Cookbook_Recipe
from . import db


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("Home.html")


@views.route('/MyCookbooks', methods=['GET', 'POST'])
# login functionality requirement
def Cookbooks():
    if(current_user.is_authenticated):
        if (request.method == 'POST'):
            if (request.form.get('HiddenCreateCookbookFormIdentifier') == "CreateCookbookForm"):
                title = request.form.get('cookbook_title')
                description = request.form.get('cookbook_desc')
                
                new_cookbook = Cookbook(user_id=current_user.id, title=title, description=description, recipe_count=0)
                db.session.add(new_cookbook)
                db.session.commit()
                flash('Cookbook Created!', category='success')
            elif (request.form.get('HiddenDeleteForm') != ""):
                cookbook_id = request.form.get('HiddenDeleteForm')
                cookbook_exists = Cookbook.query.filter_by(user_id=current_user.id, id=cookbook_id).first()
                if (cookbook_exists):
                    associated_cookbook_recipes = Cookbook_Recipe.query.filter_by(user_id=current_user.id, cookbook_id=cookbook_id).all()
                    if (associated_cookbook_recipes):
                        for cb_recipe in associated_cookbook_recipes:
                            db.session.delete(cb_recipe)
                        db.session.commit()
                    db.session.delete(cookbook_exists)
                    db.session.commit()
                    flash('Cookbook Successfully Deleted!', category='success')

            return render_template("MyCookbooks.html", user=current_user)
        else:    
            return render_template("MyCookbooks.html", user=current_user)
    else:
        flash('You need to log in to view this page', category='error')
        return redirect(url_for('views.home'))


@views.route('/CookbookView', methods=['GET', 'POST'])
def CookbookView():
    cookbook_id = request.args.get('cookbook_id')
    if (not cookbook_id or request.method != 'GET'):
        if (cookbook_id and request.method == 'POST'):
            if (request.form.get('CookbookViewFilterFormCheck')):
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
                query = Cookbook_Recipe.query.filter(Cookbook_Recipe.user_id==current_user.id, Cookbook_Recipe.cookbook_id==cookbook_id)

                # Apply search term filter if present
                if search_term:
                    query = query.filter(Cookbook_Recipe.title.ilike(f"%{search_term}%"))
                    query_string_list[0] = search_term

                # Filter by meal type
                if breakfast:
                    query = query.filter(Cookbook_Recipe.is_breakfast == True)
                    query_string_list[1] = 'checked'
                if lunch:
                    query = query.filter(Cookbook_Recipe.is_lunch == True)
                    query_string_list[2] = 'checked'
                if dinner:
                    query = query.filter(Cookbook_Recipe.is_dinner == True)
                    query_string_list[3] = 'checked'
                if snack:
                    query = query.filter(Cookbook_Recipe.is_snack == True)
                    query_string_list[4] = 'checked'
                if appetizer:
                    query = query.filter(Cookbook_Recipe.is_appetizer == True)
                    query_string_list[5] = 'checked'
                if entree:
                    query = query.filter(Cookbook_Recipe.is_entree == True)
                    query_string_list[6] = 'checked'
                if dessert:
                    query = query.filter(Cookbook_Recipe.is_dessert == True)
                    query_string_list[7] = 'checked'
                if sidedish:
                    query = query.filter(Cookbook_Recipe.is_sidedish == True)
                    query_string_list[8] = 'checked'

                # Cuisine filters
                cuisine_filters = []
                if american:
                    cuisine_filters.append(Cookbook_Recipe.is_american)
                    query_string_list[9] = 'checked'
                if chinese:
                    cuisine_filters.append(Cookbook_Recipe.is_chinese)
                    query_string_list[10] = 'checked'
                if indian:
                    cuisine_filters.append(Cookbook_Recipe.is_indian)
                    query_string_list[11] = 'checked'
                if italian:
                    cuisine_filters.append(Cookbook_Recipe.is_italian)
                    query_string_list[12] = 'checked'
                if mediterranean:
                    cuisine_filters.append(Cookbook_Recipe.is_mediterranean)
                    query_string_list[13] = 'checked'
                if mexican:
                    cuisine_filters.append(Cookbook_Recipe.is_mexican)
                    query_string_list[14] = 'checked'

                # Query for recipes matching all selected cuisines
                primary_query = query
                for filter_condition in cuisine_filters:
                    primary_query = primary_query.filter(filter_condition == True)
                primary_recipes = primary_query.all()

                # Query for recipes matching any selected cuisine
                secondary_query = query
                if cuisine_filters:
                    secondary_query = secondary_query.filter(
                        db.or_(*[filter_condition == True for filter_condition in cuisine_filters])
                    )
                secondary_recipes = secondary_query.all()

                # Combine the primary and secondary recipes, ensuring no duplicates
                filtered_recipes = primary_recipes + [recipe for recipe in secondary_recipes if recipe not in primary_recipes]
                
                the_cookbook = Cookbook.query.filter_by(user_id=current_user.id, id=cookbook_id).first()
                return render_template("CookbookView.html", user=current_user, the_cookbook=the_cookbook, recipes=filtered_recipes, query_string_list=query_string_list)
        
        return redirect(url_for('views.home'))
    else:
        the_cookbook = Cookbook.query.filter_by(user_id=current_user.id, id=cookbook_id).first()
        cookbook_recipes = Cookbook_Recipe.query.filter_by(user_id=current_user.id, cookbook_id=cookbook_id).all()
        return render_template("CookbookView.html", user=current_user, the_cookbook=the_cookbook, recipes=cookbook_recipes, query_string_list=['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''])



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

        # Filter by meal type
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

        # Cuisine filters
        cuisine_filters = []
        if american:
            cuisine_filters.append(General_Recipe.is_american)
            query_string_list[9] = 'checked'
        if chinese:
            cuisine_filters.append(General_Recipe.is_chinese)
            query_string_list[10] = 'checked'
        if indian:
            cuisine_filters.append(General_Recipe.is_indian)
            query_string_list[11] = 'checked'
        if italian:
            cuisine_filters.append(General_Recipe.is_italian)
            query_string_list[12] = 'checked'
        if mediterranean:
            cuisine_filters.append(General_Recipe.is_mediterranean)
            query_string_list[13] = 'checked'
        if mexican:
            cuisine_filters.append(General_Recipe.is_mexican)
            query_string_list[14] = 'checked'

        # Query for recipes matching all selected cuisines
        primary_query = query
        for filter_condition in cuisine_filters:
            primary_query = primary_query.filter(filter_condition == True)
        primary_recipes = primary_query.all()

        # Query for recipes matching any selected cuisine
        secondary_query = query
        if cuisine_filters:
            secondary_query = secondary_query.filter(
                db.or_(*[filter_condition == True for filter_condition in cuisine_filters])
            )
        secondary_recipes = secondary_query.all()

        # Combine the primary and secondary recipes, ensuring no duplicates
        filtered_recipes = primary_recipes + [recipe for recipe in secondary_recipes if recipe not in primary_recipes]

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
    recipe_id = request.args.get('recipe_id')
    if (not recipe_id or request.method != 'GET'):
        if (recipe_id and request.method == 'POST'):
            recipe = General_Recipe.query.filter_by(id=recipe_id).first()
            for cb in current_user.cookbooks:
                if (request.form.get(str(cb.id))):
                    new_cb_recipe = Cookbook_Recipe(user_id=current_user.id, cookbook_id=cb.id,
                                        title = recipe.title, 
                                        image_url = recipe.image_url, 
                                        ingredients = recipe.ingredients, 
                                        optional_ingredients = recipe.optional_ingredients,
                                        instructions = recipe.instructions,
                                        serving_size = recipe.serving_size, 
                                        prep_time = recipe.prep_time, 
                                        cook_time = recipe.cook_time,
                                        notes = "",
                                        is_breakfast = recipe.is_breakfast, 
                                        is_lunch = recipe.is_lunch, 
                                        is_dinner = recipe.is_dinner,
                                        is_appetizer = recipe.is_appetizer, 
                                        is_entree = recipe.is_entree, 
                                        is_dessert = recipe.is_dessert,
                                        is_sidedish = recipe.is_sidedish,
                                        is_american = recipe.is_american,
                                        is_chinese = recipe.is_chinese, 
                                        is_indian = recipe.is_indian,
                                        is_italian = recipe.is_italian,
                                        is_mediterranean = recipe.is_mediterranean, 
                                        is_mexican = recipe.is_mexican)
                    db.session.add(new_cb_recipe)

                    the_cookbook = Cookbook.query.filter_by(id=cb.id, user_id=current_user.id).first()
                    if (the_cookbook):
                        the_cookbook.recipe_count += 1
                    db.session.commit()
                    
            flash('Recipe Added Successfully!', category='success')
            ingredient_list = recipe.ingredients.split('\n')
            opt_ingredient_list = []
            opt_ingredient_list = recipe.optional_ingredients.split('\n')
            instruction_list = recipe.instructions.split('\n')
            return render_template("RecipeView.html", recipe=recipe, ingredient_list=ingredient_list, opt_ingredient_list=opt_ingredient_list, instruction_list=instruction_list)
        
        return redirect(url_for('views.Explore'))
    else:
        recipe = General_Recipe.query.filter_by(id=recipe_id).first()
        ingredient_list = recipe.ingredients.split('\n')
        opt_ingredient_list = []
        opt_ingredient_list = recipe.optional_ingredients.split('\n')
        instruction_list = recipe.instructions.split('\n')
        return render_template("RecipeView.html", recipe=recipe, ingredient_list=ingredient_list, opt_ingredient_list=opt_ingredient_list, instruction_list=instruction_list)