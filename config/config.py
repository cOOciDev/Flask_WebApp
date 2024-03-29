import os

# Define the base directory of the Flask application
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'your_secret_key'  # Change this to a random value
    DEBUG = True  # Set to False in production
    
    # DATA BASE
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False