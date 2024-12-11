DISCLAIMER:
This project is a private code base designed specifically for the UMBC CMSC447 - Software Engineering 1 course of Fall 2024 and is not meant for any other uses (public, commercial, etc.). Any replication or dissemination of any file in this repository is prohibited unless given proper permission from one of the 4 members listed below. The code base is not meant for public hosting and was not designed to handle or adhere to the standard practices used with secure web hosting and any user performing hosting does so at their own risk.
If there are any questions or concerns please contact the school University of Maryland, Baltimore County (UMBC).

UMBC CMSC447 - Group1 Section 1/6 - RecipeRepo README
Members:
* Ethan Cheung - PR49732
* Ryan Edwards - BH89659
* Lily Hagen - KU21177
* Jared Richmond - KT48372

Project Goal:
Implement a web application for users to create, store, upload, and access their favorite recipes from anywhere.

Project Description:
RecipeRepo aims to address these issues by combining useful features from various recipe sites into one seamless application. Users will be able to log in and explore a database of recipes using different filters to easily find the perfect dish. Additionally, RecipeRepo allows users to create their own personalized online cookbook, consolidating recipes in one place for quick and easy access. The platform also gives users the option to add personal notes or modifications to any recipe, tailoring it to their specific needs. With a streamlined user interface and a focus on personalized functionality, RecipeRepo aims to offer a convenient, accessible solution for recipe management anytime, anywhere.

Formal documentation can be found in google drive or upon request.

Project Dependencies:
* blinker==1.8.2
* click==8.1.7
* colorama==0.4.6
* Flask==3.0.3
* Flask-Login==0.6.3
* Flask-SQLAlchemy==3.1.1
* Flask-WTF==1.2.1
* greenlet==3.1.0
* itsdangerous==2.2.0
* Jinja2==3.1.4
* MarkupSafe==2.1.5
* SQLAlchemy==2.0.35
* typing_extensions==4.12.2
* Werkzeug==3.0.4
* WTForms==3.1.2

Initial Setup:
This project will only be able to run locally as online hosting was not developed/implemented within the scope of the project timeline. These steps outlined below need to be followed for successfully setup on your local machine in order for code execution.

1) Download Visual Studio Code IDE
2) Install the latest version of Python
3) Install the latest version of Git and Git Desktop App
4) On Git Desktop App link account with Git Repo for RecipeRepo if not already a member
5) Clone Repository onto your local machine
6) Launch code with VSCODE
7) In VSCODE click on main.py and execute this file. This will launch the site locally

Important Notes:
* Make sure to execute the main.py, that's the only way launch successfully
* Make sure to delete the databse.db file when done to reset the programs database
* The Images linked with the website recipes listed in the static > images folder, might not work as the paths described in the html might not be exact.
