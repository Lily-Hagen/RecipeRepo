from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)



@auth.route('/login', methods=['GET', 'POST'])
def login():
    # code here

    if (request.method == 'POST'):
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if(user):
            if(check_password_hash(user.password, password)):
                flash('Login Successful.', category='success')
                
            else: # password incorrect
                flash('Invalid PI Login.', category='error')

        else: # user does not exist, the flash is left the same intentionally
            flash('Invalid UDNE Login', category='error')
            
    return render_template("LoginPage.html")



@auth.route('/logout')
def logout():
    return "<h1>Logout<h1>"



@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    data = request.form
    if (request.method == 'POST'):
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        securityQuestion = request.form.get('SecurityQuestionInput')
        securityAnswer = request.form.get('SecurityAnswer')

        user_exists = User.query.filter_by(email=email).first()
        if (user_exists):
            #Post error message saying user with that email alreay exists
            flash('Email Provided Already Has Account!', category='error')
        else:
            #create user
            new_user = User(email=email, first_name=firstname, last_name=lastname, password=generate_password_hash(password1), security_prompt=securityQuestion, security_answer=securityAnswer)
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("Signup.html")