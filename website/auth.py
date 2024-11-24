from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)



@auth.route('/login', methods=['GET', 'POST'])
def login():
    # code here
    if (current_user.is_authenticated):
        flash('Cannot Access Login, You Are Already Logged In.', category='error')
        return redirect(url_for('views.home'))
    
    if (request.method == 'POST'):
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if(user):
            if(check_password_hash(user.password, password)):
                flash('Login Successful.', category='success')
                login_user(user, remember=True) # logs the user in, passes in to pages with flask module thingy
                return redirect(url_for('views.home'))
                
            else: # password incorrect
                flash('Failed to login, please check your username and/or password.', category='error')

        else: # user does not exist, the flash is left the same intentionally
            flash('Failed to login, please try again.', category='error')
            
    return render_template("LoginPage.html")



@auth.route('/logout')
# @login_required # login functionality requirement
def logout():
    if(current_user.is_authenticated):
        logout_user()
        flash('You have successfully logged out.', category='success')
        return redirect(url_for('views.home'))
    else:
        flash('You are not currently logged in.', category='error')
        return redirect(url_for('views.home'))




@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if (current_user.is_authenticated):
        flash('Cannot Access Account Sign Up While Logged In.', category='error')
        return redirect(url_for('views.home'))

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

            login_user(new_user, remember=True) # create and pass in user object 

            return redirect(url_for('views.home'))

    return render_template("Signup.html", user=current_user)



@auth.route('/forgotPassword1', methods=['GET', 'POST'])
def forgotPassword1():
    if (request.method == 'POST'):
        email = request.form.get('email')

        user_exists = User.query.filter_by(email=email).first()
        if (user_exists):
            return redirect(url_for('auth.forgotPassword2', email=email))
        else:
            flash("Email Provided Doesn't Have An Account!", category='error')
    
    return render_template("forgotPassword1.html")



@auth.route('/forgotPassword2', methods=['GET', 'POST'])
def forgotPassword2():
    if (request.method == 'GET'):
        email = request.args.get('email')
        if (not email):
            return redirect(url_for('views.home'))
        else:
            user = User.query.filter_by(email=email).first()
            secPrompt = user.security_prompt
            
            if (secPrompt == 1):
                secPrompt = "Name of the street you grew up on"
            elif (secPrompt == 2):
                secPrompt = "Mother's maiden name"
            elif (secPrompt == 3):
                secPrompt = "Name of your favorite childhood pet"
            elif (secPrompt == 4):
                secPrompt = "Title of your favorite movie"
            
            return render_template("forgotPassword2.html", email=email, secPrompt=secPrompt)

    if (request.method == 'POST'):
        email = request.form.get('email')
        secPrompt = request.form.get('SecurityQuestionInput')
        user = User.query.filter_by(email=email).first()
        secAnswer = request.form.get('SecurityAnswer')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if (secAnswer == user.security_answer):
            #Change Password to New Password and Make suree to has the password
            user.password = generate_password_hash(password1)
            db.session.commit()
            flash('Password Change Successful. Proceed to Login.', category='success')
            return redirect(url_for('views.home'))
        else:
            flash('The Answer The Security Question Is Incorrect. Password Change Failed!', category='error')
            return render_template("forgotPassword2.html", email=email, secPrompt=secPrompt)
    
    return redirect(url_for('views.home'))