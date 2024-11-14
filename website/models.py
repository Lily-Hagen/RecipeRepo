from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    password = db.Column(db.String(150))
    security_prompt = db.Column(db.Integer)
    security_answer = db.Column(db.String(150))
    cookbooks = db.relationship('Cookbook')
    cookbook_recipes = db.relationship('Cookbook_Recipe')




class General_Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    image_url = db.Column(db.String(100))
    ingredients = db.Column(db.String(1500))
    optional_ingredients = db.Column(db.String(1500))
    instructions = db.Column(db.String(1500))
    serving_size = db.Column(db.String(100))
    prep_time = db.Column(db.String(100))
    cook_time = db.Column(db.String(100))
    is_breakfast = db.Column(db.Integer)
    is_lunch = db.Column(db.Integer)
    is_dinner = db.Column(db.Integer)
    is_snack = db.Column(db.Integer)
    is_appetizer = db.Column(db.Integer)
    is_entree = db.Column(db.Integer)
    is_dessert = db.Column(db.Integer)
    is_sidedish = db.Column(db.Integer)
    is_american = db.Column(db.Integer)
    is_chinese = db.Column(db.Integer)
    is_indian = db.Column(db.Integer)
    is_italian = db.Column(db.Integer)
    is_mediterranean = db.Column(db.Integer)
    is_mexican = db.Column(db.Integer)

class Cookbook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(100))
    description = db.Column(db.String(1500))
    recipe_count = db.Column(db.Integer, default=0)
    recipes = db.relationship('Cookbook_Recipe')


class Cookbook_Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    cookbook_id = db.Column(db.Integer, db.ForeignKey('cookbook.id'))
    title = db.Column(db.String(100))
    image_url = db.Column(db.String(100))
    ingredients = db.Column(db.String(1500))
    optional_ingredients = db.Column(db.String(1500))
    instructions = db.Column(db.String(1500))
    serving_size = db.Column(db.String(100))
    prep_time = db.Column(db.String(100))
    cook_time = db.Column(db.String(100))
    notes = db.Column(db.String(1500))
    is_breakfast = db.Column(db.Integer)
    is_lunch = db.Column(db.Integer)
    is_dinner = db.Column(db.Integer)
    is_snack = db.Column(db.Integer)
    is_appetizer = db.Column(db.Integer)
    is_entree = db.Column(db.Integer)
    is_dessert = db.Column(db.Integer)
    is_sidedish = db.Column(db.Integer)
    is_american = db.Column(db.Integer)
    is_chinese = db.Column(db.Integer)
    is_indian = db.Column(db.Integer)
    is_italian = db.Column(db.Integer)
    is_mediterranean = db.Column(db.Integer)
    is_mexican = db.Column(db.Integer)