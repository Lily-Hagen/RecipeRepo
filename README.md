#### DISCLAIMER:
###### This project is a private code base designed specifically for the UMBC CMSC447 Software Engineering 1 course of Fall 2024, and is not permitted for any other uses (public, commercial, etc.). Any replication or dissemination of the files in this repository is strictly prohibited without explicit permission from one of the project members listed below. The code base is not meant for public hosting and was not designed to comply with industry-standard secure web hosting practices, and any entity hosting does so at their own risk.

#### Contributing:
###### Contributions to this project are limited to the 4 listed members. For additions or changes, please contact the team and submit a pull request through GitHub:
* Ethan Cheung - echeung3@umbc.edu
* Ryan Edwards - ryane2@umbc.edu
* Lily Hagen - Lillian.hagen14@gmail.com
* Jared Richmond - jaredr3@umbc.edu

#### Project Goal:
###### Implement a web application for users to create, store, upload, and access their favorite recipes from any device.

#### Project Description:
###### RecipeRepo integrates features from various recipe sites to address common challenges users face with recipe organization into one seamless application. Users will be able to log in and explore a database of recipes using different filters to easily find the perfect dish. Additionally, RecipeRepo allows users to create their own personalized online cookbook, consolidating recipes in one place for quick and easy access. The platform also gives users the option to add personal notes or modifications to any recipe, tailoring it to their specific needs. With a streamlined user interface and a focus on personalized functionality, RecipeRepo aims to offer a convenient, accessible solution for recipe management anytime, anywhere.

###### Formal documentation can be found in google drive or upon request.

#### Project Dependencies:
* To install the required dependencies, run the following command in your bash project directory: "pip install -r requirements.txt"
* (Ensure requirements.txt contains the list of dependencies below)
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
* (Ensure requirements.txt contains the list of dependencies above)

#### Initial Setup:
###### This project will only be able to run locally as online hosting was not developed/implemented within the scope of the project timeline. These steps outlined below need to be followed for successfully setup on your local machine in order for code execution.

1) Download Visual Studio Code IDE
2) Install the latest version of Python
3) Install the latest version of Git and Git Desktop App
4) Link your GitHub account with the Git Desktop app, and if not already a member, ensure you have access to the RecipeRepo repository
5) Clone Repository onto your local machine
6) Open the cloned repository in VSCode
7) In VSCode, navigate to main.py and execute this file. This will launch the application locally

#### Important Notes:
* If persistent data storage is required, avoid deleting the database.db file after use
* Make sure to execute the main.py, that's the only way launch successfully
* Make sure to delete the databse.db file when done to reset the programs database
* Ensure that the relative paths to images in the static/images folder are correct. If paths are incorrect, update them in the HTML code to match the project's directory structure
* Last Commit on 01/07/2025 at 12:43 - duplicated repository, removed personal information, made public

#### License
###### This project is proprietary and intended solely for academic use in UMBC CMSC447 Software Engineering 1, Fall 2024. All rights reserved.
