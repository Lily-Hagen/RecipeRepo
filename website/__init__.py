from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
import json

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'M@cr0M@rt'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User
    from .models import General_Recipe


    create_database(app)
    seed_recipe_data(app, General_Recipe)
    
    login_manager = LoginManager() # initialize flask login manager
    login_manager.login_view = 'auth.login' # pull from auth.login
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
   

    return app

#Checking for the path might be redundant code so we can research some more and see if its needed.
def create_database(app):
    if not path.exists('instance/' + DB_NAME):
        with app.app_context():
            db.create_all()

def seed_recipe_data(app, General_Recipe):
    if not path.exists('instance/' + DB_NAME):
        create_database(app)
    else:
        with app.app_context():
            if (General_Recipe.query.first()):
                recipes = General_Recipe.query.all()
                for recs in recipes:
                    db.session.delete(recs)
                db.session.commit()

            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, 'general_recipe.json')
            json_data = json.load(open(file_path))

            for recipe in json_data:
                ingredients_string = "\n".join(recipe['ingredients'])
                instructions_string = "\n".join(recipe['instructions'])
                gen_rec = General_Recipe(title=recipe['title'], image_url=recipe['image_url'], ingredients=ingredients_string, instructions=instructions_string,
                                         serving_size=recipe['serving_size'], prep_time=recipe['prep_time'], cook_time=recipe['cook_time'],
                                         is_breakfast=recipe['is_breakfast'], is_lunch=recipe['is_lunch'], is_dinner=recipe['is_dinner'], is_appetizer=recipe['is_appetizer'],
                                         is_entree=recipe['is_entree'], is_dessert=recipe['is_dessert'], is_sidedish=recipe['is_sidedish'], is_italian=recipe['is_italian'],
                                         is_chinese=recipe['is_chinese'], is_mexican=recipe['is_mexican'], is_indian=recipe['is_indian'], is_american=recipe['is_american'],
                                         is_mediterranean=recipe['is_mediterranean'])
                db.session.add(gen_rec)
                
            db.session.commit()
            