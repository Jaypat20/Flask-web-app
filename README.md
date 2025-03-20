My Flask App
Welcome to the My Flask App project! This application is built using Python’s Flask framework and uses a SQLite database to store user records. The project is structured to be easy to set up, run, and test. Follow the instructions below to get started.

Table of Contents
Project Overview
Prerequisites
Project Structure
Setup Instructions
Running the Application
Adding New Records
Running Unit Tests
Additional Notes
Project Overview
This project is a simple web application built with Flask. It displays a webpage that shows a list of user records from a database. The application uses:

Flask Blueprints: To organize routes (pages) within the app.
SQLAlchemy: As an Object-Relational Mapping (ORM) tool to interact with a SQLite database.
HTML Templates: To display user records using an existing HTML file (without modifications except to display records).
Unit Tests: To ensure that the application’s main functions work as expected.
Prerequisites
Before setting up the project, ensure you have the following installed on your system:

Python 3.7 or later: This is the programming language used.
pip: Python’s package installer (usually comes with Python).

Project Structure
Here is a quick overview of the main parts of the project:

/my_flask_app
├── app
│   ├── __init__.py       # Initializes the Flask app and database.
│   ├── models.py         # Contains the database model for user records.
│   ├── routes.py         # Contains web routes (pages) using Flask Blueprints.
│   └── templates
│       └── users.html    # HTML template to display user records.
├── config.py             # Configuration file for the app (database, secret key, etc.)
├── query.py              # Utility script to add new records to the database.
├── run.py                # Main script to launch the application.
├── requirements.txt      # List of Python packages required to run the app.
└── tests
    └── test_app.py       # Unit tests to verify application functionality.
Setup Instructions
Step 1: Download the Project
Download or Clone the Repository:
If you have Git installed, open a terminal (command prompt) and type:
git clone https://github.com/your-username/my_flask_app.git

Alternatively, download the ZIP file from the repository and extract it to a folder on your computer.

Step 2: Install Dependencies
Navigate to the Project Folder:

Open a terminal (or command prompt).
Change directory to the project folder:
bash
Copy
Edit
cd my_flask_app
Create a Virtual Environment:

Create a new virtual environment:
python -m venv venv
Activate the virtual environment:
On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate
Install the Required Packages:

Run the following command:
pip install -r requirements.txt
This will install Flask, SQLAlchemy, and any other necessary packages.
Running the Application
Start the Web Application:

In the terminal (with the virtual environment activated), run:
python run.py
The application will start running on your local server. Typically, it will be accessible at http://127.0.0.1:5000/ in your web browser.
Visit the Homepage:

Open your web browser and go to http://127.0.0.1:5000/
You should see a simple text page saying "Simple Text Page."
View the Users Page:

Navigate to http://127.0.0.1:5000/users
This page displays the list of user records stored in the database.
Adding New Records
The project provides a script called query.py to add new records to the database.

To add a new user, open a terminal and run:
python query.py
Customize the script as needed:
The script includes a function to add a user with a given name and email.
You can modify the values directly in the script for testing, or use this as a reference to add more users programmatically.
Running Unit Tests
The project includes a set of unit tests to verify the application’s functionality. To run these tests:

Ensure the virtual environment is activated.
Run the tests using the following command:
python -m unittest discover tests
Review the test output:
The tests will run and display a summary. All tests should pass, confirming that the main functionality of the app works as expected.
Additional Notes
Database File:

The application uses a SQLite database file named app.db located in the project’s root directory.
